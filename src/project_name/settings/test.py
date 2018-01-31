import tempfile
from .base import BaseSettings
from configurations import values


class Test(BaseSettings):
    MEDIA_ROOT = tempfile.mkdtemp()
    SECRET_KEY = 'test'
    DATABASES = values.DatabaseURLValue('postgresql://dev:dev@localhost:15432/dev')
