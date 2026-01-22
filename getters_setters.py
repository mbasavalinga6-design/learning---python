#  Getters and Setters

class Employee:
    def __init__(self, name, salary):
        self._name = name        # protected variable
        self._salary = salary

    # Getter
    def get_salary(self):
        return self._salary

    # Setter
    def set_salary(self, salary):
        if salary > 0:
            self._salary = salary
        else:
            print("Invalid salary")

    def display(self):
        print("Name:", self._name)
        print("Salary:", self._salary)


emp = Employee("Basava", 25000)
emp.display()

emp.set_salary(30000)
print("Updated Salary:", emp.get_salary())
