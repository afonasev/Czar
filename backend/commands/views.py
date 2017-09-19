
from django.http import HttpResponse


def hello_world(request):  # pylint:disable=unused-argument
    return HttpResponse('Hello world!')
