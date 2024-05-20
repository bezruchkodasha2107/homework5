"""
Написать функцию dict_from_args, которая принимает неограниченное
количество позиционных аргументов и неограниченное количество аргументов
ключевых-слов.

Если все позиционные аргументы - целые числа, то рассчитать их сумму. Если
нет, то кинуть ошибку TypeError(Все позиционные аргументы должны быть целыми).

Если все именованные аргументы - ключевые слова являются строками, то найти максимальную
длину слова. Если нет, то кинуть ошибку TypeError(Все аргументы - ключевые
слова должны быть строками).

Функция должна вернуть словарь, вида:
{
    "args_sum": 13,
    "kwargs_max_len": 7
}
"""
def dict_from_args(*args, **kwargs):

    for arg in args:
        if not isinstance(arg, int):
            raise TypeError ("Все позиционные аргументы должны быть целыми")
        
    args_sum = sum(args)

    for kwarg in kwargs.keys():
        if not isinstance(kwarg, str):
            raise TypeError("Все аргументы - ключевые слова должны быть строками")
        
    kwargs_max_len = max([len(key) for key in kwargs.keys()])

    result = {
        "args_sum": args_sum,
        "kwargs_max_len": kwargs_max_len
    }

    return result

try:
    print(dict_from_args(1, 2, 3, 4, 5, a=9, aa=52, bbbbbbb=0))
except TypeError as e:
    print(e)

try:
    print(dict_from_args(1, 2, 3.5, 4, 5, a=9, aa=52, bbbbbbb=0))
except TypeError as e:
    print(e)
    


  



    