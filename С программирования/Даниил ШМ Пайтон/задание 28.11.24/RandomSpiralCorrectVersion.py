import random as r
import turtle as t
tp = t.Pen()
t.bgcolor('black')
tp.speed(0)
colors = ['red','yellow','blue','green','orange','purple','white','gray']
for n in range(50):
    
    tp.color(r.choice(colors))
    size = r.randint(10,40)
    x = r.randrange(-t.window_width()//2, t.window_width()//2)
    y = r.randrange(-t.window_height()//2, t.window_height()//2)
    tp.up()
    tp.setpos(x,y)
    tp.down()
    for m in range(50):
        tp.forward(2*m)
        tp.left(91)
