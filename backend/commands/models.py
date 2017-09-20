import subprocess

from django.db import models


class Group(models.Model):

    title = models.SlugField(unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Command(models.Model):

    group = models.ForeignKey(Group, related_name='commands')
    title = models.SlugField()
    description = models.TextField(blank=True)
    body = models.TextField()
    is_disabled = models.BooleanField(default=False)

    def run(self):
        return subprocess.check_output(self.body, shell=True).decode()

    def __str__(self):
        return f'{self.group.title} - {self.title}'

    class Meta:
        unique_together = ('group', 'title')
