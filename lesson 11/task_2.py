class Student:
    """
    Класс для моделирования объекта студента

    Attributes
    ----------
    surname : str
        фамилия студента
    name : str
        имя студента
    group : int
        номер группы, в которой обучается студент
    grads : list
        список оценок студента

    Methods
    ----------
    __init__(surname, name, group, grads):
        Инициализирует атрибуты фамилии, имени, группы и списка оценок студента.
    average_grade():
        Считает и возвращает среднюю оценку студента.
    __eq__(other):
        Сравнивает средние оценки двух студентов на равенство.
    __ne__(other):
        Сравнивает средние оценки двух студентов на неравенство.
    __lt__(other):
        Проверяет, меньше ли средняя оценка одного студента, чем у другого.
    __gt__(other):
        Проверяет, больше ли средняя оценка одного студента, чем у другого.
    __le__(other):
        Проверяет, меньше или равна ли средняя оценка одного студента, чем у другого.
    __ge__(other):
        Проверяет, больше или равна ли средняя оценка одного студента, чем у другого.
    add_grade(grade):
        Добавляет одну оценку в список оценок студента.
    __str__():
        Возвращает строковое представление объекта студента.
    """
    
    def __init__(self, surname, name, group, grads):
        self.surname = surname
        self.name = name
        self.group = group
        self.grads = grads 

    def average_grade(self):
        return sum(self.grads) / len(self.grads)
    
    def __eq__(self, other):
        return self.average_grade() == other.average_grade()
    
    def __ne__(self, other):
        return self.average_grade() != other.average_grade()
    
    def __lt__(self, other):
        return self.average_grade() < other.average_grade()
    
    def __gt__(self, other):
        return self.average_grade() > other.average_grade()
    
    def __le__(self, other):
        return self.average_grade() <= other.average_grade()
    
    def __ge__(self, other):
        return self.average_grade() >= other.average_grade()
    
    def add_grade(self, grade):
        self.grads.append(grade)
    
    def __str__(self):
        return f"{self.surname} {self.name}, Group: {self.group}, Average Grade: {self.average_grade():.2f}"

# Создание студентов
student1 = Student('Иванов', 'Иван', 11, [10, 5, 8, 6, 9, 9])
student2 = Student('Смирнов', 'Антон', 11, [4, 8, 9, 10, 8, 7])
student3 = Student('Новикова', 'Анастасия', 11, [8, 8, 9, 10, 8, 8])
student4 = Student('Петров', 'Евгений', 11, [4, 5, 8, 3, 2, 5])
student5 = Student('Васильева', 'Василиса', 11, [9, 8, 9, 10, 9, 9])

# Проверка методов
print(student1.average_grade())
print(student2.average_grade())

print(student1 == student2)
print(student1 != student2)
print(student1 < student2)
print(student1 > student2)
print(student1 <= student2)
print(student1 >= student2)

student1.add_grade(5)
print(student1.grads)

# Сортировка студентов по среднему баллу
list_students = [student1, student2, student3, student4, student5]
sorted_students = sorted(list_students, key=lambda student: student.average_grade())
reverse_sorted_students = sorted(list_students, key=lambda student: student.average_grade(), reverse=True)

# Вывод отсортированных студентов
print("Вывод студентов отсортированных по возрастанию:")
for student in sorted_students:
    print(student)

print("Вывод студентов отсортированных по убыванию:")
for student in reverse_sorted_students:
    print(student)

# Студенты со средним баллом больше 8
print("Студенты со средним баллом больше 8:")
students_above_8 = [student for student in list_students if student.average_grade() > 8]
for student in students_above_8:
    print(student)
