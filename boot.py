import pygame, sys, time
import loadanim, startanim, keyprocessor

SCREEN_DIM = WIDTH, HEIGHT = (1000, 675)
screen = pygame.display.set_mode(SCREEN_DIM)
pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP])

loadanim.loadanimation(screen, SCREEN_DIM)

titlefont = pygame.font.SysFont('Copperplate', 30)
title = titlefont.render("S. L. A. R. O. S.", True, (0, 0, 0))
subtitlefont = pygame.font.SysFont('Andale Mono', 38)

startanim.startanimation(screen, SCREEN_DIM)
keylist = []

while True:
    screen.fill((255, 255, 255))
    currentkey = None

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:
            currentkey = keyprocessor.getkey(event.key)
            if currentkey == 'return':
                keylist = []
            else:
                keylist.append(currentkey)

    screen.blit(title, (10, 10))
    sentence = subtitlefont.render(''.join(keylist), True, (0, 0, 0))
    screen.blit(sentence, (20, 630))


    pygame.display.update()    