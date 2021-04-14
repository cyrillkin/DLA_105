
# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]


a = [1, 2, 4, 0]
b = []

for i in a:
    c = i ** 2
    b.append(c)
print(a)
print(b)
print('')

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.


a = ['apple', 'banana', 'grapes', 'lemon']
b = ['orange', 'pineapple', 'lemon', 'apple']
res = []

for i in a:
    if i in b:
        pass
    else:
        res.append(i)

for n in b:
    res.append(n)

print(res)
print('')


# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4


a = [1, 5, 6, 13, 15, 20, -10, -325, 40, 104, 24]
b = []

for i in a:
    if i > 0 and i%3 == 0 and i%4 != 0:
        b.append(i)
print(b)