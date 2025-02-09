#randomspiralfunction.py
import turtle as t1
import random as r
t = t1.Pen()
t.speed(0)
t1.bgcolor('black')
colors  =  ['red','yellow','blue','green','orange','purple','white','gray']
def random_spiral():
     t.pencolor(r.choice(colors))
     size = r.randint(10,40)
     x = r.randrange(-t1.window_width()//2,t1.window_width()//2)
     y = r.randrange(-t1.window_height()//2,t1.window_height()//2)
     t.up()
     t.setpos(x,y)
     t.down()
     for m in range(size):
          t.forward(2*m)
          t.left(91)

for n in range(50):
     random_spiral()
