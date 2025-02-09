import turtle as tM
t = tM.Pen()
t.up()
t.speed(0)
tM.bgcolor('black')
sides = int(tM.numinput('Кол-во сторон','Сколько будет сторон у вашей спирали?', 4,2,6))
colors = ['red','yellow','blue','green','purple','orange']

for m in range(100):
     t.up()
     t.forward(m*4)
     pos = t.position()
     head = t.heading()
     for n in range(1):
          t.down()
          t.circle(m)
          t.right(360/sides-2)
          t.pensize(1)
          t.up()
     t.color(colors[m%sides])
     t.setx(pos[0])
     t.sety(pos[1])
     t.setheading(head)
     t.left(360/sides+2)
     t.down()
     
tM.exitonclick()

'int(m/2)'
