"""
Написать функцию  которая принимает фамилию имя и отчество одной стройкой, 
а возвращает в виде краткого формата. 
Функция должна содержать необязательный параметр в виде логического значения 
и в зависимости от него возвращала ФИО в двух следующих форматах:
 -  Николаев И.С. 
 -  И.С.Николаев

"""

def fio(full_name, reverse = True):
    last_name, first_name, middle_name = full_name.split()

    if reverse:
        print(f"{last_name} {first_name[0]}. {middle_name[0]}.")
    else:
        print(f"{first_name[0]}. {middle_name[0]}. {last_name}")

full_name = input("Введите фамилию, имя и отчество: ")

fio(full_name)
fio(full_name, False)
