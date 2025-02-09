def countdown(n):
    print(n)
    if n > 0:
        return countdown(n-1)
countdown(3)
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

def mult(a,b):
    if b == 0:
        return 0
    rest = mult(a,b-1)
    value = a + rest
    return value


number = -1

while number != 0:
    print('''
Test_Functions.py

Проверить функцию:

0 - exit()
1 - countdown(n)
2 - factorial(n)
3 - mult(a,b)

    ''')
    number = int(input())
    if number == 1:
        n = int(input('n = '))
        countdown(n)
    elif number == 2:
        n = int(input('n = '))
        print('factorial:', factorial(n))
    elif number == 3:
        a = int(input('a = '))
        b = int(input('b = '))
        print('mult:', mult(a,b))
    elif number == 0:
        exit()
    else:
        print('Ошибка!')
