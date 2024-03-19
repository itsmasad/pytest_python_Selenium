# Inheritance

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showData(self):
        print(f'Emplyee name is {self.name} and id is {self.id}')

e1 = Employee("Asad",200)
e1.showData()
e2 = Employee("Naveed",199)
e2.showData()
