#####################################################################
# author:       
# date:         
# description:  
#####################################################################

# import the abc library to make abstract classes
from abc import ABC, abstractmethod

######################################################################
# An employee class. Its constructor takes the first name, last name and
# pay. It also has email and position as instance variables. It contains
# a single abstract method i.e. applyRaise, and a createEmail function
# that creates an appropriate email address from the employee's first
# and last names.
######################################################################
class Employee:
    def __init__(self, firstname, lastname, pay, position = None):
        self.firstname = firstname
        self.lastname = lastname
        self.pay = pay
        self.email = self.createEmail()
        self.position = position
    
    @property
    def firstname(self):
        return self._firstname
    
    @property
    def lastname(self):
        return self._lastname
    
    @property
    def pay(self):
        return self._pay
    
    @property
    def email(self):
        return self._email
    
    @firstname.setter
    def firstname(self, firstname):
        firstname.replace(" ", "")
        self._firstname = firstname

    @lastname.setter
    def lastname(self, lastname):
        for i in lastname:
            if i == " ":
                lastname.remove(i)
                print(lastname)
        self._lastname = lastname

    @pay.setter
    def pay(self, pay):
        if pay < 20000:
            self._pay = 20000
        else:
            self._pay = pay
    
    @email.setter
    def email(self, email):
        if "@latech.edu" not in email:
            self.createEmail()
        else:
            self._email = email

    def createEmail(self):
        return f"{self.firstname.lower()}.{self.lastname.lower()}@latech.edu"
    
    @abstractmethod
    def applyRaise(self, rate):
        raise NotImplementedError
    
    def __str__(self):
        return f"{self.lastname}, {self.firstname} ({self.email})"

######################################################################
# A faculty class is a subclass of the Employee class above. Its
# constructor receives both names as well as the position. The Faculty
# class also overrides the applyRaise function by multiplying the pay by
# the rate provided as an argument. It also slightly tweaks the __str__
# function in the super class.
######################################################################
class Faculty(Employee):
    def __init__(self, firstname, lastname, position, pay = 50000):
        super().__init__(self, firstname, lastname, pay)
        self.position = position
    
    def applyRaise(self, rate):
        if rate > 0:
            self.pay = self.pay * rate
        else:
            self.pay = self.pay
        
    def __str__(self):
        return f"{self.lastname}, {self.firstname} ({self.email}) - {self.position}"

######################################################################
# A Staff class is a subclass of the Employee class above. Its
# constructor only receives both names. It also overrides the applyraise
# function but adding the increase (provided as the argument) to the
# pay. It doesn't change anything else from the Employee class.
######################################################################


