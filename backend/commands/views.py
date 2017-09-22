from django.core.exceptions import PermissionDenied
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views import View

from . import models


class RunCommand(View):

    def post(self, request, group, command):
        token = self._get_actual_token(request.META.get('HTTP_ACCESS_TOKEN'))
        if token is None:
            raise PermissionDenied

        command = self._get_command_or_404(group, command)

        if not token.has_permission(command.group):
            raise PermissionDenied

        return JsonResponse(command.run(source=models.Call.API, token=token))

    def _get_actual_token(self, token):
        token_obj = models.AccessToken.objects.filter(token=token).first()
        if token_obj and not token_obj.is_active():
            return None
        return token_obj

    def _get_command_or_404(self, group, command):
        return get_object_or_404(
            models.Command,
            title=command,
            group__title=group,
            is_disabled=False,
        )
