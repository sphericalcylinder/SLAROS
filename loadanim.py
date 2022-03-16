import pygame, sys, time

pygame.font.init()
def loadanimation(screen, screen_dimensions: tuple):
    WIDTH = screen_dimensions[0]

    disks = []
    for i in range(1, 10):
        disks.append(pygame.image.load(f'assets/diskimages/disk{i}.png'))

    titlefont = pygame.font.SysFont('Copperplate', 100)
    subtitlefont = pygame.font.SysFont('Andale Mono', 38)
    subsubtitlefont = pygame.font.SysFont('Andale Mono', 20)
    loading = subtitlefont.render("Loading, please wait", True, (255, 255, 255))
    doneloading = subtitlefont.render("Finished, booting...", True, (255, 255, 255))
    title = titlefont.render("S. L. A. R. O. S.", True, (255, 255, 255))
    desc = subsubtitlefont.render("Slow Loading And Running Operating System", True, (255, 255, 255))


    count = 0
    waittime = 0.1
    countdown = 50
    doneload = False
    while True:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            pass

        if count <= 8:
            screen.blit(disks[count], ((WIDTH/2)-150, 300))
        else:
            count = 0
            screen.blit(disks[count], ((WIDTH/2)-150, 300))
            if waittime > 0.02:
                waittime -= 0.01
            elif waittime > 0.001:
                waittime -= 0.001
            else:
                countdown -= 1
                doneload = True
        screen.blit(title, (150, 50))
        screen.blit(desc, (250, 150))
        if not doneload:
            screen.blit(loading, (260, 615))
        else:
            screen.blit(doneloading, (265, 615))

        pygame.display.update()
        count += 1
        
        time.sleep(waittime)
        if countdown == 0:
            break
            
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
        
