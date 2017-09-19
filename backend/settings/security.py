import os

from .env import DEBUG

# SECURITY WARNING: keep the secret key used in production secret!
if DEBUG:
    SECRET_KEY = 'secret_key'
else:
    SECRET_KEY = os.environ['SECRET_KEY']

if DEBUG:
    ALLOWED_HOSTS = []
else:
    ALLOWED_HOSTS = ['.afonasev.ru']

VALIDATORS_PATH = 'django.contrib.auth.password_validation.'

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': VALIDATORS_PATH + 'UserAttributeSimilarityValidator'},
    {'NAME': VALIDATORS_PATH + 'MinimumLengthValidator'},
    {'NAME': VALIDATORS_PATH + 'CommonPasswordValidator'},
    {'NAME': VALIDATORS_PATH + 'NumericPasswordValidator'}
]

X_FRAME_OPTIONS = 'DEN'
