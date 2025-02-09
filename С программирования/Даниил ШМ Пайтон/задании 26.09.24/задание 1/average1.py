count = 0
summ = 0.0
number = 1

print("Введите 0, чтобы выйди из циклы")

while number != 0:
    number = float(input('Введите число:'))
    if number != 0:
        count += 1
        summ += number
    if number == 0:
        print('Среднее значение составило:', summ/count)
        
