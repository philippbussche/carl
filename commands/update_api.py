from util import CommandInvocationError, CommandExecutionError

USAGE = "update_api [args...]"

ABOUT = """Updates an API, creates it if it does not exist yet (e.g. for continous deployment).
"""

OPTIONS = {
     'server': {
          'short': 's',
          'help': 'Kong host name (and port)',
          'value': True,
          'value_help': '',
          'required': True
     },
}


def command(options, args):
    if not options:
        raise CommandInvocationError('missing command: update_api [args...]')
    print("YAAY")
