import pygame,random
pygame.init()
screen = pygame.display.set_mode([800,600])
FixedUpdate = True


while FixedUpdate:
     pygame.draw.circle(screen, (random.randint(0,255),random.randint(0,255),random.randint(0,255)), (400,300), 50)
     
     pygame.display.update()

     


     
     for key in pygame.event.get():
          if key.type == pygame.QUIT:
               FixedUpdate = False


pygame.quit()
