"""
Запросить трижды ввод наименования товаров и их цену через пробел. 
"пример: 
>>>яблоко 10"
>>>груша 15
>>>малина 20
    
    - создать из введенных данных словарь где ключ это наименование, а цена значение
    - запросить имя товара, найти его в словаре, и вывести его цену, увеличенную на 15%. 
    - вывести сумму всех товаров

"""

tovar_1 = input("Введите название первого товара и его цену ")
tovar_2 = input("Введите название второго товара и его цену ")
tovar_3 = input("Введите название третьего товара и его цену ")

tovar_1_name, tovar_1_price = tovar_1.split(' ')
tovar_2_name, tovar_2_price = tovar_2.split(' ')
tovar_3_name, tovar_3_price = tovar_3.split(' ')

tovar_1_price, tovar_2_price, tovar_3_price = map(float, [tovar_1_price, tovar_2_price, tovar_3_price])

dict_tovar = {
    tovar_1_name: tovar_1_price,
    tovar_2_name: tovar_2_price,
    tovar_3_name: tovar_3_price
}

print(dict_tovar)

poisk = input("Введите имя товара для его поиска ")
price_with_increase = dict_tovar.get(poisk) * 1.15
print(price_with_increase)

sum_tovar = sum(dict_tovar.values())
print(f"Сумма всех товаров равнв: {sum_tovar}")