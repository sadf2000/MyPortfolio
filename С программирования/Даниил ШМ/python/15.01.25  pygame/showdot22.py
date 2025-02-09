import pygame
pygame.init()
scr = pygame.display.set_mode([800,600])
pygame.display.set_caption('Пэйнт')
pic = pygame.image.load('smile.bmp')

mousedown = False
keep_going = True
color = (255,150,0)
mov = (0,15)
radius = 5

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
               new_spot = (pic.get_width()/2+(pygame.mouse.get_pos()[0]-pic.get_width())
                           ,pic.get_height()/2+(pygame.mouse.get_pos()[1]-pic.get_height()))

               #pygame.draw.circle(scr,color,spot,radius)
               scr.blit(pic, new_spot)
     pygame.display.update()

pygame.quit()
               
