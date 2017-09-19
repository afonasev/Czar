from django.conf.urls import url

from .views import hello_world

app_name = 'commands'

urlpatterns = [
    url(r'^$', hello_world, name='hello-world'),
]
