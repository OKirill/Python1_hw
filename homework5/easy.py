# # -*- coding: utf-8 -*-
#
if __name__ == '__main__':
    print('---------------------Задача №1 (easy)----------------------')
import os
import shutil


def make_dir(name):
    try:
        os.makedirs(name)
    except FileExistsError:
        print('{} - уже существует'.format(name))


def remove_dir(name):
    try:
        os.removedirs(name)
    except FileNotFoundError:
        print('{} - папки не существует'.format(name))


def start():
    answer = ''
    quantity_dirs = range(1, 10)

    while answer != '3':

        answer = input('Выберите пункт меню:\n'
                       '1. Создать папки dir_1 - dir_9\n'
                       '2. Удалить папки dir_1 - dir_9\n'
                       '3. Выход\n')
        if answer == '3':
            break
        if answer == '1':
            for i in quantity_dirs:
                i = str(i)
                make_dir('dir_' + i)
        elif answer == '2':
            for i in quantity_dirs:
                i = str(i)
                remove_dir('dir_' + i)


if __name__ == '__main__':
    start()

if __name__ == '__main__':
    print('---------------------Задача №2 (easy)----------------------')


def list_dir():
    buffer = os.listdir()
    print('****************************************')
    print('Список Папок:')
    for index, element in enumerate(buffer, start=1):
        if os.path.isdir(element):
            print('{}. {}'.format(index, element))


def list_files():
    files = os.listdir()
    print('****************************************')
    print('Список Файлов:')
    for index, element in enumerate(files, start=1):
        if os.path.isfile(element):
            print('{}. {}'.format(index, element))


if __name__ == '__main__':
    list_dir()
    list_files()

if __name__ == '__main__':
    print('---------------------Задача №3 (easy)----------------------')


def current_file_copy():
    name_file = os.path.realpath(__file__)
    new_file = name_file + '.copy'
    if os.path.isfile(new_file) != True:
        shutil.copy(name_file, new_file)
        return new_file + ' - создан'
    else:
        return 'Файл уже скопирован'


if __name__ == '__main__':
    print(current_file_copy())
