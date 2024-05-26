"""
Описать абстрактный класс Animal у которого:

- атрибут name - кличка (тип str)
- магический метод __init__, который принимает аргумент name
- абстрактный метод says, который не принимает аргументов

На основе Animal определить классы Cat, Dog, Cow, которые переопределят метод
says таким образом, чтобы он возвращал строку вида:

- "{кличка} - кошка. Говорит МЯУ!" для класса Cat
- "{кличка} - собака. Говорит ГАВ!" для класса Dog
- "{кличка} - корова. Говорит МУ!" для класса Cow
"""
from abc import ABC, abstractmethod

class Animal:
    name : str
    def __init__(self, name) -> None:
        self.name = name

    @abstractmethod
    def says():
        pass

class Cat(Animal):
    def says(self):
        return f"{self.name} - кошка. Говорит МЯУ!"
    
class Dog(Animal):
    def says(self):
        return f"{self.name} - собака. Говорит ГАВ!"
    
class Cow(Animal):
    def says(self):
        return f"{self.name} - корова. Говорит МУ!"
    
cat = Cat("Барсик")
dog = Dog("Рекс")
cow = Cow("Мурка")

print(cat.says()) 
print(dog.says()) 
print(cow.says())
    

