"""
Дан список пользователей след. формата: 
[{"name":"some_name", "login":"some_login", "password":"some_password" },
 ...
]

Отфильтровать используя функцию filter() список на предмет паролей 
которые менее 5 символов.

*Отфильтровать используя функцию filter() список на предмет валидных логинов. 
Валидный логин должен содержать только латинские буквы, цифры и черту подчеркивания. 
Каждому пользователю с плохим логином вывести текст 
"Уважаемый user_name, ваш логин user_login не является корректным."

"""
import re

list_people = [{"name":"Yana", "login":"yana25", "password":"123456"},
               {"name":"Kirill", "login":"21_Kirill_05", "password":"56865265"},
               {"name":"Dasha", "login":"Dasha_2005", "password":"21072005"}]

l1 = filter(lambda x : True if len(x['password']) >= 5 else False, list_people)
print(list(l1))

l2 = filter(lambda x : True if re.search('\w', x['login']) and '_' in x['login'] else False, list_people)
print(list(l2))