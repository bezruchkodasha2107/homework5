"""
Написать декоратор который позволит не останавливать программу 
в случае если любая декорируемая функция выбрасывает ошибку, 
а выводить имя функции в которой произошла ошибка и информацию об ошибке в консоль. 
Имя функции можно узнать использовав свойство __name__ ( print(func.__name__) )
"""
def not_error_decorator(f):
    def wrapper(*args):
        try:
            print(f(*args))
        except ZeroDivisionError as e:
            print(f.__name__)
        except TypeError as e:
            print(f.__name__)
            
    return wrapper

@not_error_decorator
def numerical(a, b):
    return a/b

numerical(5, 'a')