# Django 2.0+ project template

Boilerplate template to start a Django project.

It's using the template feature of [the startproject command](https://docs.djangoproject.com/en/2.0/ref/django-admin/#startproject).
It makes a fair amount of assumptions that match my personal taste, so it may not be suitable for everybody.


## Getting started

    $ mkvirtualenv -p python3 <project_name>
    $ workon <project_name>
    $ pip install Django
    $ django-admin startproject \
          --template=https://github.com/zacbri/django-project-template/archive/master.zip \
          --extension=py,md,env,cfg \
          --name=.gitignore,Makefile \
          <project_name>
    $ cd <project_name>
    $ mv example.env .env
    $ pip install -e .[dev,test]

Once the project is created, the following will kickstart your dev environment:

    $ docker-compose up -d
    $ make load_dev_data
    $ <project_name> django runserver_plus

Two users are created by default:

- Superuser: **admin@example.com / admin**
- Unprivileged user: **admin@example.com / user**

## Environment variables

These are common between environments. The `ENVIRONMENT` variable loads the correct settings, possible values are: `dev`, `test` `staging`, `production` or whatever other settings class you add to <project_name>/settings.

    ENVIRONMENT='dev'
    DJANGO_SECRET_KEY='super-secret-key'
    DJANGO_DEBUG='yes'
    DJANGO_LANGUAGE_CODE='en-us'
    DJANGO_TIMEZONE='UTC'

These settings(and their default values) are only used on staging and production environments.

    DJANGO_SESSION_COOKIE_SECURE='yes'
    DJANGO_SECURE_BROWSER_XSS_FILTER='yes'
    DJANGO_SECURE_CONTENT_TYPE_NOSNIFF='yes'
    DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS='yes'
    DJANGO_SECURE_HSTS_SECONDS=31536000
    DJANGO_SECURE_REDIRECT_EXEMPT=''
    DJANGO_SECURE_SSL_HOST=''
    DJANGO_SECURE_SSL_REDIRECT='yes'
    DJANGO_SECURE_PROXY_SSL_HEADER='HTTP_X_FORWARDED_PROTO,https'

## Highlights

### Django

- Django 2.0+
- Django applications are in a clean *apps/*
- Put all cross-app resources in core/ (site-wide templates, assets, shared code...)
- Development, Tests, Staging and Production settings with [django-configurations](https://django-configurations.readthedocs.org)
- Get value insight and debug information while on Development with [django-debug-toolbar](https://django-debug-toolbar.readthedocs.org).
- Collection of custom extensions with [django-extensions](http://django-extensions.readthedocs.org).
- HTTPS and other security related settings on Staging and Production.
- Static files serving with [whitenoise](http://whitenoise.evans.io/en/stable/django.html)
- Custom command runner using [Click](http://click.pocoo.org)
- PostgreSQL database support with psycopg2.
- Clear separation of runtime media files in var/
- Boilerplate *Users* Django app using the user's email address as identifier

### Other

- Python packaging-ready (*setup.py*)
- Makefile for common development tasks
- Docker Compose file for dev environment, PostgreSQL included by default
- Sensible *.gitignore*

## Creating a new app

This requires a little more work than with the default Django layout:

    $ mkdir src/{{project_name}}/apps/<app_name>
    $ ./manage.py startapp <app_name> src/{{project_name}}/apps/<app_name>

And add `<project_name>.apps.<app_name>` to the `INSTALLED_APPS` setting.

## Custom runner and Django management commands

The custom runner is available as a command that takes the name of the project.
To get a list of available subcommands, run `<project_name> help`.

By default, it provides access to all the Django management commands:

    # List available commands (equivalent to running ./manage.py)
    $ <project_name> django

    # Migrate the database
    $ <project_name> django migrate

    #... and so on ...

## Credits

This template is inspired by the ones from [jpadilla](https://github.com/jpadilla/django-project-template) and [JocelynDelalande](https://github.com/JocelynDelalande/django-project-template).
These are les opinionated, have a look if you're looking for something more generic.

__________
*Boilerplate readme for project below...*
__________

# {{project_name}}

## Loading development data

Development data (users, ...) can be loaded into the database using simple commands:

    # Load
    $ make load_dev_data

    # Clear
    $ make clear_dev_data

    # Reset (clear then load)
    $ make reset_dev_data

This creates 2 users with the following credentials:

- Superuser: **admin@example.com / admin**
- Unprivileged user: **admin@example.com / user**

## Writing and running tests

Tests are run using [pytest](https://docs.pytest.org).
They should be placed in the *tests/{{project_name}}* directory, probably organized by Django app.

To run the tests, the best way is to use the Makefile targets:

    # Run flake8 linting
    $ make lint

    # Run python tests
    $ make test-python

    # Run both linting and tests
    $ make test

    # Check tests coverage
    $ make coverage

Alternatively, tests can be run via a Django command (`{{project_name}} django test`) or directly with pytest.
