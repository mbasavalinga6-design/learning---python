    # Inheritance --------
class Person:
    def __init__(self, name):
        self.name = name

    def role(self):
        print("I am a person")

class Student(Person):
    def role(self):
        print("I am a student")

class Teacher(Person):
    def role(self):
        print("I am a teacher")


# Polymorphism --------
people = [Student("Basava"), Teacher("Ravi"), Person("Guest")]

for p in people:
    p.role()
