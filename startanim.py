import pygame, time
pygame.font.init()

def startanimation(screen, screen_dimentions: tuple):

    for i in range(100, 30, -1):
        screen.fill((0, 0, 0))
        titlefont = pygame.font.SysFont('Copperplate', i)
        title = titlefont.render("S. L. A. R. O. S.", True, (255, 255, 255))
        screen.blit(title, (150, 50))
        pygame.display.update()
        for event in pygame.event.get():
            pass
        time.sleep(0.01)
    

    for g in range(150, 10, -1):
        screen.fill((0, 0, 0))
        screen.blit(title, (g, 50))
        pygame.display.update()
        for event in pygame.event.get():
            pass
        time.sleep(0.01)

    for j in range(50, 10, -1):
        screen.fill((0, 0, 0))
        screen.blit(title, (10, j))
        pygame.display.update()
        for event in pygame.event.get():
            pass
        time.sleep(0.01)
    