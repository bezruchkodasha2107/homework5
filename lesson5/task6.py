'''
Запросить 3 раза строку из нескольких чисел через пробел
    - вывести все уникальные числа по возрастанию
    - вывести числа которые есть в каждой строке
    -* вывести числа которые есть только в одной из трех строк
    
    выполнить без циклов и условий
    
    пример:
    >>> 1 2 11 22
    >>> 1 2 22 33
    >>> 1 2 33 44

    1) 1 2 11 22 33 44
    2) 1 2
    3) 11 44
'''

set_1 = input("Введите первую строку чисел через пробел: ").split()
set_2 = input("Введите вторую строку чисел через пробел: ").split()
set_3 = input("Введите третью строку чисел через пробел: ").split()

set_1, set_2, set_3 = map(set, [set_1, set_2, set_3])

unique_numbers = sorted(set_1.union(set_2, set_3), key=int)
print("Уникальные числа по возрастанию:", *unique_numbers)

common_numbers = sorted(set_1.intersection(set_2, set_3), key=int)
print("Числа, которые есть в каждой строке:", *common_numbers)

exclusive_numbers = sorted((set_1 - set_2 - set_3), key=int)
print("Числа, которые есть только в первой из трех строк:", *exclusive_numbers)

exclusive_numbers = sorted((set_1 ^ set_2 ^ set_3), key=int)
print("Числа, которые есть только в первой из трех строк:", *exclusive_numbers)

