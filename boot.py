import os, sys, time

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'

try:
    import pygame
except:
    os.system("pip3 install pygame -q")
    import pygame
import keyprocessor, commandprocessor, loadanim, wordlist

os.environ['SLAROSDIR'] = os.getcwd()

def mfn(filename):
    """Makes a proper path to a file in the directory this is in"""
    return f"{os.environ['SLAROSDIR']}/{filename}"


SCREEN_DIM = WIDTH, HEIGHT = (1000, 675)
screen = pygame.display.set_mode(SCREEN_DIM)
pygame.display.set_caption("S.L.A.R.O.S.", "SLAROS")
pygame.font.init()
pygame.event.set_allowed(
    [pygame.QUIT, pygame.KEYDOWN])

loadanim.loadanimation(screen, SCREEN_DIM)

titlefont = pygame.font.Font(mfn('copperplate.ttf'), 20)
title = titlefont.render("S. L. A. R. O. S.", True, (0, 0, 0))
subtitlefont = pygame.font.Font(mfn('andalemono.ttf'), 12)

keylist = []
sentencelist = []
goup = False
shift = False
vdir = os.getcwd()

while True:
    screen.fill((255, 255, 255))
    currentkey = ''
    waslen = len(sentencelist)
    result = None

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LSHIFT and not shift:
                shift = True
            elif event.key == pygame.K_LSHIFT and shift:
                shift = False
            currentkey = keyprocessor.getkey(event.key, shift)
            if currentkey == 'return':
                stringkeylist = ''.join(keylist)
                result = commandprocessor.match_command(stringkeylist)
                if result is None:
                    sentencelist.append(wordlist.Sentence(stringkeylist, 600, True))
                    sentencelist.append(wordlist.Sentence('Invalid', 625, False))
                else:
                    if result == 'clear':
                        sentencelist = []
                    else:
                        sentencelist.append(wordlist.Sentence(stringkeylist, 600, True))
                        sentencelist.append(wordlist.Sentence(result, 625, False))
                keylist = []
            elif currentkey == 'backspace':
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

    if waslen != currlen:
        diff = currlen - waslen
        goup = True
    for x in sentencelist:
        if goup:
            x.updatey(diff)
        sentence = x.loadsentence()
        screen.blit(sentence[0], sentence[1])
    goup = False

    screen.blit(title, (10, 10))

    pygame.display.update()
