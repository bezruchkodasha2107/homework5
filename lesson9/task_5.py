'''
*Написать рекурсивную функцию, которая принимает список 
и печатает каждых элемент на новой строке. 
Если элемент списка - список, то его элементы должны выводиться 
с отступом относительно родительского на 2 символа. 
Символ для отступа передать дополнительными необязательным параметром.

Пример1: some_list = [1, 2, 3, [4, [5, 6], 7], 8, 9]
1
2
3
--4
----5
----6
--7
8
9

Пример2: some_list=[1,[2,[[3],4]],5,[[[6,7]]],8,[[[[9,10]],11]],12]
1
--2
------3
----4
5
------6
------7
8
--------9
--------10
----11
12


'''