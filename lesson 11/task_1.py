"""
Создать класс Phone, у которого будут следующие атрибуты:

Определить атрибуты:

- brand - бренд
- model - модель
- issue_year - год выпуска

Определить методы:

- инициализатор __init__
- receive_call, который принимает имя звонящего и выводит на экран: 
        <Бренд-Модель> - Звонит {name}
- get_info, который будет возвращать кортеж (brand, model, issue_year)
- метод __str__, который выводит на экран информацию об устройстве:
Бренд: {}
Модель: {}
Год выпуска: {}
"""

class Phone:
    """
    Класс для моделирования объекта телефона

    Attributes
    ----------
    brand : str
        бренд телефона
    model : str
        модель телефона
    issue_year : int
        год выпуска

    Methods
    ----------
    receive call():
        Выводит имя звонящего
    
    get_info():
        Возвращает информацию о телефоне в кортеже

    __str__():
        Выводит информацию о телефоне 
    """

    def __init__(self, brand, model, issue_year) -> None:
        self.brand = brand
        self.model = model
        self. issue_year = issue_year

    def receive_call(self, name):
        print(f"{self.brand} - {self.model} - Звонит {name}")

    def get_info(self):
        return (self.brand, self.model, self.issue_year)
    
    def __str__(self):
        return f"Бренд: {self.brand}\n" \
               f"Модель: {self.model}\n" \
               f"Год выпуска: {self.issue_year}"

phone1 = Phone('Apple', 'Iphone 14 Pro Max', 2022)
phone1.receive_call('Макс')
print(phone1.get_info())
print(phone1)


    