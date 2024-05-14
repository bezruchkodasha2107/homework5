"""
Дан словарь наблюдения за температурой 
{"day1":18, "day2":22, "day3":7, "day4":11, "day5":14}. 
Отсортировать словарь по температуре в порядке возрастания и обратно.

"""
d = {"day1":18, "day2":22, "day3":7, "day4":11, "day5":14}

d1 = dict(sorted(d.items(), key=lambda item : item[1]))
print(d1)

d2 = dict(sorted(d.items(), key=lambda item : item[1], reverse=True))
print(d2)