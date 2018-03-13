from util import CommandInvocationError, CommandExecutionError

USAGE = "delete_api [args...]"

ABOUT = """Deletes an API.
"""

OPTIONS = {
     'server': {
          'short': 's',
          'help': 'Kong server name or IP (and port)',
          'value': True,
          'value_help': '',
          'required': True
     },
}


def command(options, args):
    if not options:
        raise CommandInvocationError('missing command: delete_api [args...]')
    print("YAAY")
