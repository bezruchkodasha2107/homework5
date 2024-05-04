'''
Запросить высоту елочки - число от 3 до 20. 
Напечатать на экране елочку где ее высото равна числу строк. 
Пример елочки из 4 строк:
   *
  ***
 *****
*******

'''

while True:
    number = int(input("Введите число от 3 до 20: "))
    if number >= 3 and number <= 20:
        break
    else:
        print("Вы ввели неправильное число. Введите еще раз.")

for i in range(1, number + 1):
    spaces = ' ' * (number-i)
    stars = '*' * (i * 2 - 1)
    print(spaces + stars)