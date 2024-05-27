"""
Создать класс BookCard, в классе должны быть:

- private атрибут author - автор (тип str)
- private атрибут title - название книги (тип str)
- private атрибут year - год издания (тип int)
- магический метод __init__, который принимает author, title, year
- магические методы сравнения для сортировки книг по году издания
- сеттеры и геттеры к атрибутам author, title, year. В сеттерах сделать проверку
  на тип данных, если тип данных не подходит, то бросить ValueError. Для года
  издания дополнительно проверить на валидность (> 0, <= текущего года).

Аксессоры реализоваться через property.
"""

from datetime import date

CURRENT_YEAR = date.today().year

class BookCard:
    __author: str
    __title: str
    __year: int

    def __init__(self, author, title, year) -> None:
        self.author = author
        self.title = title
        self.year = year

    def __eq__(self, other):
        return self.year == other.year

    def __ne__(self, other):
        return self.year != other.year

    def __lt__(self, other):
        return self.year < other.year

    def __le__(self, other):
        return self.year <= other.year

    def __gt__(self, other):
        return self.year > other.year

    def __ge__(self, other):
        return self.year >= other.year

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, val):
        if not isinstance(val, str):
            raise ValueError("Author must be a string")
        self.__author = val

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, val):
        if not isinstance(val, str):
            raise ValueError("Title must be a string")
        self.__title = val

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, val):
        if not isinstance(val, int):
            raise ValueError("Year must be an integer")
        if val <= 0 or val > CURRENT_YEAR:
            raise ValueError(f"Year must be between 1 and {CURRENT_YEAR}")
        self.__year = val


book1 = BookCard("Author A", "Book One", 1995)
book2 = BookCard("Author B", "Book Two", 2001)
book3 = BookCard("Author C", "Book Three", 1987)
book4 = BookCard("Author D", "Book Four", 2001)

books = [book1, book2, book3, book4]


sorted_books = sorted(books)

print("Книги отсортированы по году издания (по возрастанию):")
for book in sorted_books:
    print(f"{book.author} - {book.title} ({book.year})")


sorted_books_desc = sorted(books, reverse=True)

print("\nКниги отсортированы по году издания (по убыванию):")
for book in sorted_books_desc:
    print(f"{book.author} - {book.title} ({book.year})")
