'''
Запросить у пользователя число вывести сколько. 
Если число менее 20 -  вывести на экран сколько чисел 
в диапазоне от 0 до этого числа делится без остатка на 7. 
Если более 20 - вывести на экран сколько чисел 
в диапазоне от 0 до этого числа делится без остатка на 11.
'''

number = int(input("Введите число: "))

if number < 20:
    divisible_by_7 = (number // 7) 
    print(f"Чисел от 0 до {number}, которые делятся на 7 без остатка:", divisible_by_7)

else:
    divisible_by_11 = (number // 11) 
    print(f"Чисел от 0 до {number}, которые делятся на 11 без остатка:", divisible_by_11)
