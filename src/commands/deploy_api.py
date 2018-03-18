from util import CommandInvocationError, CommandExecutionError

USAGE = "deploy_api [args...]"

ABOUT = """Deploys an API, making it available e.g. through a specific Host name.
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
        raise CommandInvocationError('missing command: deploy_api [args...]')
    print("YAAY")
