import re
import random
import string
from datetime import datetime, timedelta
import sqlite3

class User:
    def __init__(self, name, login, password=None) -> None:
        self.id = None
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
    
    def save(self):
        connection = sqlite3.connect('my_database.db')
        cursor = connection.cursor()

        if self.id is None:
            cursor.execute('''
                INSERT INTO users (name, login, password, is_blocked, subscription_date, subscription_mode)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (self.name, self.login, self.password, int(self.is_blocked), self.subscription_date.isoformat(), self.subscription_mode))
            self.id = cursor.lastrowid # получение идентификатора
        else:
            cursor.execute('''
                UPDATE users
                SET name = ?, login = ?, password = ?, is_blocked = ?, subscription_date = ?, subscription_mode = ?
                WHERE id = ?
            ''', (self.name, self.login, self.password, int(self.is_blocked), self.subscription_date.isoformat(), self.subscription_mode, self.id))

        connection.commit()
        connection.close()

    def add_service(self, service_id, start_date=None):
        connection = sqlite3.connect('my_database.db')
        cursor = connection.cursor()
        if start_date is None:
            start_date = datetime.now().isoformat()
        cursor.execute('''
            INSERT INTO user_services (user_id, service_id, start_date)
            VALUES (?, ?, ?)
        ''', (self.id, service_id, start_date))
        connection.commit()
        connection.close()

    def remove_service(self, service_id):
        connection = sqlite3.connect('my_database.db')
        cursor = connection.cursor()

        cursor.execute('''
            DELETE FROM user_services
            WHERE user_id = ? AND service_id = ?
        ''', (self.id, service_id))

        connection.commit()
        connection.close()

    def extend_service(self, service_id, additional_days):
        connection = sqlite3.connect('my_database.db')
        cursor = connection.cursor()

        cursor.execute('''
            SELECT start_date FROM user_services
            WHERE user_id = ? AND service_id = ?
        ''', (self.id, service_id))
        result = cursor.fetchone()

        if result:
            start_date = datetime.fromisoformat(result[0])
            new_end_date = start_date + timedelta(days=additional_days)

            cursor.execute('''
                UPDATE user_services
                SET start_date = ?
                WHERE user_id = ? AND service_id = ?
            ''', (new_end_date.isoformat(), self.id, service_id))
        else:
            self.add_service(service_id, datetime.now().isoformat())

        connection.commit()
        connection.close()

def create_tables():
    connection = sqlite3.connect('my_database.db')
    cursor = connection.cursor()

    # Создание таблицы пользователей
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT,
            login TEXT,
            password TEXT,
            is_blocked INTEGER,
            subscription_date TEXT,
            subscription_mode TEXT
        )
    ''')

    # Создание таблицы услуг
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS services (
            id INTEGER PRIMARY KEY,
            name TEXT,
            type INTEGER,
            cost REAL,
            period INTEGER
        )
    ''')

    # Создание таблицы пользовательских услуг
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_services (
            user_id INTEGER,
            service_id INTEGER,
            start_date TEXT,
            FOREIGN KEY(user_id) REFERENCES users(id),
            FOREIGN KEY(service_id) REFERENCES services(id)
        )
    ''')

    connection.commit()
    connection.close()

# Создаем таблицы
create_tables()

# Создаем экземпляры пользователей
user1 = User(name="Иван", login="ivan_login1")
user2 = User(name="Петр", login="peter_login2")

# Сохраняем пользователей в базе данных
user1.save()
user2.save()

# Создаем экземпляры услуг
services = [
    {'name': 'Сервис 1', 'type': 1, 'cost': 10.0, 'period': 30},
    {'name': 'Сервис 2', 'type': 0, 'cost': 0.0, 'period': 15},
    {'name': 'Сервис 3', 'type': 1, 'cost': 20.0, 'period': 60}
]

# Сохраняем услуги в базе данных
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

cursor.execute('''
    INSERT INTO services (name, type, cost, period)
    VALUES (?, ?, ?, ?)
''', (services[0]['name'], services[0]['type'], services[0]['cost'], services[0]['period']))

cursor.execute('''
    INSERT INTO services (name, type, cost, period)
    VALUES (?, ?, ?, ?)
''', (services[1]['name'], services[1]['type'], services[1]['cost'], services[1]['period']))

cursor.execute('''
    INSERT INTO services (name, type, cost, period)
    VALUES (?, ?, ?, ?)
''', (services[2]['name'], services[2]['type'], services[2]['cost'], services[2]['period']))

connection.commit()
connection.close()

# Добавляем услуги для пользователя user1
user1.add_service(service_id=1)  # service_id = 1 для 'Сервис 1'
user1.add_service(service_id=2)  # service_id = 2 для 'Сервис 2'

# Показываем информацию о пользователе и его подключенных услугах
print(user1.get_info())

# Продляем одну из услуг для пользователя user1
user1.extend_service(service_id=1, additional_days=15)  # Продляем 'Сервис 1' на 15 дней

# Удаляем одну из услуг для пользователя user1
user1.remove_service(service_id=2)  # Удаляем 'Сервис 2'

# Показываем обновленную информацию о пользователе и его подключенных услугах
print(user1.get_info())
