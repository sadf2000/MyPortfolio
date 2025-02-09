import random as r
rn = r.randint(1,10)
g = int(input('Введите число от 1 до 10:'))
while g != rn:
    if g>rn:
        print('Рандомное число меньше')
    if g<rn:
        print('Рандомное число больше')
    g = int(input('Отгадайте еще раз!:'))
print('Это:', rn)
