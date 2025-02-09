import pygame as p
p.init()
screen = p.display.set_mode([800,600])
FixedUpdate = True
pic = p.image.load('smile.bmp')

picx =0
picy =0

speedx =5
speedy = 5

timer = p.time.Clock()
while FixedUpdate:
     
     picx += speedx
     picy += speedy
     
     if picx <= 0 or picx +pic.get_width() >= 800:
          speedx = -speedx

     if picy <= 0 or picy +pic.get_height() >= 600:
          speedy = -speedy

     screen.blit(pic, (picx,picy))

     timer.tick(60)
     p.display.update()
     screen.fill((0,0,0))
     
     for key in p.event.get():
          if key.type == p.QUIT:
               FixedUpdate = False







p.quit()
     
