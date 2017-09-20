from django.test import TestCase
from django.urls import reverse

from . import factories


class GroupModelTest(TestCase):

    def test_string_representation(self):
        group = factories.GroupFactory()
        assert str(group) == group.title


class CommandModelTest(TestCase):

    def test_string_representation(self):
        command = factories.CommandFactory()
        assert str(command) == f'{command.group.title} - {command.title}'

    def test_run(self):
        command = factories.CommandFactory(body='''
            test=123
            echo $test
        ''')
        assert command.run() == '123\n'


class RunCommandViewTest(TestCase):

    def test_404(self):
        response = self.client.post(reverse('commands:run-command', kwargs={
            'group': 'test-group',
            'command': 'test-command',
        }))
        assert response.status_code == 404

    def test_success(self):
        command = factories.CommandFactory(body='''
            test=123
            echo $test
        ''')

        response = self.client.post(reverse('commands:run-command', kwargs={
            'group': command.group.title,
            'command': command.title,
        }))

        assert response.status_code == 200
        assert response.json() == {'result': '123\n'}

    def test_error(self):
        command = factories.CommandFactory(body='wrong')
        response = self.client.post(reverse('commands:run-command', kwargs={
            'group': command.group.title,
            'command': command.title,
        }))
        assert response.status_code == 200
        assert response.json() == {
            'error': "Command 'wrong' returned non-zero exit status 127.",
        }
