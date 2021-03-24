# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый- работник получал строку из файла

class Worker:
    def __init__(self, name, surname, salary, dolznost, norma):
        self.name = name
        self.surname = surname
        self.salary = int(salary)
        self.dolznost = dolznost
        self.norma = int(norma)
        self.hours = 0

    def work_hours(self):
        with open('data/hours.txt', 'r', encoding='UTF-8') as f:
            for i in f.readlines():
                if i.split()[0] == self.name and i.split()[1] == self.surname:
                    self.hours = int(i.split()[2])
                    break
                else:
                    continue

    def calc(self):
        for_hour = self.salary // self.norma
        salary = 0
        if self.hours > self.norma:
            razn = self.hours - self.norma
            salary = (razn * for_hour) * 2
            return (salary + self.salary)
        elif self.hours < self.norma:
            razn = self.norma - self.hours
            salary = razn * for_hour
            return (self.salary - salary)
        else:
            return (self.salary)

    def write(self, salary):
        with open('salary.txt', 'a', encoding='UTF-8') as f:
            f.write(self.name + ' ' + self.surname + ' ' + str(salary) + ' ' + self.dolznost)
            f.write('\n')


if __name__ == '__main__':
    def total(file):
        f = open(file, 'r', encoding='UTF-8')
        for i in f.readlines():
            if i.count('Имя') == 1:
                continue
            else:
                name, surname, salary, position, norm_hours = i.split()
                workman = Worker(name, surname, salary, position, norm_hours)
                workman.work_hours()
                salary = workman.calc()
                workman.write(salary)
        f.close()

total('data/workers.txt')