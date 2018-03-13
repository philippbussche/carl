from util import CommandInvocationError, CommandExecutionError
from commands.functions import create_api

USAGE = "update_api [args...]"

ABOUT = """Updates an API. Creates the API if it does not exist yet (e.g. for cd).
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
        raise CommandInvocationError('missing command: update_api [args...]')
    print("YAAY")
