import turtle as t
sides = int(t.numinput('кол-во сторон','Сколько сторон у спирали?:',4))
tP = t.Pen()
tP.speed(0)
tP.width(2)
t.bgcolor('black')
colors = ['red','yellow','blue','green','purple','orange']
#print(str(num)+str('/')+str(x))
for m in range(5,75):
    tP.left(360/sides+5)
    tP.width(m//25+1)
    tP.up()
    tP.forward(4*m)
    tP.down()
    
    tP.color(colors[m%sides])
    if(m%2==0):
        for n in range(sides):
            tP.circle(m/3)
            tP.right(360/sides)
    else:
        for n in range(sides):
            tP.forward(m)
            tP.right(360/sides)
    
print('Законченно!')
