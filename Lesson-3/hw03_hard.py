﻿# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.
# equation = 'y = -12x + 11111140.2121'
# x = 2.5
# вычислите и выведите y


equation = 'y = -12x + 11111140.2121'
x = 2.5

str = equation.split(' ')
a = str[2]
coef_a = str[2][:-1]

y = float(coef_a) * x + float(str[4])
print(y)
print('')

# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом 
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

# Пример корректной даты
# date = '01.11.1985'

# Примеры некорректных дат
# date = '01.22.1001'
# date = '1.12.1001'
# date = '-2.10.3001'


date = input('Введите дату:')
d = date.split('.')

day = int(d[0])
month = int(d[1])
year = int(d[2])

a = [1, 3, 5, 7, 8, 10, 12]

if month not in a and day > 30:
    print('Введён некорректный день')
elif day > 31 or day < 1:
    print('Введён некорректный день')
elif month > 12 or month < 1:
    print('Введён некорректный месяц')
elif year > 9999 or year < 1:
    print('Введён некорректный год')
elif (len(d[0])) != 2 or len(d[1]) != 2 or len(d[2]) != 4:
    print('Введён некорректный формат даты')

else:
    print('Всё верно! Дата {} введена правильно!'.format(date))


# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты, 
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ? N ? 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3