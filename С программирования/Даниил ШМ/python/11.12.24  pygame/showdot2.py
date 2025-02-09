import pygame
import random
import time
pygame.init()
screen = pygame.display.set_mode([800,600])

keep_going = True


while keep_going:
     for event in pygame.event.get():
          if event.type== pygame.QUIT:
               keep_going = False
     for i in range(1):
          green= (random.randint(0,255),random.randint(0,255),random.randint(0,255))
          r = random.randint(25,50)
          pygame.draw.circle(screen,green,(random.randint(100,1000),random.randint(100,1000)),r)
          time.sleep(0.1)
     pygame.display.update()
pygame.quit()
