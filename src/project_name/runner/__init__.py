import os

import click
from django.utils.module_loading import import_string

import {{project_name}}


@click.group()
@click.option(
    '--environment',
    default='',
    envvar='ENVIRONMENT',
    help='Override environment (settings).',
    metavar='ENV')
@click.version_option(version={{project_name}}.__version__)
@click.pass_context
def cli(ctx, environment):
    """{{project_name}} is something.
    """
    # Elevate --environment option to ENVIRONMENT env var
    if environment:
        os.environ['ENVIRONMENT'] = environment

    configuration = os.getenv('ENVIRONMENT', 'dev').title()
    os.environ.setdefault(
        'DJANGO_SETTINGS_MODULE', '{{project_name}}.settings')
    os.environ.setdefault('DJANGO_CONFIGURATION', configuration)


"""
    Add your runner commands here
"""
list(map(lambda cmd: cli.add_command(import_string(cmd)), (
    '{{project_name}}.runner.commands.help.help',
    '{{project_name}}.runner.commands.django.django',
)))


def make_django_command(name, django_command=None, help=None):
    "A wrapper to convert a Django subcommand a Click command"
    if django_command is None:
        django_command = name

    @click.command(
        name=name,
        help=help,
        add_help_option=False,
        context_settings=dict(
            ignore_unknown_options=True,
        ))
    @click.argument('management_args', nargs=-1, type=click.UNPROCESSED)
    @click.pass_context
    def inner(ctx, management_args):
        from {{project_name}}.runner.commands.django import django
        ctx.params['management_args'] = (django_command,) + management_args
        ctx.forward(django)

    return inner


def main():
    cli(obj={}, max_content_width=100)
