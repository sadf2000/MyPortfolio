#graphsmile.py
import turtle as t1
import random as r
t = t1.Pen()
t.speed(0)
t1.bgcolor('black')
colors  =  ['red','yellow','blue','green','orange','purple','white','gray']



def head():
     t.color('yellow') # 'yellow'
     t.begin_fill()
     t.circle(50)
     
     t.end_fill()
def right_eye(x,y):
     
     t.setpos(x-15, y+60)
     t.down()
     t.color('black') #black
     t.begin_fill()
     t.circle(10)
     t.end_fill()
     t.up()
def left_eye(x,y):
     t.setpos(x+15, y+60)
     t.down()
     t.color('black') #black
     t.begin_fill()
     t.circle(10)
     t.end_fill()
     t.up()


def Ulibka(x,y):
     
     t.setpos(x-25,y+40)
     t.down()
     t.color('black') #black
     t.width(10)
     t.goto(x-10,y+20)
     t.goto(x+10,y+20)
     t.goto(x+25,y+40)
     t.width(1)
     t.up()

def draw_smiley(x,y):
     t.hideturtle()
     t.up()
     t.setpos(x,y)
     t.down()
     head()
     right_eye(x,y)
     left_eye(x,y)
     Ulibka(x,y)
     

     

for n in range(50):
     x = r.randrange(-t1.window_width()//2,t1.window_width()//2)
     y = r.randrange(-t1.window_height()//2,t1.window_height()//2)
     draw_smiley(x,y)







     

