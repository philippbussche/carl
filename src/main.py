import sys

from util import keys, CommandInvocationError, CommandExecutionError, \
                    parse_options, HELP_OPTIONS
from commands import add_api, update_api, deploy_api, delete_api

COMMANDS = {'add_api': add_api,
            'deploy_api': deploy_api,
            'update_api': update_api,
            'delete_api': delete_api
            }

COMMANDS_ORDER = ('add_api', 'update_api', 'deploy_api', 'delete_api')

HELP_TEMPLATE = """\
USAGE
    ./carl {usage}

ABOUT
    {about}"""

USAGE = """\
USAGE
    carl <command> <args...>

ABOUT
    Kong management utility

COMMANDS
    help                Print this message
    help <command>      Show detailed help for the given carl command
"""


def main():
    if len(sys.argv) < 2:
        print_usage()

    command = sys.argv[1]
    args = sys.argv[2:]

    if command in HELP_OPTIONS or command == 'help':
        if args:
            print_usage(command=args[0])
        else:
            print_usage()

    if command not in COMMANDS:
        print_usage(error="%s: unrecognized command" % command)

    mod = COMMANDS[command]

    try:
        options, args = parse_options(getattr(mod, 'OPTIONS', {}), args)

        if 'help' in options:
            print_usage(command=command)

        mod.command(options, args)
    except CommandInvocationError as exc:
        print_usage(command=command, error=str(exc))
    except CommandExecutionError as exc:
        print(str(exc))


def indent(text, spaces=4):
    indentation = (' ' * spaces)
    indented_text = ('\n%s' % indentation).join(text.split('\n'))
    return indented_text


def print_usage(command=None, error=None):
    if command and command not in COMMANDS:
        error = '%s: unrecognized command' % command
        command = None

    if command:
        mod = COMMANDS[command]
        about = indent(mod.ABOUT)

        print(HELP_TEMPLATE.format(usage=mod.USAGE, about=about))

        if getattr(mod, 'OPTIONS', None):
            print('OPTIONS')
            for opt in sorted(keys(mod.OPTIONS)):
                opt_descr = mod.OPTIONS[opt]
                if isinstance(opt_descr, dict):
                    if 'short' in opt_descr:
                        opt = '%s / -%s' % (opt, opt_descr['short'])
                    if opt_descr.get('value', False):
                        opt += ' %s' % \
                            (opt_descr.get('value_help', ' <value>'))

                    opt_help = opt_descr.get('help', False)

                    if opt_help is False:
                        continue

                    if opt_descr.get('required', False):
                        opt_help = 'REQUIRED: %s' % opt_help
                else:
                    opt_help = opt_descr

                print('    --%-28s  %s' % (opt, opt_help))
    else:
        print(USAGE)

        for cmd in COMMANDS_ORDER:
            # print(cmd)
            mod = COMMANDS[cmd]
            first_line = mod.ABOUT.splitlines()[0]
            print("    %-18s  %s" % (cmd, first_line))

    if error:
        prefix = "./carl {command}".format(command=command) if command else './carl'
        print('')
        print("ERROR: {prefix}: {error}".format(prefix=prefix, error=error))

    sys.exit(1 if error else 0)


if __name__ == '__main__':
    main()
