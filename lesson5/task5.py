"""
Запросить фразу 
    - вывести на экран количество уникальных символов
    - вывести на экран количество уникальных слов
    -* вывести символ который встречался чаще всего

"""
text = input("Введите фразу: ")
symbol_text = set(text.split(' '))
word_text = set(text.replace(' ', ''))
print(len(symbol_text))
print(len(word_text))
