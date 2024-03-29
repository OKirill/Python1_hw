# -*- coding: utf-8 -*-

# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

if __name__ == '__main__':
    print('---------------------Задача №1 (normal)----------------------')

import os
import easy

def change_dir (path):
    try:
        os.chdir(path)
        return 'Успешно перешли в папку: {}'.format(path)
    except FileNotFoundError:
        return ('dir_{} - папки не существует'.format(path))

def start ():
    answer =''
    while answer != '5':
        print('----------------------------------------')
        print('Текущая директория: ' + os.getcwd())
        answer = input('Выберите пункт меню:\n'
                       '1. Перейти в папку\n'
                       '2. Помотреть Директории текущей папки\n'
                       '3. Посмотреть Файлы текущей папки\n'
                       '4. Удалить папку\n'
                       '5. Создать папку\n'
                       '6. Выход\n')
        if answer =='6':
            break
        if answer == '1':
            path_name = input('Укажите папку для перехода: ')
            print(change_dir(path_name))
        elif answer == '2':
            easy.list_dir()
        elif answer == '3':
            easy.list_files()
        elif answer == '4':
            name = input('Введите имя удаляемой папки: ')
            easy.remove_dir(name)
        elif answer == '5':
            name = input('Введите имя новой папки: ')
            easy.make_dir(name)



if __name__ == '__main__':
    start()