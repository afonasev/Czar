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
    actions = ['run_command']

    # pylint:disable=unused-argument
    def run_command(self, request, queryset):
        for command in queryset:
            command.run(source=models.Call.ADMIN)
    run_command.short_description = 'Run'


@admin.register(models.Call)
class Call(admin.ModelAdmin):

    date_hierarchy = 'time'
    list_display = (
        'command',
        'source',
        'result',
        'output',
        'time',
    )
    list_filter = ('result', 'source', 'command__group', 'command')
