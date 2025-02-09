import turtle as t
num = int(t.numinput('кол-во сторон или окружностей','Сколько сторон или окружностей?:',6))

shape = t.textinput('Какую форму вы хотите?','Введите m если это многоульник, введите r если это роззета')
tP = t.Pen()
tP.speed(0)
tP.width(2)
#print(str(num)+str('/')+str(x))
for x in range(num):
    if shape == 'r':
          tP.circle(100)
          
    elif shape == 'm':
          tP.forward(150)
    else:
        print('Ошибка: Неправильный ввод!')
        
    tP.left(360/num)
    print(str(num)+str('/')+str(x))
    
print('Законченно!')
