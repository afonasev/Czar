from django.contrib import admin

from . import models


class CommandsInline(admin.TabularInline):

    extra = 0
    model = models.Command


@admin.register(models.Group)
class Group(admin.ModelAdmin):

    inlines = (CommandsInline, )
    list_display = ('title', 'description')


@admin.register(models.Command)
class Command(admin.ModelAdmin):

    list_display = ('group', 'title', 'description', 'is_disabled')
    list_editable = ('is_disabled', )
    list_filter = ('group', 'is_disabled')
    actions = ('run_commands', )

    # pylint:disable=unused-argument
    def run_commands(self, request, queryset):
        for command in queryset:
            command.run(source=models.Call.ADMIN)

    run_commands.short_description = 'Run commands'


@admin.register(models.Call)
class Call(admin.ModelAdmin):

    date_hierarchy = 'time'
    list_display = (
        'command',
        'source',
        'result',
        'output',
        'time',
        'token',
    )
    list_filter = ('result', 'source', 'command__group', 'command')


@admin.register(models.AccessToken)
class AccessToken(admin.ModelAdmin):

    date_hierarchy = 'created_at'
    list_display = (
        'user',
        'token',
        'created_at',
        'expired_at',
        'is_active',
    )
    list_filter = ('user', 'user__groups')
    actions = ('disable_tokens', )

    def is_active(self, obj):
        return obj.is_active()

    # pylint:disable=unused-argument
    def disable_tokens(self, request, queryset):
        queryset.update(is_disabled=True)

    disable_tokens.short_description = 'Disable tokens'
