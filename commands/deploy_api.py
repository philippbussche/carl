from util import CommandInvocationError, CommandExecutionError

USAGE = "deploy_api [args...]"

ABOUT = """Deploys an API which results in a blue/green switch.
            If blue does not exist yet, it will be created as a copy of green.
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
        raise CommandInvocationError('missing command: deploy_api [args...]')
    print("YAAY")
