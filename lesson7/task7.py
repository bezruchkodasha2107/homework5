"""
Запросить любое число не менее 10. 
Вывести на экран сумму квадратов каждой цифры составляющей это число. 
Например: дано 236 => 2*2 + 3*3 + 6*6 = 49 

"""

while True:
    num = input("Введите чисто не менее 10: ")
    if int(num) < 10:
        print("Вы ввели неверное число. Введите еше раз")
    else:
        break

n = 0
for i in num:
    n += int(i) ** 2
print(n)