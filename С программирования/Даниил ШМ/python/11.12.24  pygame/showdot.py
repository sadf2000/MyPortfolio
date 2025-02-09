import pygame
pygame.init()
screen = pygame.display.set_mode([800,600])

keep_going = True
g = (0,255,0)
r = 50
while keep_going:
     for event in pygame.event.get():
          if event.type== pygame.QUIT:
               keep_going = False
     pygame.draw.circle(screen,green,(100,100),r)
     pygame.display.update()
pygame.quit()
