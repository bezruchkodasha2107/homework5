'''
Запросить любое число. Заменить каждую цифру этого числа буквой, 
у которой номер в алфавите равен этой цифре. 
Например: 1352=aceb.
'''

number = input("Введите любое число: ")

a = ord('a')
alphabet = [chr(alpha) for alpha in range(a, a+26)]
print(alphabet)

word = ''
if int(number) > 26:
    for num in number:
        word += alphabet[int(num)-1]
else:
    word = alphabet[int(number)-1]

print(word)