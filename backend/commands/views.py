import subprocess

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views import View

from . import models


class RunCommand(View):

    # pylint:disable=unused-argument
    def post(self, request, group, command):
        command = get_object_or_404(
            models.Command, title=command, group__title=group,
        )

        result = {}
        try:
            result['result'] = command.run()
        except subprocess.CalledProcessError as exc:
            result['error'] = str(exc)

        return JsonResponse(result)
