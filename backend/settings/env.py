import os

PRODUCTION = os.environ.get('PRODUCTION', False)
DEBUG = not PRODUCTION
