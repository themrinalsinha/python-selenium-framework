def terminal_output(command):
    from subprocess import check_output
    command = command.split(' ')
    return check_output(command).decode('utf-8').strip()

from .automator import Automator
