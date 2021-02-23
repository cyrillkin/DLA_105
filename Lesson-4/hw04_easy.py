# Задание-1:
# Напишите функцию, переводящую км в мили и выводящую информацию на консоль
# т.е функция ничего не возвращает, а выводит на консоль ответ самостоятельно
# Предполагается, что 1км = 1,609 мили

# def convert(km):
#     miles = 1.609*km
#     print(miles)
# convert(15)

# Задание-2:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.


# def my_round(number, ndigits):
#     integer = int(number)
#     fraction = number % 1 * 10 ** ndigits
#     balance = float(fraction) - int(fraction)
#     if balance >= 0.5:
#         var = integer + (int(fraction) + 1) / 10 ** ndigits
#         var = '{:.5f}'.format(var)
#         return var
#     else:
#         var = intreger + int(fraction) / 10 ** ndigits
#         var = '{:.5f}'.format(var)
#         return var
#
# print(my_round(2.1234567, 5))
# print(my_round(2.1999967, 5))
# print(my_round(2.9999967, 5))
#
# второй вариант
#
# def my_round(number, ndigits):
# # number = 2.64515
# # ndigits = 0
#     a = str(number).split('.')
#
# # k_1
#     if int(a[1][0] and ndigits == 0) >= 5:
#         k_1 = int(a[0])+1
#     else:
#         k_1 = a[0]
#
# # k_2
#     len = len(a[1])
#     if ndigits ==0:
#         k_2 = ""
#     elif ndigits < len:
#         if int(a[1][len-1]) >= 5:
#             k_2 = int(a[1][0:ndigits])+1
#         else:
#             k_2 = a[1][0:ndigits]
#     elif ndigits == len:
#         k_2 = a[1][0:ndigits]
#     else:
#         k_2 = a[1][0:ndigits] + (ndigits - len) * '0'
#
#     if ndigits ==0:
#         str = str(k_1)
#     else:
#         str = str(k_1) + '.' + str(k_2)
#
#     return str
#
# print(my_round(2.1234567, 5))
# print(my_round(2.1999967, 5))
# print(my_round(2.9999967, 5))


# Задание-3:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить, должна возвращать либо True,
# ибо False (если счастливый и несчастливый соответственно)

# def lucky_ticket(number_ticket):
#     number = str(number_ticket)
#     lst1 = int(number[:1]) + int(number[1:2]) + int(number[2:3])
#     lst2 = int(number[-1]) + int(number[-2]) + int(number[-3])
#     if lst1 == lst2:
#         return True
#     else:
#         return False
#
# ticket = 123123
# print(lucky_ticket(ticket))