"""
С помощью декораторов реализовать конвейер сборки бургера

Написать декоратор bread, который:
 - до декорируемой функции будет печатать "</------------\\>"
 - после декорируемой функции будет печатать "<\\____________/>"


Написать декоратор tomato, который:
 - до декорируемой функции будет печатать "*** помидоры ****"

Написать декоратор salad, который:
 - до декорируемой функции будет печатать "~~~~ салат ~~~~~"

Написать декоратор cheese, который:
 - до декорируемой функции будет печатать "^^^^^ сыр ^^^^^^"

Написать декоратор onion, который:
 - до декорируемой функции будет печатать "----- лук ------"

Написать функцию beef, которая:
 - печатает "### говядина ###"

Написать функцию chicken, которая:
 - печатает "|||| курица ||||"

1) Собрать с помощью декораторов гамбургер:
    - булка
    - лук
    - помидоры
    - говядина
    - булка

2) Собрать с помощью декораторов чикенбургер:
    - булка
    - сыр
    - салат
    - курица
    - булка
"""

def bread(f):
    def wrapper():
        print("</------------\\>")
        f()
        print("<\\____________/>")
    return wrapper

def tomato(f):
    def wrapper():
        print("*** помидоры ****")
        f()
    return wrapper

def salad(f):
    def wrapper():
        print("~~~~ салат ~~~~~")
        f()
    return wrapper

def cheese(f):
    def wrapper():
        print("^^^^^ сыр ^^^^^^")
        f()
    return wrapper

def onion(f):
    def wrapper():
        print("----- лук ------")
        f()
    return wrapper

def beef(f):
    def wrapper():
        print("### говядина ###")
        f()
    return wrapper

def chicken(f):
    def wrapper():
        print("|||| курица ||||")
        f()
    return wrapper


#сборка гамбурера
@bread
@onion
@tomato
def beef():
    print("### говядина ###")

@bread
@cheese
@salad
def chicken():
    print("|||| курица ||||")

beef()
chicken()


