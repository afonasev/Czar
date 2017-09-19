from split_settings.tools import include

include(
    # Load environment settings
    'env.py',

    # Here we should have the order because of dependencies
    'paths.py',
    'apps.py',
    'middleware.py',

    # Load all other settings
    '*.py',
)
