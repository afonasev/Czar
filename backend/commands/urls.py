from django.conf.urls import url

from .views import RunCommand

app_name = 'commands'

urlpatterns = [
    url(
        r'^(?P<group>[-\w]+)/(?P<command>[-\w]+)/$',
        RunCommand.as_view(),
        name='run-command',
    ),
]
