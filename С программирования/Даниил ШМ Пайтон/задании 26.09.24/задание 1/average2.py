sum1 = 0.0
print('Сколько чисел хотите усреднить?')
count = int(input(''))
crnt_cnt = 0

while crnt_cnt < count:
    
    crnt_cnt += 1
    print('Число', crnt_cnt)
    number = float(input('Введите число:'))
    sum1 = sum1 + number
    
    
print('Среднее арифметическое:', sum1/count)
                   
