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
            if command[:2] == 'cd':
                try:
                    os.chdir(command[3:])
                    return f'Directory now {os.getcwd()}'
                except:
                    return None
            elif command[:4] == 'echo':
                return command[5:]
            elif command[:3] == 'run':
                filename: str = command[4:]
                if filename.endswith('_slars.py'):
                    return command
                else:
                    return None
            else:
                return None