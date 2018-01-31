import os
import click


@click.command(
    add_help_option=False, context_settings=dict(ignore_unknown_options=True))
@click.argument('management_args', nargs=-1, type=click.UNPROCESSED)
@click.pass_context
def django(ctx, management_args):
    "Execute Django subcommands."
    if len(management_args) and management_args[0] == 'test':
        if '--environment' not in management_args:
            os.environ['DJANGO_CONFIGURATION'] = 'Test'

    try:
        from configurations.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            'Couldn\'t import Django-configurations. Are you sure it\'s'
            'installed and available on your PYTHONPATH environment variable?'
            'Did you forget to activate a virtual environment?') from exc

    execute_from_command_line(argv=[ctx.command_path] + list(management_args))
