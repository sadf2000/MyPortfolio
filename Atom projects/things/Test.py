import pygame

pygame.init()
scr = pygame.display.set_mode([800,600])
Update = True
while Update:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Update = False
