from datetime import timedelta

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from . import factories, models
from .management.commands import fill_fake_data


class GroupModelTest(TestCase):

    def test_string_representation(self):
        group = factories.GroupFactory()
        assert str(group) == group.title


class CommandModelTest(TestCase):

    def test_string_representation(self):
        command = factories.CommandFactory()
        assert str(command) == f'{command.group.title} - {command.title}'

    def test_run_success(self):
        command = factories.CommandFactory(body='test=123; echo $test')
        assert command.run(models.Call.API) == {models.SUCCESS: '123\n'}

        call = command.calls.first()
        assert call.output == '123\n'
        assert call.result == models.Call.SUCCESS_RESULT
        assert call.source == models.Call.API

    def test_run_fail(self):
        command = factories.CommandFactory(body='wrong')
        expected_output = "Command 'wrong' returned non-zero exit status 127."
        assert command.run(models.Call.ADMIN) == {models.FAIL: expected_output}

        call = command.calls.first()
        assert call.output == expected_output
        assert call.result == models.Call.FAIL_RESULT
        assert call.source == models.Call.ADMIN


class CallModelTest(TestCase):

    def test_string_representation(self):
        call = factories.CallFactory()
        assert str(call) == f'{call.command} - {call.time}'


class AccessTokenModelTest(TestCase):

    def test_string_representation(self):
        token = factories.AccessTokenFactory()
        assert str(token) == token.token

    def test_is_active(self):
        token = factories.AccessTokenFactory()
        assert token.is_active()

    def test_is_active_for_not_expired(self):
        expired_at = timezone.now() + timedelta(days=1)
        token = factories.AccessTokenFactory(expired_at=expired_at)
        assert token.is_active()

    def test_is_active_for_expired(self):
        expired_at = timezone.now() - timedelta(days=1)
        token = factories.AccessTokenFactory(expired_at=expired_at)
        assert not token.is_active()

    def test_is_active_for_disabled(self):
        token = factories.AccessTokenFactory(is_disabled=True)
        assert not token.is_active()


class RunCommandViewTest(TestCase):

    def test_unknown_command_404(self):
        response = self.client.post(reverse('commands:run-command', kwargs={
            'group': 'test-group',
            'command': 'test-command',
        }), HTTP_ACCESS_TOKEN=factories.AccessTokenFactory().token)
        assert response.status_code == 404

    def test_success(self):
        command = factories.CommandFactory(body='test=123; echo $test')
        response = self.client.post(reverse('commands:run-command', kwargs={
            'group': command.group.title,
            'command': command.title,
        }), HTTP_ACCESS_TOKEN=factories.AccessTokenFactory().token)

        assert response.status_code == 200
        assert response.json() == {models.SUCCESS: '123\n'}
        assert command.calls.first().source == models.Call.API

    def test_fail(self):
        command = factories.CommandFactory(body='wrong')
        response = self.client.post(reverse('commands:run-command', kwargs={
            'group': command.group.title,
            'command': command.title,
        }), HTTP_ACCESS_TOKEN=factories.AccessTokenFactory().token)

        assert response.status_code == 200
        assert response.json() == {
            models.FAIL: "Command 'wrong' returned non-zero exit status 127.",
        }
        assert command.calls.first().source == models.Call.API

    def test_disabled_command_404(self):
        command = factories.CommandFactory(is_disabled=True)
        response = self.client.post(reverse('commands:run-command', kwargs={
            'group': command.group.title,
            'command': command.title,
        }), HTTP_ACCESS_TOKEN=factories.AccessTokenFactory().token)
        assert response.status_code == 404


class RunCommandViewPermissionTest(TestCase):

    def test_without_token_403(self):
        command = factories.CommandFactory()
        response = self.client.post(reverse('commands:run-command', kwargs={
            'group': command.group.title,
            'command': command.title,
        }))
        assert response.status_code == 403

    def test_unknown_token_403(self):
        command = factories.CommandFactory()
        response = self.client.post(reverse('commands:run-command', kwargs={
            'group': command.group.title,
            'command': command.title,
        }), HTTP_ACCESS_TOKEN='wrong_token')
        assert response.status_code == 403

    def test_not_active_token_403(self):
        token = factories.AccessTokenFactory(is_disabled=True).token
        command = factories.CommandFactory()
        response = self.client.post(reverse('commands:run-command', kwargs={
            'group': command.group.title,
            'command': command.title,
        }), HTTP_ACCESS_TOKEN=token)
        assert response.status_code == 403


class FillFakeDataTest(TestCase):

    def test_run(self):
        fill_fake_data.Command().handle()
