import os
import sys
from hw06_easy import current_dir, make_dir, remove_dir


# Задача-1:
# Примечание: Если уже делали easy задание, то просто перенесите решение сюда.
# Следующая программа написана верно, однако содержит места потенциальных ошибок.
# используя конструкцию try добавьте в код обработку соответствующих исключений.
# Пример.
# Исходная программа:


def avg(a, b):

    """Вернуть среднее геометрическое чисел 'a' и 'b'.

    Параметры:
        - a, b (int или float).

    Результат:
        - float.
    """
    while True:
        try:
           a = float(input("a = "))
           break
        except ValueError:
           print('Введите любое число')
           continue

    while True:
       try:
           b = float(input("b = "))
           break
       except ValueError:
           print('Введите любое число')
           continue
    c = (a * b) ** 0.5
    print("Среднее геометрическое = {:.2f}".format(c))


# ПРИМЕЧАНИЕ: Для решения задачи 2-3 необходимо познакомиться с модулями os, sys!
# СМ.: https://pythonworld.ru/moduli/modul-os.html, https://pythonworld.ru/moduli/modul-sys.html

# Задача-2:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь "меню" выбора действия, в котором будут пункты:
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


move_to_dir = sys.argv[1]
look_current_dir = sys.argv[2]
make_new_dir = sys.argv[3]
remove_current_dir = sys.argv[4]


dir = os.path.join(os.getcwd(), move_to_dir)
os.chdir(dir)

dir2 = os.path.join(os.getcwd(), look_current_dir)
current_dir(dir2)

dir_path = os.path.join(os.getcwd(), make_new_dir)
make_dir(dir_path)

remove_current_dir = os.path.join(os.getcwd(), remove_current_dir)
remove_dir(remove_current_dir)