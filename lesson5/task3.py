"""
дан словарь
d = {'one':11, 'two':22, 'hello':'python', True:False}
запросить номер элемента и удалить его из словаря с помощью del.

"""

d = {'one':11, 'two':22, 'hello':'python', True:False}

number = int(input("Введите номер элемента: "))
key_del = list(d.keys())[number]
del d[key_del]
print(d)