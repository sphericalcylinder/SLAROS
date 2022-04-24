import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sprint import sprint
# sprint is SLAROSprint, abbreviated, not very fast running.
# Your SLARS file must end in _slars.py, or else it won't work

def run():
    print('hi')
    sprint('hi')