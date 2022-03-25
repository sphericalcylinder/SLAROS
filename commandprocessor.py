import sys, os

def match_command(command):
    match command:
        case 'pwd':
            return os.getcwd()
        case 'ls':
            return ', '.join(os.listdir(os.getcwd()))
        case 'clear':
            return 'clear'
        case 'exit':
            sys.exit(0)
        case _:
            if command[0:3] == 'cpa':
                os.chdir(command[4:])
            else:
                return None