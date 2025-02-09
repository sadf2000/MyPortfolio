import os
os.system('color 2')
menu_item = -1
namelist = []
while menu_item != 0:
    os.system('cls')
    print('''
--------------------------------------
1. Вывести список
2. Добавить имя в список
3. Удалить имя из списка
4. Изменить элемент в списке
0. Выйди
''')
    menu_item = int(input('Выберите пункт меню: '))
    if menu_item == 1:
        current = 0
        if len(namelist) > 0:
            while current < len(namelist):
                print(current,'.', namelist[current])
                current += 1
            input()
        else:
            print('Список пуст')
            input()
    elif menu_item == 2:
        name = input('Введите новое имя:')                  
        namelist.append(name)
    elif menu_item == 3:
        del_name = input('Какое имя удалить?')
        if del_name in namelist:
            item_number = namelist.index(del_name)
            del namelist[item_number]
        else:
            print(del_name, 'не найдено!')
            input()
    elif menu_item == 4:
        old_name = input('Какое имя вы бы хотели изменить?')
        if old_name in namelist:
            item_number = namelist.index(old_name)
            new_name = input('Новое имя: ')
            namelist[item_number] = new_name
        else:
            print(old_name, 'не найдено!')
            input()
    else:
        print('Неправильный запрос!')
        input()

print('До свидания!')
input()






        

