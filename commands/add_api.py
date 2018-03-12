from util import CommandInvocationError, CommandExecutionError

USAGE = "add_api [args...]"

ABOUT = """Create an API which does not exist yet (e.g. for bootstrapping).
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
        raise CommandInvocationError('missing command: add_api [args...]')
    print("YAAY")
