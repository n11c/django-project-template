#!/usr/bin/env python3
import os

from setuptools import setup
from setuptools import find_packages

base_dir = os.path.dirname(__file__)

about = {}
with open(os.path.join(
        base_dir, 'src', '{{project_name}}', '__about__.py')) as f:
    exec(f.read(), about)


with open(os.path.join(base_dir, 'README.md')) as f:
    long_description = f.read()

dependency_links = []


requires = [
    'click==6.7',
    'Django>=2.0',
    'dj-database-url==0.4.2',
    'django-configurations==2.0',
    'django-extensions==1.9.9',
    'whitenoise==3.3.1',
    'psycopg2==2.7.3.2',
]


setup(
    name=about['__title__'],
    version=about['__version__'],
    package_dir={'': 'src'},
    packages=find_packages('src'),
    long_description=long_description,
    include_package_data=True,
    description=about['__summary__'],
    author=about['__author__'],
    author_email=about['__email__'],
    url=about['__uri__'],
    install_requires=requires,
    dependency_links=dependency_links,
    license=about['__license__'],
    entry_points={
        'console_scripts': [
            '{{project_name}} = {{project_name}}.runner:main']
    },
    extras_require={
        'dev': [
            'Werkzeug==0.14.1',
            'django-debug-toolbar==1.9.1',
            'docker-compose==1.18.0',
            'bumpversion==0.5.3',
        ],
        'test': [
            'flake8==3.5.0',
            'pytest==3.4.0',
            'pytest-django==3.1.2',
            'pytest-cov==2.5.1',
            'factory-boy==2.10.0',
            'Faker==0.8.10',
        ]
    },
    classifiers=[
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ]
)
