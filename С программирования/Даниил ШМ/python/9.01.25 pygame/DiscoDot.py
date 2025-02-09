import pygame,random
pygame.init()
screen = pygame.display.set_mode([800,600])
FixedUpdate = True

colors = [0]*100
locations = [0]*100
sizes = [0]*100

new_x = 0
new_y = 0

for n in range(100):
     colors[n] = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
     sizes[n] = random.randint(10,100)
     locations[n] = (random.randint(0,800),random.randint(0,600))
     
while FixedUpdate:
     
     for n in range(100):
          
     
          pygame.draw.circle(screen, colors[n] ,locations[n] , sizes[n])


     locations[n] = (new_x,new_y)

     new_x = locations[n][0] + 1
     new_y = locations[n][1] + 1
     
     if new_x > 800:
          new_x -= 800
     if new_y > 600:
          new_y -= 600
     
     
     pygame.display.update()
     
     for key in pygame.event.get():
          if key.type == pygame.QUIT:
               FixedUpdate = False


pygame.quit()
