# Django 2.0+ project template

Simple boilerplate template to start a Django project, replacing the default one (which is IMHO confusing).

It's using the template feature of [the startproject command](https://docs.djangoproject.com/en/2.0/ref/django-admin/#startproject).
It makes the least amount of assumptions possible while still trying provide a useful setup.


## Getting started

    $ django-admin startproject \
          --template=https://github.com/zacbri/django-project-template/archive/master.zip \
          --extension=py,md,env,.gitignore \
          <project_name>
    $ mv example.env .env
    $ pip install -r requirements/dev.txt

## Environment variables

These are common between environments. The `ENVIRONMENT` variable loads the correct settings, possible values are: `DEV`, `STAGING`, `PRODUCTION`.

    ENVIRONMENT='DEV'
    DJANGO_SECRET_KEY='super-secret-key'
    DJANGO_DEBUG='yes'

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

- Django 2.0+
- Django applicationrs are in a clean *apps/*
- Development, Staging and Production settings with [django-configurations](https://django-configurations.readthedocs.org)
- Get value insight and debug information while on Development with [django-debug-toolbar](https://django-debug-toolbar.readthedocs.org).
- Collection of custom extensions with [django-extensions](http://django-extensions.readthedocs.org).
- HTTPS and other security related settings on Staging and Production.
- Static files serving with [whitenoise](http://whitenoise.evans.io/en/stable/django.html)
- Clear separation of runtime media files in var/
- Put all cross-app resources in core/ (site-wide templates, assets, shared code...)
- Separated dev/prod requirements
- Sensible *.gitignore*
- Boilerplate *Users* Django app pre-included

## Creating a new app

Sadly, a bit more complicated than with vanilla template :

    $ mkdir {{ project_name }}/apps/<app_name>
    $ ./manage.py startapp <app_name> {{ project_name }}/apps/<app_name>

And add `{{ project_name }}.apps.<app_name>` to your `INSTALLED_APPS`.
