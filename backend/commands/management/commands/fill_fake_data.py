from random import choice, randint

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from faker import Faker

from backend.commands import models

fake = Faker()


def make_text(min_paragraphs, max_paragraphs):
    return '\n'.join(
        fake.paragraphs(nb=randint(min_paragraphs, max_paragraphs))
    )


class Command(BaseCommand):
    help = 'Fill fake data for dev server'

    def handle(self, *args, **options):
        self._create_admin_user()
        groups = self._create_groups()
        commands = self._create_commands(groups=groups)
        self._create_calls(commands=commands)
        self.stdout.write(self.style.SUCCESS('Fake data filled!'))

    @staticmethod
    def _create_admin_user():
        return get_user_model().objects.create_user(
            username='admin',
            password='password13',
            is_staff=True,
            is_superuser=True,
        )

    def _create_groups(self):
        groups = []
        for _ in range(15):
            group = models.Group(
                title=fake.slug(),
                description=make_text(1, 3),
            )
            group.save()
            groups.append(group)
        return groups

    def _create_commands(self, groups):
        commands = []
        for _ in range(100):
            command = models.Command(
                group=choice(groups),
                title=fake.slug(),
                description=make_text(1, 3),
                body=choice(['ls .', 'pwd', 'time', 'date']),
                is_disabled=choice([True, False, False]),
            )
            command.save()
            commands.append(command)
        return commands

    def _create_calls(self, commands):
        for _ in range(1000):
            models.Call(
                command=choice(commands),
                source=choice([
                    models.Call.API,
                    models.Call.ADMIN,
                ]),
                result=choice([
                    models.Call.SUCCESS_RESULT,
                    models.Call.FAIL_RESULT,
                ]),
                output=make_text(1, 3),
            ).save()
