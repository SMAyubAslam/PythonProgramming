class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def showDetails(self):
        print(f'Employee id is {self.id} and name is {self.name}')

class Programmer(Employee):
    def showlanguage(self):
        print(f"{self.name} is expert in pyhton")

e1 = Employee('Ayub', 243)
e2 = Programmer('Salika', 254)
e1.showDetails()
e2.showDetails()
e2.showlanguage()