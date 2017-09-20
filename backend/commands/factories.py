import factory


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
