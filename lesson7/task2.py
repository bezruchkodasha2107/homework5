'''
Запросить фразу состоящую минимум из трех слов. 
Сформировать фразу из этих слов в которой каждая буква слова, 
продублирована то количество раз, которое соответствует номеру позиции 
данной буквы в слове этой буквы. 
Например: Привет как дела => Прриииввввееееетттттт кааккк деелллаааа

'''
while True:
    phrase = input("Введите фразу состоящую из трех слов: ")
    words = phrase.split()
    if len(words) >= 3:
        break
    else:
        print("Вы ввели маленькую фразу. Введите фразу еще раз. ")

new_phrase = []
for word in words:
    new_word = ''
    count = 1
    for i in word:
        new_word += i * count
        count += 1
    print(new_word)
    new_phrase.append(new_word)

print(' '.join(new_phrase))


        


