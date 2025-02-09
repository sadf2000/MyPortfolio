import pygame,random
pygame.init()
scr = pygame.display.set_mode([800,600])
pygame.display.set_caption('Пэйнт')


mousedown = False
keep_going = True
#color = (255,150,0)
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

          if mousedown:
               spot = pygame.mouse.get_pos()
               pygame.draw.circle(scr,(random.randint(0,255),random.randint(0,255)
                                       ,random.randint(0,255)),spot,radius)
     pygame.display.update()

pygame.quit()
               
