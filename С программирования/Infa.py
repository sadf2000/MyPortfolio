while True:
    x = input("0 - закрыть программу; 1 - высчитать среднее арифметическое);2 - сложение; 3 - высчитание; 4 - произведение(остальное - решить путем eval):")
    if x == '0':
        break
    elif x == '1':
        i = 0
        resultnum = 0
        while True:
            num=input('Напишите число(v - выйди):')
            if num == 'v':
                break
            else:
                try:
                    resultnum += float(num)
                    i += 1
                except:
                    print('Ошибка')
        print('Итого:',resultnum/float(i))
    elif x == '2':
        i = float(input('Введите 1 число:'))
        i2 = float(input('Введите 2 число:'))
        resultnum = i+i2
        print('Итого:',resultnum)
    elif x == '3':
        i = float(input('Введите 1 число:'))
        i2 = float(input('Введите 2 число:'))
        resultnum = i-i2
        print('Итого:',resultnum)
    elif x == '4':
        i = float(input('Введите 1 число:'))
        i2 = float(input('Введите 2 число:'))
        resultnum = i*i2
        print('Итого:',resultnum)
    else:
        try:
            print(eval(x))#Если пользователь хочет решить другой пример или не устраивает один из перечисленных запросов
        except:
            print('Введите что нибудь')
