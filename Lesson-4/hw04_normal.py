# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1


def fibonacci(n, m):
    a, b = 1, 1
    list = []
    for i in range(m):
        a, b = b, a + b
        list.append(a)
    return list[n - 1:m]


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    a = 0
    b = 1
    while b < len(origin_list):
        while a < (len(origin_list) - 1):
            if origin_list[a] > origin_list[a+1]:
                origin_list[a], origin_list[a+1] = origin_list[a+1], origin_list[a]
            a += 1
        b += 1
        a = 0


# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


def filter(item, parameter):
    list = []
    for i in parameter:
        if item(i) == True:
            list.append(i)
        else:
            continue
    return list


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.


def paral(a, b, c, d):
    if c[0] - b[0] == d[0] - a[0] and b[1] - a[1] == c[1] - d[1]:
        return True
    else:
        return False


if __name__ == '__main__':
    print(fibonacci(1, 10))
    print('')

    original_list = [2, 10, -12, 2.5, 20, -11, 4, 4, 0]
    sort_to_max(original_list)
    print(original_list)
    print('')

    print(filter((lambda x: x > 5), parameter=[1, 5, 10, 2, 46]))
    print('')

    print(paral((0, 0), (1, 1), (3, 1), (2, 0)))