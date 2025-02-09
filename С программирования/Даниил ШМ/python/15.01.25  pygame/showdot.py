import pygame
pygame.init()
scr = pygame.display.set_mode([800,600])
pygame.display.set_caption('Пэйнт')


mousedown = False
keep_going = True
color = (255,255,0)
mov = (0,15)
radius = 5

while keep_going:
     for event in pygame.event.get():
          if event.type == pygame.QUIT:
               keep_going = False
          if event.type == pygame.MOUSEBUTTONDOWN:
               spot = event.pos
               pygame.draw.circle(scr,color,spot,radius)
     pygame.display.update()

pygame.quit()
               
