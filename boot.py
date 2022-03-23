import os, sys, time
import pygame
import keyprocessor, commandprocessor, loadanim

SCREEN_DIM = WIDTH, HEIGHT = (1000, 675)
screen = pygame.display.set_mode(SCREEN_DIM)
pygame.font.init()
pygame.event.set_allowed(
    [pygame.QUIT, pygame.KEYDOWN])

loadanim.loadanimation(screen, SCREEN_DIM)

titlefont = pygame.font.Font('assets/copperplate.ttf', 20)
title = titlefont.render("S. L. A. R. O. S.", True, (0, 0, 0))
subtitlefont = pygame.font.Font('assets/andalemono.ttf', 12)

keylist = []
sentencelist = []
sentencey = 620
goup = False
shift = False


while True:
    screen.fill((255, 255, 255))
    currentkey = ''
    waslen = len(sentencelist)
    result = None
    respsent = False

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
                sentencelist.append([stringkeylist, [20, 620]])
                result = commandprocessor.match_command(stringkeylist)
                if result is not None:
                    respsent = True
                keylist = []
            elif currentkey == 'backspace':
                keylist.reverse()
                keylist.remove(keylist[0])
                keylist.reverse()
            else:
                keylist.append(currentkey)
    currlen = len(sentencelist)

    if result is not None:
        sentencelist.append([result, [20, 620]])
    sentence = subtitlefont.render(f"JSH $ {''.join(keylist)}", True, (0, 0, 0))
    screen.blit(sentence, (20, 630))

    if waslen != currlen:
        goup = True
        waslen = currlen
    for x in sentencelist:
        if goup:
            if respsent:
                x[1][1] -= 50
                respsent = False
            else:
                x[1][1] -= 25
        c = subtitlefont.render(f'JSH $ {"".join(x[0])}', True, (0, 0, 0))
        screen.blit(c, x[1])
    goup = False

    screen.blit(title, (10, 10))

    pygame.display.update()
