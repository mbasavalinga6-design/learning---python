# ---Encapsulation
class Student:
    def __init__(self, name, age):
        self.name = name
        self._age = age   # protected variable

    def get_age(self):
        return self._age

    def set_age(self, age):
        if age > 0:
            self._age = age
        else:
            print("Invalid age")

    def display(self):
        print("Name:", self.name)
        print("Age:", self._age)


s1 = Student("Basava", 20)
s1.display()
s1.set_age(22)
print("Updated Age:", s1.get_age())


# ---Abstraction
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def area(self):
        return 4 * 4

sq = Square()
print("Square Area:", sq.area())
