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
