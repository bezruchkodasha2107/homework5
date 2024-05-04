"""
1. Запросить у пользователей имя и отзыв о магазине. 
Программа должна запрашивать данные пока не введено слово "stop". 
Все данные сложить в словарь.
    -распечатать количество отзывов
    -распечатать отдельно имена пользователей
    -распечатать отдельно отзывы

"""

feedbacks = {}

while True:
    name = input("Введите ваше имя: ")
    if name.lower() == 'stop':
        break
    feedback = input("Напишите, пожалуйста, отзыв о магазине: ")
    if feedback.lower() == 'stop':
        break
    feedbacks[name] = feedback

print(len(feedbacks))

print("\nИмена пользователей: ")
for name in feedbacks.keys():
    print(name)

print("\nОтзывы пользователей: ")
for feedback in feedbacks.values():   
    print(feedback)





