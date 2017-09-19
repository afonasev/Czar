import os

from .env import PRODUCTION
from .paths import BASE_DIR, PROJECT_DIR

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = (
    os.path.join(PROJECT_DIR, "static"),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

if PRODUCTION:
    STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.' \
        'ManifestStaticFilesStorage'
