import math
import random

# Первое задание
some_list = [3, 5, 16, 25, 36, 7, 49]
square_list = []

for num in some_list:
    if num > 0 and (math.sqrt(num)) % 1 == 0:
        square_list.append(int(math.sqrt(num)))
print(square_list)

# Второе задание

date = input('Введите дату в формате dd.mm.yyyy: ')
date_we_need = (date.split('.'))
day = {'01': 'первое', '02': 'второе', '03': 'третье', '04': 'четвертое', '05': 'пятое', '06': 'шестое',
       '07': 'седьмое', '08': 'восьмое', '09': 'девятое', '10': 'десятое', '11': 'одинадцатое', '12': 'двенадцатое',
       '13': 'тринадцатое', '14': 'четырнадцатое', '15': 'пятьнадцатое', '16': 'шестьнадцатое', '17': 'семнадцатое',
       '18': 'восемнадцатое', '19': 'девятнадцатое', '20': 'двадцатое', '21': 'двадцать первое',
       '22': 'двадцать второе', '23': 'двадцать третье', '24': 'двадцать четвертое', '25': 'двадцать пятое',
       '26': 'двадцать шестое', '27': 'двадцать седьмое', '28': 'двадцать восьмое', '29': 'двадцать девятое',
       '30': 'дридцатое', '31': 'тридцать первое'}
month = {'01': 'января', '02': 'февраля', '03': 'марта', '04': 'апреля', '05': 'мая', '06': 'июня', '07': 'июля',
         '08': 'августа', '09': 'сентября', '10': 'октября', '11': 'ноября', '12': 'декабря'}

print(f'Вы ввели {day[date_we_need[0]]} {month[date_we_need[1]]} {date_we_need[2]}')


# Третье задание


def random_list(x):
    some_list = []
    i = 0
    while i < x:
        some_list.append(random.randint(-100, 100))
        i += 1
    print(some_list)


random_list(23)

# Четвертое задание
my_last_list = [2, 2, 3, 5, 6, 7, 12, 13, 4, 15, 5]



final_list = set(my_last_list)
another_final_list = [x for x in my_last_list if not my_last_list.count(x) > 1]
print(final_list)
print(another_final_list)


