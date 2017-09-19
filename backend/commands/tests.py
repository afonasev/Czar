from django.test import TestCase
from django.urls import reverse


class HelloWorldTest(TestCase):

    def test(self):
        response = self.client.get(reverse('commands:hello-world'))
        assert response.status_code == 200
