'''
Запросить число от 1 до 12. 
Если ввели другое число сообщить об ошибке. 
Когда введут допустимое число - вывести на экран соответствующее 
название месяца, пору года и сколько дней в данном месяце.

'''

number = int(input("Введите число от 1 до 12: "))

if 1 <= number <= 12:
    if number == 1:
        month_name = "Январь"
    elif number == 2:
        month_name = "Февраль"
    elif number == 3:
        month_name = "Март"
    elif number == 4:
        month_name = "Апрель"
    elif number == 5:
        month_name = "Май"
    elif number == 6:
        month_name = "Июнь"
    elif number == 7:
        month_name = "Июль"
    elif number == 8:
        month_name = "Август"
    elif number == 9:
        month_name = "Сентябрь"
    elif number == 10:
        month_name = "Октябрь"
    elif number == 11:
        month_name = "Ноябрь"
    else:
        month_name = "Декабрь"

    if 3 <= number <= 5:
        season = "весна"
    elif 6 <= number <= 8:
        season = "лето"
    elif 9 <= number <= 11:
        season = "осень"
    else:
        season = "зима"

    if number in {1, 3, 5, 7, 8, 10, 12}:
        days = 31
    elif number == 2:
        days = 28 
    else:
        days = 30

    print(f"Месяц: {month_name}, Пора года: {season}, Количество дней: {days}")
else:
    print("Ошибка: Введите число от 1 до 12.")
