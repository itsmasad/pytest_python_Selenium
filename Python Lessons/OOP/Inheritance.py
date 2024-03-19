# Inheritance

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showData(self):
        print(f'Emplyee name is {self.name} and id is {self.id}')

# Inheriting everything which Employee have 
class Programmer(Employee):
    def showLanguage(self):
        print('Default language is Python')

# Calling Employee method directly
e1 = Employee("Asad",200)
e1.showData()

# Calling Employee method using Programmer to see if the inheritence is working
e3 = Programmer("Hadi",150)
e3.showData()
e3.showLanguage()