"""
в файле hero1 добавить следующий функционал
        - добавить несколько классов других героев унаследовав их от Hero.
        - Каждому герою добавить уникальное свойство-спец.очки (мана, ярость, и т.п. ) и 
                и свойство отражающее урон от спец.атаки.
        - Создать метод атаки special_attack которая возможна только если количество 
                спец.очков более 0.
        - Добавить метод atack который при атаке с вероятностью 25% будет использовать 
                спец.способность героя если у него остались спец.очки. 
                При спец атаке вычитать из очков 1. Если вероятность пришлась на
                остальные 75% - выполнить обычную атаку. Вывести сообщение в консоль 
                о типе и результате атаки.

добавить класс Arena:
        - атрибут warriors - все воины на арене (тип list)
        - магический метод __init__, который принимает необязательный аргумент warriors.
                Если был передан список warriors, та заполняет им атрибут. Если нет, то заполняет
                пустым списком.
        - метод add_warrior, который принимает аргумент warrior и добавляет его к warriors.
                Если данный воин уже есть в списке, то бросить исключение ValueError("Воин уже на арене").
                Если нет, то добавить воина к списку warriors и вывести сообщение на экран
                "{warrior.name} участвует в битве"
        - метод choose_warrior, который не принимает аргументов и возвращает случайного
                воина из warriors
        - метод battle, который не принимает аргументов и симулирует битву. Сперва 
                должна пройти проверка, что воинов на арене больше 1. Если меньше, то бросить
                исключение ValueError("Количество воинов на арене должно быть больше 1").
                Битва продолжается, пока на арене не останется только один воин. Сперва
                в случайном порядке выбираются атакующий и защищающийся. Атакующий ударяет
                защищающегося. Если у защищающегося осталось 0 health_points, то удалить его
                из списка воинов и вывести на экран сообщение "{defender.name} пал в битве".
                Когда останется только один воин, то вывести сообщение "Победил воин: {winner.name}".
                Вернуть данного воина из метода battle.
                
                
Создать несколько воинов используя разные классы, добавить их на арену и запустить битву. 
Выжить должен только один.

"""
import random

class Spell:
    def __init__(self, name, dang=10, mana=5, type=1) -> None:
        self.name = name

class Hero:
    """     
    Класс дял создания героя 
    
     ...

    Attributes
    ----------
    name : str
        Имя героя
    health : int
        здоровье героя 
    age : int
        age of the person

    Methods
    -------
    print_info():
        Печатает в консоль информацию о герое
    
    kick():
        производит один удар - высчитывает и уменьшает броню и здоровье 
    
    """
    #  свойства класса - каждый созданный объект будет их иметь по умолчанию
    option1 = True
    points = 0
    level = 1

    # конструктор - тут мы создаем свойства которые должны быть у каждого нового объекта
    # и присылаем сюда первоначальные их значения
    def __init__(self, name, health, armor, strong, special_points, special_damage) -> None:
        # свойства объектов
        self.name = name
        self.health = health
        self.armor = armor
        self.strong = strong
        self.special_points = special_points
        self.special_damage = special_damage
    
    # методы - это действия/команды которые могут выполнять объекты
    def _get_info(self):
        print(
              f"Имя {self.name}\n" \
              f"Здоровье - {self.health}\n" \
              f"Защита {self.armor}"
        )
        
    def print_info(self):
        
        print(self._get_info() + '\n')
    
    def kick(self, other):        
        other.armor -= self.strong
        if other.armor < 0:
            other.health += other.armor
            other.armor = 0
            

class Mag(Hero):    
    def __init__(self, name, health, armor, strong, special_points, special_damage, mana, spells) -> None:
        # Hero.__init__(self, name, health, armor, strong)
        super().__init__(name, health, armor, strong, special_points, special_damage)
        self.mana = mana
        self.spells = spells
        self.base_spell = fireball
        


    def cast_spell(self):
        print(self.base_spell)
    

    def print_info(self, sep="-"):
        info =  f"{super()._get_info()}\n"  \
                f"{sep*20}\n" \
                f"Мана - {self.mana}\n"
        print(info)


class Knight(Hero):
    def __init__(self, name, health, armor, strong, special_points, special_damage ) -> None:
        super().__init__(name, health, armor, strong, special_points, special_damage)

# новый класс ЛУЧНИКИ со свойством ЛОВКОСТЬ
class Archer(Hero):

    def __init__(self, name, health, armor, strong, special_points, special_damage, agility) -> None:
        super().__init__(name, health, armor, strong, special_points, special_damage)
        self.agility = agility

    def special_attack(self, other):
        if self.special_points > 0:
            self.special_points -= 1
            other.health -= self.special_damage
            print(f'{self.name} использует ловкость и наносит специальный урон {self.special_damage} {other.name}')
        else:
            print(f'{self.name} не может использовать специальную атаку, так как нет ярости.')

    def attack(self, other):
        if random.random() <= 0.25 and self.special_points > 0:
            self.special_attack(other)
        else:
            self.kick(other)


#новый класс БАРБАРИАН со свойством ЯРОСТЬ
class Barbarian(Hero):
    def __init__(self, name, health, armor, strong, special_points, special_damage, rage) -> None:
        super().__init__(name, health, armor, strong, special_points, special_damage)
        self.rage = rage

    def special_attack(self, other):
        if self.special_points > 0:
            self.special_points -= 1
            other.health -= self.special_damage
            print(f'{self.name} использует ярость и наносит специальный урон {self.special_damage} {other.name}')
        else:
            print(f'{self.name} не может использовать специальную атаку, так как нет ярости.')

    def attack(self, other):
        if random.random() <= 0.25 and self.special_points > 0:
            self.special_attack(other)
        else:
            self.kick(other)

class Arena:
    def __init__(self, warriors = None) -> None:
        if warriors is None:
            self.warriors = []
        else:
            self.warriors = warriors

    def add_warrior(self, warrior):
        if warrior in self.warriors:
            raise ValueError("Воин уже на арене")
        else:
            self.warriors.append(warrior)
            print(f"{warrior.name} участвует в битве")

    def choose_warrior(self):
        return random.choice(self.warriors)
    
    def battle(self):
        if len(self.warriors) < 2:
            raise ValueError("Количество воинов на арене должно быть больше 1")

        while len(self.warriors) > 1:
            attacker = self.choose_warrior()
            defender = self.choose_warrior()

            while defender == attacker:  
                defender = self.choose_warrior()

            print(f"{attacker.name} атакует {defender.name}")

        
            defender.kick(attacker)

            if defender.health <= 0:
                self.warriors.remove(defender)
                print(f"{defender.name} пал в битве")

        winner = self.warriors[0]
        print(f"Победил воин: {winner.name}")
        return winner


fireball = Spell('Fireball')        

hero1 = Hero('Dimitri', 50, 20, 15, 25, 30)    
hero2 = Hero('Alex', 60, 10, 5, 25, 25)    
hero3 = Mag('Gendalf', 30, 25, 10, 30, 25, 25, [fireball])    
print(hero3.base_spell.name)
hero3.print_info()

print(hero3.mana)


archer = Archer('Legolas', 40, 15, 20, 15, 25, agility=30)

barbarian = Barbarian('Conan', 70, 5, 25, 10, 30, rage=20)


arena = Arena()
arena.add_warrior(hero1)
arena.add_warrior(hero2)
arena.add_warrior(hero3)
arena.add_warrior(archer)
arena.add_warrior(barbarian)


arena.battle()