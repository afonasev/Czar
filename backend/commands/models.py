import functools
import subprocess

from django.db import models

SUCCESS = 'success'
FAIL = 'fail'


def log_calls(func):

    @functools.wraps(func)
    def wrapped(command):
        result = func(command)

        if SUCCESS in result:
            result_status = Call.SUCCESS_RESULT
            output = result[SUCCESS]
        else:
            result_status = Call.FAIL_RESULT
            output = result[FAIL]

        Call(command=command, result=result_status, output=output).save()

        return result

    return wrapped


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

    @log_calls
    def run(self):
        try:
            output = subprocess.check_output(self.body, shell=True).decode()
            return {SUCCESS: output}
        except subprocess.CalledProcessError as exc:
            return {FAIL: str(exc)}

    def __str__(self):
        return f'{self.group.title} - {self.title}'

    class Meta:
        unique_together = ('group', 'title')


class Call(models.Model):

    SUCCESS_RESULT = 1
    FAIL_RESULT = 2

    RESULTS = (
        (SUCCESS_RESULT, SUCCESS),
        (FAIL_RESULT, FAIL),
    )

    command = models.ForeignKey(Command, related_name='calls')
    result = models.IntegerField(choices=RESULTS)
    output = models.TextField(blank=True)
    time = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return f'{self.command} - {self.time}'
