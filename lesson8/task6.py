"""
Напишите функцию yes_or_no, которая принимает список из целых чисел,
а возвращает список из Yes или No для каждого элемента, 
Yes - если число уже встречалось и No, если нет
[1,2,3,1,4] => [no, no, no, yes, no]

если в списке не все целые числа вернуть False.

"""
def yes_or_no(l):
    seem = {}
    result = []

    for num in l:
        if not isinstance(num, int):
            return False
        if num in seem:
            result.append('yes')
        else:
            result.append('no')
            seem[num] = True
    return result

l = [1, 2, 3, 1, 4.2]
print(yes_or_no(l))
