#!/usr/bin/env bash
python manage.py migrate
python manage.py collectstatic --noinput -v0
gunicorn -w 5 -b 0.0.0.0:8000 backend.wsgi &
tail -f logs/errors.log
