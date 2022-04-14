import os, sys, time

# Hide pygame welcome prompt
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'

# Try to import pygame
try:
    import pygame
except: #install if it's not
    os.system("pip3 install pygame -q")
    import pygame
import keyprocessor, commandprocessor, loadanim, wordlist, linewrap

#Get the directory that we're in
os.environ['SLAROSDIR'] = os.getcwd()

# Function to make direct paths easier
def mfn(filename):
    """Makes a proper path to a file in the directory this is in"""
    return f"{os.environ['SLAROSDIR']}/{filename}"

# Setup window
SCREEN_DIM = WIDTH, HEIGHT = (1000, 675)
screen = pygame.display.set_mode(SCREEN_DIM)
pygame.display.set_caption("S.L.A.R.O.S.", "SLAROS")
pygame.font.init()
pygame.event.set_allowed(
    [pygame.QUIT, pygame.KEYDOWN])

# Display loading animation
#loadanim.loadanimation(screen, SCREEN_DIM)

# Prepare fonts
titlefont = pygame.font.Font(mfn('copperplate.ttf'), 20)
title = titlefont.render("S. L. A. R. O. S.", True, (0, 0, 0))
subtitlefont = pygame.font.Font(mfn('andalemono.ttf'), 12)

# Set some variables for the while loop
keylist = []
sentencelist = []
goup = False
shift = False

while True:
    # Fill screen with white
    screen.fill((255, 255, 255))
    currentkey = ''
    waslen = len(sentencelist)
    result = None

    # Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LSHIFT and not shift:
                shift = True
            elif event.key == pygame.K_LSHIFT and shift:
                shift = False
            # Get the key pressed as a string
            currentkey = keyprocessor.getkey(event.key, shift)
            if currentkey == 'return':
                stringkeylist = ''.join(keylist)
                # Check if it's a registered command
                result = commandprocessor.match_command(stringkeylist)
                if result == None:
                    # If not, display invalid
                    sentencelist.append(wordlist.Sentence(stringkeylist, 600, True))
                    sentencelist.append(wordlist.Sentence('Invalid', 625, False))
                else:
                    # Clear the screen
                    if result == 'clear':
                        sentencelist = []
                    # Line wrapping
                    linewrap.wrap(sentencelist, stringkeylist, result)
                    #sentencelist.append(wordlist.Sentence(stringkeylist, 600, True))
                    #sentencelist.append(wordlist.Sentence(result, 625, False))
                    #if len(result) <= 135:
                    #    sentencelist.append(wordlist.Sentence(stringkeylist, 600, True))
                    #    sentencelist.append(wordlist.Sentence(result, 625, False))
                    #else:
                    #    sentencelist.append(wordlist.Sentence(stringkeylist, 575, True))
                    #    result1 = result[:135]
                    #    result2 = result[135:]
                    #    sentencelist.append(wordlist.Sentence(result1, 600, False))
                    #    sentencelist.append(wordlist.Sentence(result2, 625, False))
                keylist = []
            elif currentkey == 'backspace':
                # Do fancy backspace stuff
                keylist.reverse()
                try:
                    keylist.remove(keylist[0])
                except:
                    pass
                keylist.reverse()
            else:
                keylist.append(currentkey)
    currlen = len(sentencelist)


    sentence = subtitlefont.render(f"JSH $ {''.join(keylist)}", True, (0, 0, 0))
    screen.blit(sentence, (20, 630))

    # Check if there's a new line
    if waslen != currlen:
        diff = currlen - waslen
        goup = True
    for x in sentencelist:
        # Delete lines that are off the screen
        if x.y < 0:
            sentencelist.remove(x)
        # Move the other ones up
        if goup:
            x.updatey(diff)
        sentence = x.loadsentence()
        screen.blit(sentence[0], sentence[1])
    goup = False

    screen.blit(title, (10, 10))

    pygame.display.update()
