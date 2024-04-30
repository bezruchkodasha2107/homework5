'''
Буква "a" стоит 10 очков, "b" - 20, "c" - 30, "d" - 40
Запросить кодовою фразу из пяти символов используя только a, b, c, d.
Вывести на экран общее количество очков введенной фразы.

'''

point_dict = {
    "a" : 10,
    "b" : 20,
    "c" : 30,
    "d" : 40
}

text = input("Введите кодовую фразу: ")
total_sum = point_dict.get(text[0]) + point_dict.get(text[1]) + point_dict.get(text[2]) + point_dict.get(text[3]) + point_dict.get(text[4])
print(total_sum)