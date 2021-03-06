import pygame, time, os

pygame.font.init()
def loadanimation(screen, screen_dimensions: tuple):
    WIDTH = screen_dimensions[0]

    disks = []
    try:
        for i in range(1, 10):
            disks.append(pygame.image.load(os.environ['SLAROSDIR']+f'/diskimages/disk{i}.png'))
    except:
        disks = []
        for i in range(1, 10):
            disks.append(pygame.image.load(os.environ['SLAROSDIR']+f'/assets/diskimages/disk{i}.png'))

    titlefont = pygame.font.Font('copperplate.ttf', 75)
    subtitlefont = pygame.font.Font('andalemono.ttf', 38)
    subsubtitlefont = pygame.font.Font('andalemono.ttf', 20)
    jshfont = pygame.font.Font('times.ttf', 40)
    loading = subtitlefont.render("Loading, please wait", True, (255, 255, 255))
    doneloading = subtitlefont.render("Finished, booting...", True, (255, 255, 255))
    title = titlefont.render("S. L. A. R. O. S.", True, (255, 255, 255))
    desc = subsubtitlefont.render("Slow Loading And Running Operating System", True, (255, 255, 255))
    nowjsh = jshfont.render("with JSH", True, (255, 255, 255))


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
        screen.blit(nowjsh, (750, 155))
        if not doneload:
            screen.blit(loading, (260, 615))
        else:
            screen.blit(doneloading, (265, 615))

        pygame.display.update()
        count += 1
        
        time.sleep(waittime)
        if countdown == 0:
            break
            
    for i in range(75, 20, -1):
        screen.fill((0, 0, 0))
        titlefont = pygame.font.Font('copperplate.ttf', i)
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
        
