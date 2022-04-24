import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import linewrap

def sprint(string: str, newline: bool = False):

    from boot import sentencelist, stringkeylist, colors
    
    if not newline:
        linewrap.wrap(sentencelist, stringkeylist, string, colors)
    if newline:
        newlines = len(input)//135
        diff = 135*newlines - len(string)
        string + (' '*diff)
        linewrap.wrap(sentencelist, stringkeylist, string, colors)
