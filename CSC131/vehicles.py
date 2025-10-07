class Vehicle:
    def __init__(self, year, make, model):
        self.year = year
        self.make = make
        self.model = model 
        self.engine = None

    def __str__(self):
        return f"Year: {self.year}\nMake: {self.make}\nModel: {self.model}\nEngine: {self.engine}"

class DodgeRam(Vehicle):
    make = "Dodge"
    model = "Ram"

    def __init__(self, name, year):
        super().__init__(year, DodgeRam.make, DodgeRam.model)
        self.name = name

    def __str__(self):
        return f"Name: {self.name}\n{super().__str__()}"

class Engine:
    def __init__(self, kind=None):
        self.kind = kind

#main
dr = DodgeRam("Bob", 2020)
print(dr)