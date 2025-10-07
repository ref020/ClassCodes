class dog:
    kind = 'pup'

    def __init__(self, dogName):
        self.name = dogName
        self.age = 0
        
#accessor(getter)
    @property
    def age(self):
        return self._age

#Mutator(setter)
    @age.setter
    def age(self, age):
        if age >= 0:
            self._age = age

d1 = dog("Dixie")
d1.age  = -5
print(d1.name)
print(d1.age)

#Order of execution
# 19, 4, 5, 6, 15, 16, 17, 20, 15, 16, 21, 22, 10, 11
