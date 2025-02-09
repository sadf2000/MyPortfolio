'параметры:'
import random
number = random.randint(1,10)
guess = -1
'принт:'
print('угадайте число!')
while guess != number:
    guess = int(input('Это... :'))
    if guess == number:
        print('угадали!')

    if guess > number:
        print('Оно меньше')
    if guess < number:
        print('Оно больше')
                           
