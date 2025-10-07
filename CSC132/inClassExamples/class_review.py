#inheritance
#child class inherits the state and behavior of parent calss
#state:what is the class (instance variables)
#behavior: what can the class do (Functions)
#"child" is a "parent" relationship

#first box is the class name
#second box tells you the instance variables
#third box tells you the behaviors/Functions

class Vehicle: 
    def __init__(self, name):
        self.tires = None
        self.engine = None
        self.owner = name

    def __str__(self):
        return f"owner = {self.owner}, tires = {self.tires}, engine = {self.engine}"
    
class Car(Vehicle):
    def __init__(self, name):
        super().__init__(name)
        self.tires = 4
        self.engine = True

    def __str__(self):
        return "Car; " + super().__str__()
    
class Cycle(Vehicle):
    def __init__(self, name):
        super().__init__(name)
        self.tires = 2

    def __str__(self):
        return super().__str__()
        
class Bicycle(Cycle):
    def __init__(self, name):
        super().__init__(name)
        self.engine = False

    def __str__(self):
        return "Bicycle; " + super().__str__()
        
class Motorcycle(Cycle):
    def __init__(self, name):
        super().__init__(name)
        self.engine = True

    def __str__(self):
        return "Motorcycle; " + super().__str__()
        

c1 = Car("ray")
b1 = Bicycle("ray")
m1 = Motorcycle("ray")

print(c1)
print(b1)
print(m1)