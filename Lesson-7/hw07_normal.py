# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

class Person:
    def __init__(self, full_name):
        self.full_name = full_name

    def get_full_name(self):
        return self.full_name

class Student(Person):
    def __init__(self, full_name, first_parent, second_parent, school_class):
        Person.__init__(self, full_name)
        self.first_parent = first_parent
        self.second_parent = second_parent
        self.school_class = school_class

    def get_class_room(self):
        return self.school_class

    def get_parent(self):
        return self.first_parent, self.second_parent

class Teacher(Person):
    def __init__(self, full_name, classes, subject):
        Person.__init__(self, full_name)
        self.classes = classes
        self.subject = subject

    def get_subject(self):
        return self.subject

    def get_classes(self):
        return self.classes

if __name__ == '__main__':

    #classes
    school_classes = ['9A', '10A', '11B']

    #students
    students = [Student('Иванов И.И.', 'Иван Иванович', 'Анна Ивановна', school_classes[0]), Student('Петров П.П.', 'Петр Иванович', 'Юлия Ивановна', school_classes[1]), Student('Сидоров С.С.', 'Семён Иванович', 'Мария Ивановна', school_classes[2])]

    #parents
    parent_1 = ['Иван Иванович', 'Анна Ивановна']
    parent_2 = ['Петр Иванович', 'Юлия Ивановна']
    parent_3 = ['Семён Иванович', 'Мария Ивановна']

    #teachers
    teachers = [Teacher('Семёнов В.И', ['9A', '10A'], 'Math'), Teacher('Борисов С.А', ['9A', '11B'], 'English'), Teacher('Попов К.У', ['10A', '11B'], 'History')]

    # 1. Получить полный список всех классов школы
    for i in students:
        print(i.get_class_room())

    # 2. Получить список всех учеников в указанном классе
    # (каждый ученик отображается в формате "Фамилия И.О.")
    name_class = '11A'
    for i in students:
        if i.get_class_room() == name_class:
            print('\n' + i.get_full_name())

    # 3. Получить список всех предметов указанного ученика
    # (Ученик --> Класс --> Учителя --> Предметы)

    name_student = students[0]
    for i in teachers:
        name_class = i.get_classes()

    for name_class in teachers:
        name_teacher = i.get_full_name()

    for name_teacher in teachers:
        name_subject = name_teacher.get_subject()

    print(name_student.get_full_name() + ' --> ' + name_student.get_class_room() + ' --> ' + name_teacher.get_full_name() + ' --> ' + name_teacher.get_subject())

    # 4. Узнать ФИО родителей указанного ученика
    parents = name_student.get_parent()
    print(parents)

    # 5. Получить список всех Учителей, преподающих в указанном классе
    name_class = '10A'
    for i in teachers:
        if name_class in i.get_classes():
            print(i.get_full_name())