from django.core.exceptions import PermissionDenied
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views import View

from . import models


class RunCommand(View):

    def post(self, request, group, command):
        token = request.META.get('HTTP_ACCESS_TOKEN')

        if not self._check_permission(token):
            raise PermissionDenied

        return self._run_command(group, command)

    def _check_permission(self, token):
        if not token:
            return False

        token_obj = models.AccessToken.objects.filter(token=token).first()

        if token_obj is None or not token_obj.is_active():
            return False

        return True

    def _run_command(self, group, command):
        command = get_object_or_404(
            models.Command,
            title=command,
            group__title=group,
            is_disabled=False,
        )
        return JsonResponse(command.run(source=models.Call.API))
