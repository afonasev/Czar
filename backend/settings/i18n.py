import os

from .paths import PROJECT_DIR

LANGUAGE_CODE = 'en'

USE_I18N = True
USE_L10N = True

LOCALE_PATHS = (os.path.join(PROJECT_DIR, 'locale'),)
