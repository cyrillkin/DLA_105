# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3


# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"


workers = []
hours = []

workers_file = open('data/workers', 'r', encoding='UTF-8')
for i in workers_file:
    workers.append(i.strip())
workers_file.close()

hours_file = open('data/hours_of', 'r', encoding='UTF-8')
for i in hours_file:
    hours.append(i.strip())
hours_file.close()

workers = workers[1:]
hours = hours[1:]

vedomost = open('data/total.txt', 'w', encoding='UTF-8')
for m in workers:
    x = m.split(' ')
    name_workers = x[0]
    surname_workers = x[1]
    for n in hours:
        y = n.split(' ')
        name_hours = y[0]
        surname_hours = y[1]
        if name_workers == name_hours and surname_workers == surname_hours:
            salary = int(x[2])
            norma = int(x[4])
            work_hours = int(y[2])
            work = work_hours - norma
            if work > 0:
                total = salary + ((salary / norma) * (work_hours - norma)) * 2
            else:
                total = salary + (salary / norma) * (work_hours - norma)

            write_str = name_workers + ' ' + surname_hours + ' ' + str(total) + '\n'
            vedomost.write(write_str)
vedomost.close()


# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))


dict = dict()

with open('data/fruits.txt', 'r', encoding='UTF-8') as read:
    for i in read.readlines():
        file = 'fruits_{}'.format(i[0].upper().strip())
        dict[file] = dict.get(file, '') + i

for n in dict:
    name = 'data/{}.txt'.format(n)
    with open(name, 'w', encoding='UTF-8') as record:
        record.write(dict[n])