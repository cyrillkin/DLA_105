
__author__ = 'Маштаков Кирилл Владимирович'

# Задача-1: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользоваться данным ресурсом можно только с 18 лет"

# age = int(input('How old are you:'))
#
# if age >= 18:
#     print('\nДоступ разрешён')
# else:
#     print('\nИзвините, пользоваться данным ресурсом можно только с 18 лет')

# Задача-2: Напишите программу, которая спрашивает "Четные или нечетные?", в зависимости от ответа,
# используя цикл с предусловием while или for in
# вывести в одну строку через пробел соотвествующие числа от 0 до 20
# Пример работы:
# $ "Четные или нечетные?"
# четные
# 0 2 4 6 8 10 12 14 16 18 20
# $ "Четные или нечетные?"
# нечетные
# 1 3 5 7 9 11 13 15 17 19
# $ "Четные или нечетные?"
# qwerty (или любая другая строка)
# Я не понимаю, что вы от меня хотите...

# print('Четные или нечетные?')
# div = int(input('Enter number from 0 to 20:'))
#
# if div >= 0 and div <= 20:
#     div=int(div)%2
#     if div == 0:
#         print('чётные')
#     elif div == 1:
#         print('нечётные')
#     while div <= 20:
#         print(div, end = ' ')
#         div += 2
# else:
#     print('Я не понимаю, что вы от меня хотите...')

# Задача-3: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.

# x = int(input('Enter number:'))
# z = 0
# out_write = x
#
# while x > 0:
#     y = x%10
#     x = x//10
#     if y > z:
#         z = y
# print('Самая большая цифра числа', out_write, ':', z)