import os
import shutil
import sys

# Задача-1:
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

# ПРИМЕЧАНИЕ: Для решения задач 2-4 необходимо познакомиться с модулями os, sys!
# СМ.: https://pythonworld.ru/moduli/modul-os.html, https://pythonworld.ru/moduli/modul-sys.html

# Задача-2:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

def make_dir(dir):
    dir_path = os.path.join(os.getcwd(), dir)
    try:
        os.mkdir(dir_path)
        print('Папка', dir, 'создана')
    except FileExistsError:
        print('Папка', dir, 'уже существует')

def remove_dir(dir):
    dir_path = os.path.join(os.getcwd(), dir)
    try:
        os.rmdir(dir_path)
        print('Папка', dir, 'удалена')
    except FileNotFoundError:
        print('Папки', dir, 'не существует')

# Задача-3:
# Напишите скрипт, отображающий папки текущей директории.

def current_dir(path):
    for i in os.listdir(path):
        print(i)

# Задача-4:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def copy(new_name):
    file_name = os.path.basename(sys.argv[0])
    shutil.copy(file_name, new_name)

if __name__ == '__main__':

 #   avg(10, 20)

    # i = 1
    # while i <= 9:
    #     dir = 'dir_' + str(i)
    #     make_dir(dir)
    #     i += 1

    # i = 1
    # while i <= 9:
    #     dir = 'dir_' + str(i)
    #     remove_dir(dir)
    # i += 1

    path = os.getcwd()
    current_dir(path)
    copy('hgyu')