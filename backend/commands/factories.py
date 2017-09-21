import factory

from . import models


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'auth.User'

    username = factory.Faker('user_name')
    password = factory.Faker('password')


class GroupFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'commands.Group'

    title = factory.Faker('word')


class CommandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'commands.Command'

    group = factory.SubFactory(GroupFactory)
    title = factory.Faker('word')
    body = factory.Faker('text')


class CallFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'commands.Call'

    command = factory.SubFactory(CommandFactory)
    source = models.Call.API
    result = models.Call.SUCCESS_RESULT
    output = factory.Faker('text')


class AccessTokenFactory(factory.DjangoModelFactory):
    class Meta:
        model = 'commands.AccessToken'

    user = factory.SubFactory(UserFactory)
    token = models.generate_token()
