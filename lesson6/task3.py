'''
Запросить 3 числа. Вывести наибольшее  из них. Решить используя if.
'''

numbers = input("Введите три числа: ").split()
int_numbers = list(map(int, numbers))
print(int_numbers)

if int_numbers[0] > int_numbers[1] > int_numbers[2]:
    print(int_numbers[0])
elif int_numbers[0] < int_numbers[1] < int_numbers[2]:
    print(int_numbers[2])
else:
    print(int_numbers[1])

