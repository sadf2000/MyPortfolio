import pygame,random
pygame.init()
scr = pygame.display.set_mode([800,600])
pygame.display.set_caption('Пэйнт')


mousedown = False
keep_going = True
#color = (255,0,0)
mov = (0,15)
radius = 10
'''if event.button == 1
                    mouseType = 1
               if event.button == 2
                    mouseType = 2
               if event.button == 3
                    mouseType = 3'''
while keep_going:
     for event in pygame.event.get():
          if event.type == pygame.QUIT:
               keep_going = False
               
          if event.type == pygame.MOUSEBUTTONDOWN:
               mousedown = True
               mouseType = event.button
               
          if event.type == pygame.MOUSEBUTTONUP:
               mousedown = False
               mouseType = 0
               
          if mousedown:
               spot = pygame.mouse.get_pos()
               if mouseType == 1:  # Левая кнопка
                    pygame.draw.circle(scr,(255,0,0),spot,radius)
               elif mouseType == 2:  # Правая кнопка
                    pygame.draw.circle(scr,(0,255,0),spot,radius)
               elif mouseType == 3:  # Правая кнопка
                    pygame.draw.circle(scr,(0,0,255),spot,radius)
     pygame.display.update()

pygame.quit()
               
