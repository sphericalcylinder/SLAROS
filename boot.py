import os, sys, time
import pygame
import keyprocessor, commandprocessor, loadanim

SCREEN_DIM = WIDTH, HEIGHT = (1000, 675)
screen = pygame.display.set_mode(SCREEN_DIM)
pygame.event.set_allowed(
    [pygame.QUIT, pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP])

loadanim.loadanimation(screen, SCREEN_DIM)

titlefont = pygame.font.SysFont('Copperplate', 30)
title = titlefont.render("S. L. A. R. O. S.", True, (0, 0, 0))
subtitlefont = pygame.font.SysFont('Andale Mono', 20)

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
                    goup = True
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
    sentence = subtitlefont.render(f">>> {''.join(keylist)}", True, (0, 0, 0))
    screen.blit(sentence, (20, 630))

    if waslen != currlen:
        goup = True
        waslen = currlen
    for x in sentencelist:
        if goup:
                x[1][1] -= 25
        c = subtitlefont.render(f'>>> {"".join(x[0])}', True, (0, 0, 0))
        screen.blit(c, x[1])
    goup = False

    screen.blit(title, (10, 10))

    pygame.display.update()
