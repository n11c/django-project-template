from os.path import join
from .base import BaseSettings
from configurations import values


class Dev(BaseSettings):

    # .env file used to set environment variables locally during development
    DOTENV = join(BaseSettings.ROOT_DIR, '.env')

    SECRET_KEY = values.SecretValue()

    DEBUG = values.BooleanValue(True)

    DATABASES = values.DatabaseURLValue('postgresql://dev:dev@localhost:15432/dev')

    INTERNAL_IPS = [
        '127.0.0.1'
    ]

    INSTALLED_APPS = BaseSettings.INSTALLED_APPS + [
        'debug_toolbar',
    ]

    MIDDLEWARE = BaseSettings.MIDDLEWARE + [
        'debug_toolbar.middleware.DebugToolbarMiddleware'
    ]
