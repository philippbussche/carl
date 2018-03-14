from util import CommandInvocationError, CommandExecutionError
from commands.functions import update_api

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
     'uri': {
          'short': 'u',
          'help': 'Specify the URI pattern for this API',
          'value': True,
          'value_help': '',
          'required': True
     },
     'upstream_url': {
          'short': 'up',
          'help': 'Specify the upstream url to be used for this API',
          'value': True,
          'value_help': '',
          'required': True
     },
     'strip_uri': {
          'short': 'strip',
          'help': 'True or false indicating if uri called should be stripped before handing to upstream',
          'value': True,
          'value_help': '',
          'required': True
     },
     'host': {
          'short': 'h',
          'help': 'Host name expected to be used for reaching this API via.',
          'value': True,
          'value_help': '',
          'required': True
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
        raise CommandInvocationError('missing command: update_api [args...]')
    update_api(**options)
