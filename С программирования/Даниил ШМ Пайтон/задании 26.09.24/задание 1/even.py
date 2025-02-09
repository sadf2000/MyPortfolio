number = float(input("Назовите число:"))
if number % 2 == 0:
    print(int(number), '- чётное')
elif number % 2 == 1:
    print(int(number), '- нечётное')
else:
    print(number, '- ошибка')
