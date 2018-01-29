from .base import BaseSettings
from configurations import values

class Dev(BaseSettings):

    DEBUG = values.BooleanValue(True)

    INTERNAL_IPS = [
        '127.0.0.1'
    ]

    INSTALLED_APPS = BaseSettings.INSTALLED_APPS + [
        'debug_toolbar',
    ]

    MIDDLEWARE = BaseSettings.MIDDLEWARE + [
        'debug_toolbar.middleware.DebugToolbarMiddleware'
    ]
