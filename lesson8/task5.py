'''
Написать функцию count_char, которая принимает строковое значение,
из которого создает и возвращает словарь, следующего вида:
{'буква': 'количество-вхождений-в-строку'}
Нельзя пользоваться collections.Counter!

'''
a = input("Напишите фразу: ")

def count_char(frase):
    dict_frase = {}
    
    for i in frase:
        if i in dict_frase:
           dict_frase[i] += 1
        elif i == ' ':
            continue
        else:
           dict_frase[i] = 1
    return dict_frase

print(count_char(a))