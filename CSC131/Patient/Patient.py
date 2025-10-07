##########################################################################
# name: Ray Favaza
# date: 1/21/23
# desc: A code to make a table of patients and their weights, ages, and time in the hospital
##########################################################################

# A patient class. A patient has a name, age and weight. Only the name
# and age are provided as arguments for the constructor. On top of
# accessors and mutators for those variables, the patient class also has
# an increaseAge function that increases the age by 1.
class Patient:

    # Initialize Patient class
    def __init__(self, name, age):
        self.age = age
        self.name = name
        self.weight = 150

    # Patient class getters and setters
    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @property
    def weight(self):
        return self._weight

    @name.setter
    def name(self, name):
        self._name = name

    @age.setter
    def age(self, age):
        if(age < 0):
            self._age = 0
        else:
            self._age = age

    @weight.setter
    def weight(self, weight):
        if(weight > 1400):
            self._weight = 150
        elif(weight < 0):
            self._weight = 150
        else:
            self._weight = weight

    # Increase age function
    def increaseAge(self):
        self._age += 1


# An In class which is a subclass of the Patient class and refers to an
# in-patient. An in-patient also contains a "stay" instance variable 
# that stores the number of days that that patient will stay in the
# hospital. Its constructor receives the name, age and stay duration as
# arguments. On top of appropriate accessors and mutators, the In class
# also has a __str__ function to define how an In object would be printed.
class In(Patient):

    # Initialize in subclass 
    def __init__(self, name, age, stay):
        super().__init__(name, age)
        self.stay = stay

    # Acessors and mutators for in subclass
    @property
    def stay(self):
        return self._stay

    @stay.setter
    def stay(self, stay):
        if(stay>0):
            self._stay = stay
        else:
            self._stay = 5

    # String magic function for in subclass
    def __str__(self):
        return (f"IN-\t{self.name}\t{self.age}\t{self.weight}\t{self.stay}")

# An Out class, which is a subclass of the Patient class and refers to
# an out-patient. An outpatient receives the name and age as arguments
# to its constructor. It also has a __str__ function that defines how an
# Out object would be printed.
class Out(Patient):

    # Initializer for Out subclass
    def __init__(self, name, age): 
        super().__init__(name, age)

    # String magic function for Out subclass
    def __str__(self):
        return (f"OUT-\t{self.name}\t{self.age}\t{self.weight}")
        
# An ICU class which is a subclass of the In class and refers to a
# patient in the ICU. The ICU class receives the name and age as
# arguments to its constructor. It also has a class variable called days
# with the value 5 stored in it. This class variable is used to
# determine what the stay of the patient will be.
class ICU(In):

    # Class variable days
    days = 5

    # Initializer for ICU subclass
    def __init__(self,name,age, stay = days):
        super().__init__(name, age, stay)
    
# A CheckUp class which is a subclass of the Out class and refers to a
# patient who is getting a checkup at the hospital. It receives the name
# and age as arguments for its constructor.
class CheckUp(Out):

    # Initializer for Checkup subclass
    def __init__(self, name, age):
        super().__init__(name,age)
