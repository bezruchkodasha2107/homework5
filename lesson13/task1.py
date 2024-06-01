"""
Создать класс User с атрибутами:

Свойства:
	- name - имя - содержит только буквы русского алфавита 
	- login - логин - может содержать  только латинские буквы цифры и черту подчеркивания быть не менее 6 символов
	- password - пароль - может содержать  только латинские буквы цифры. Обязательные условия: 
                содержит менее шести символов
                содержит строчную букву
                содержит заглавную букву
                содержит число
	- is_blocked - заблокирован
	- subscription_date - дата до какой действует подписка
	- subscription_mode - вид подписки (free, paid)


Методы:
	- bloc - принимает логическое значение и помечает пользователя заблокированным 
	- check_subscr - может принимать аргумент в виде даты. Проверяет действует ли подписка на определенную дату. 
						Если дата не передана значит на дату проверки. 
						Возвращает  действует ли подписка, ее вид и сколько осталось дней.
	- change_pass - смена пароля и присваивание его в качестве действующего. 
						Пароль должен пройти валидацию. 
						Если пароль не был передан сгенерировать по правилам и вывести в консоль.
	- get_info - выводит информацию о пользователе если заблокирован то сообщает об этом.



Создание объекта должно происходить  при передаче обязательных аргументов имя и логин и необязательного - пароль. Логин и пароль должны быть проверен на валидность.
Если пароль в конструктор не был передан он должен сгенерироваться на основании правил, и должен быть выведен на экран(консоль).
При создании пользователя ему предоставляется пробная подписка сроком на 30 дней.
При изменении даты подписки  вид подписки меняется на платный.
Валидацию данных сделать через регулярные выражения
"""
import re
import random
import string
from datetime import datetime, timedelta

class User:
    def __init__(self, name, login, password=None) -> None:
        self.validate_name(name)
        self.name = name

        self.validate_login(login)
        self.login = login

        if password:
            self.validate_password(password)
            self.password = password
        else:
            self.password = self.generate_password()
            print(f"Generated password: {self.password}")

        self.is_blocked = False
        self.subscription_date = datetime.now() + timedelta(days=30)
        self.subscription_mode = 'free'

    def validate_name(self, name):
        if not re.match(r'^[А-Яа-яЁё]+$', name):
            raise ValueError('Имя должно состоять только из русских букв')

    def validate_login(self, login):
        if not re.match(r'^[A-Za-z0-9_]{6,}$', login):
            raise ValueError('Неверный логин')

    def validate_password(self, password):
        if len(password) < 6:
            raise ValueError('Пароль должен быть не менее 6 символов')
        if not re.search(r'[a-z]', password):
            raise ValueError('Пароль должен содержать маленькие буквы')
        if not re.search(r'[A-Z]', password):
            raise ValueError('Пароль должен содержать заглавные буквы')
        if not re.search(r'[0-9]', password):
            raise ValueError('Пароль должен содержать цифры')
        if not re.match(r'^[a-zA-Z0-9]+$', password):
            raise ValueError('Пароль должен состоять только из латинских букв и цифр')

    def block(self, block_status):
        self.is_blocked = block_status

    def check_subscr(self, date=None):
        date = date if date else datetime.now()
        if date <= self.subscription_date:
            days_left = (self.subscription_date - date).days
            return f"Подписка активна, тип: {self.subscription_mode}, осталось: {days_left} дней"
        else:
            return "Подписка закончилась"

    def generate_password(self):
        while True:
            password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
            try:
                self.validate_password(password)
                return password
            except ValueError:
                continue

    def change_pass(self, new_password=None):
        if new_password:
            self.validate_password(new_password)
            self.password = new_password
        else:
            self.password = self.generate_password()
            print(f"Generated password: {self.password}")

    def get_info(self):
        if self.is_blocked:
            return "Пользователь заблокирован"
        else:
            return (f"Имя: {self.name}, Логин: {self.login}, "
                    f"Вид подписки: {self.subscription_mode}, "
                    f"Дата подписки: {self.subscription_date}")


user = User(name="Иван", login="ivan_login1")
print(user.get_info())
user.change_pass()
user.block(True)
print(user.get_info())
 
        

