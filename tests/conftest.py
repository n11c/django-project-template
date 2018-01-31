import os
import configurations


def pytest_configure(config):
    os.environ['DJANGO_CONFIGURATION'] = 'Test'
    os.environ['DJANGO_SETTINGS_MODULE'] = '{{project_name}}.settings'
    configurations.setup()


def pytest_runtest_teardown(item):
    pass
