from util import CommandInvocationError, CommandExecutionError
from commands.functions import delete_apis

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
     'all': {
          'short': 'a',
          'help': 'Delete all the APIs configured.',
          'value': False,
          'value_help': '',
          'required': False
     },
     'client_ssl': {
          'short': 'client_ssl',
          'help': 'True or false indicating if client ssl mutual auth should be used.',
          'value': True,
          'value_help': '',
          'required': False
     },
     'cert': {
          'short': 'cert',
          'help': 'If client_ssl is true then this has to reference absolute path to cert file.',
          'value': True,
          'value_help': '',
          'required': False
     },
     'key': {
          'short': 'key',
          'help': 'If client_ssl is true then this has to reference absolute path to key file.',
          'value': True,
          'value_help': '',
          'required': False
     },
}


def command(options, args):
    if not options:
        raise CommandInvocationError('missing command: delete_api [args...]')
    delete_apis(**options)
