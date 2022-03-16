import sys, os

def match_command(command):
    match command:
        case 'ls':
            return os.getcwd()
        case 'exit':
            sys.exit(0)
        case 'fexit':
            sys.exit('Forced Exit')
        case _:
            if command[0:3] == 'cpa':
                os.chdir(command[3:])
            else:
                return None