import math
__author__ = 'Маштаков Кирилл Владимирович'

# Задача-1: Ввести ваше имя и возраст в отдельные переменные,
# вычесть из возраста 18 и вывести на экран в следующем виде:
# "Василий на 2 года/лет больше 18"
# по желанию сделать адаптивный вывод, то есть "на 5 лет больше", "на 3 года меньше" и.т.д.

"""
name = str(input('Your name:'))
age = int(input('How old are you:'))

diff = age - 18
year = 'лет'

if(diff < 5 and diff > -5):
    year = 'года'

if diff>0:
    res = print(name, 'на', diff, year, 'больше 18')
elif diff<0:
    res = print(name, 'на', abs(diff), year, 'меньше 18')
else:
    res = print(name, 'вам 18 лет')
"""

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!

"""
var_1 = int(input('First variable:'))   #ввод первой переменной
var_2 = int(input('Second variable:'))  #ввод второй переменной

# Первый способ:
var_1, var_2 = var_2, var_1

# Второй способ:
div = var_1/var_2
var_1 = var_1/div
var_2 = var_2*div

print('\nVariables exchange!\nFirst variable:', var_1, '\nSecond variable:', var_2) #вывод на экран
"""

# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4

"""
a = int(input('First coef:'))  #коэффициент a
b = int(input('Second coef:'))  #коэффициент b
c = int(input('Third coef:'))  #коэффициент с

D = b**2 - 4 * a * c

if D > 0:
    x_1 = (-b + math.sqrt(D))/(2 * a)   # или x_1 = (-b + D**0.5)/2 * a  ;-)
    x_2 = (-b - math.sqrt(D))/(2 * a)
    print('The equation have two roots:\nx1 = ', x_1, '\nx2 = ', x_2)
elif D == 0:
    x = -b/(2 * a)
    print('The equation have one root:\nx = ', x)
else:
    print('No roots')
"""