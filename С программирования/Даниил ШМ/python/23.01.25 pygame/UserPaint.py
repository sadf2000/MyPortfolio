import pygame,random
pygame.init()
scr = pygame.display.set_mode([800,600])
#scr = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption('Пэйнт')


mousedown = False
keep_going = True
color = (255,0,0)
mov = (0,15)
radius = 10

while keep_going:
     for event in pygame.event.get():
          if event.type == pygame.QUIT:
               keep_going = False
          if event.type == pygame.MOUSEBUTTONDOWN:
               mousedown = True
          if event.type == pygame.MOUSEBUTTONUP:
               mousedown = False
          if event.type == pygame.KEYDOWN: 
               if event.key == pygame.K_r:
                    color = (255,0,0)
               if event.key == pygame.K_g:
                    color = (0,255,0)
               if event.key == pygame.K_b:
                    color = (0,0,255)
               if event.key == pygame.K_c:
                    scr.fill((0, 0, 0))
          if mousedown:
               spot = pygame.mouse.get_pos()
               pygame.draw.circle(scr,color,spot,radius)
     pygame.display.update()

pygame.quit()
               
