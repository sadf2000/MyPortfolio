def square(l):
    return l**2

def rectangle(w,h):
    return w*h

def circle(rad):
    return 3.14*rad**2

def options():
    print('''
Меню:

s - вычислить площадь квадрата
r - вычислить площадь прямоугольник
c - вычислить площадь круга

q - выйти
''')

print('Вычислитель площадей v.1.0')
choice = ''

while choice != 'q':
    options()
    choice = input('Введите ваш выбор:')

    if choice == 's':
        l = float(input('Высота или ширина:'))
        print('Площадь квадрата =',square(l))
    elif choice == 'r':
        w = float(input('Высота:'))
        h = float(input('Ширина:'))
        print('Площадь прямоугольника =',rectangle(w,h))
    elif choice == 'c':
        rad = float(input('Радиус:'))
        print('Площадь круга =',circle(rad))
    elif choice == 'q':
        print(' ', end='')
    else:
        print('Комманда неопознанна!')
    
    
