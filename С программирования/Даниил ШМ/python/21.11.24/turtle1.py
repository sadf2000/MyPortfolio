import turtle as tM
t = tM.Pen()
t.up()
t.speed(99999999999999999999999999999999999999999999999999999999)
tM.bgcolor('black')
sides = int(tM.numinput('Кол-во сторон','Сколько будет сторон у вашей спирали?', 4,2,6))
colors = ['red','yellow','blue','green','purple','orange']
for m in range(100):
     t.forward(m*4)
     pos = t.position()
     head = t.heading()
     for n in range(int(m/2)):
          t.down()
          t.color(colors[n%sides])
          t.forward(2*n)
          t.right(360/sides-2)
          t.up()
     t.setx(pos[0])
     t.sety(pos[1])
     t.setheading(head)
     t.left(360/sides+2)
     
     
