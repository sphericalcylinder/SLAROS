import sys, os

def match_command(command):
    match command:
        case 'pwd':
            return os.getcwd()
        case 'ls':
            return os.listdir(os.getcwd())
        case 'exit':
            sys.exit(0)
        case 'fexit':
            sys.exit('Forced Exit')
        case _:
            if command[0:3] == 'cpa':
                os.chdir(command[4:])
            else:
                return None