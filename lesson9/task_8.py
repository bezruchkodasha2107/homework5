'''
Дан список содержащий в себе различные типы данных, отфильтровать таким
образом, чтобы 
 - остались только строки.
 - остался только логический тип.
 
'''


data_list = [True, False, 123, "hello", 3.14, "world", None, True]

strings_only = filter(lambda x: isinstance(x, str), data_list)
print("Только строки:", list(strings_only))

booleans_only = filter(lambda x: isinstance(x, bool), data_list)
print("Только логические типы:", list(booleans_only))
