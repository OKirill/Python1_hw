import re

# name = input(' Введите ваше Имя: ')
# surname = input('Введите вашу фамилию: ')
# email = input('Введите ваш  email: ')
# if re.match('^[А-Я]{1,1}', name):
#     if re.match('^[А-Я]{1,1}', surname):
#         if re.findall('[a-z0-9_]+@+[a-z0-9]+\.(ru|com|org)', email):
#             print('Добрый день, {} {}! Ваш почтовый адрес: {}'.format(name, surname, email))
# else:
#     print('Проверьте правильность написания')

name = input(' Введите ваше Имя: ')
surname = input('Введите вашу фамилию: ')
email = input('Введите ваш  email: ')
pattern = '^[А-Я]{1,1}'
if not re.search(pattern, name):
    print('Имя введено неверно')
if not re.search(pattern, surname):
    print('Фамилия введена неверно')
if not re.search('^[a-z0-9_]+@+[a-z0-9]+\.(ru|com|org)', email):
    print('email Введен неверно')


some_str = '''
Мороз и солнце; день чудесный!
Еще ты дремлешь, друг прелестный —
Пора, красавица, проснись:
Открой сомкнуты негой взоры
Навстречу северной Авроры,
Звездою севера явись!
Вечор, ты помнишь, вьюга злилась,
На мутном небе мгла носилась;
Луна, как бледное пятно,
Сквозь тучи мрачные желтела,
И ты печальная сидела —
А нынче... погляди в окно:
Под голубыми небесами
Великолепными коврами,
Блестя на солнце, снег лежит;
Прозрачный лес один чернеет,
И ель сквозь иней зеленеет,
И речка подо льдом блестит.
Вся комната янтарным блеском
Озарена. Веселым треском
Трещит затопленная печь.
Приятно думать у лежанки.
Но знаешь: не велеть ли в санки
Кобылку бурую запречь?
Скользя по утреннему снегу,
Друг милый, предадимся бегу
Нетерпеливого коня
И навестим поля пустые,
Леса, недавно столь густые,
И берег, милый для меня.'''

import re
pattern = '\.{2,}'

result = re.search(pattern, some_str)

if result:
    print('У нас есть более одной точки')
else:
    print('В тексте нет более одной точки.')