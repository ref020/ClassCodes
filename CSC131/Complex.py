############################################################################
# name: 
# date:
# description:
###########################################################################

# Don't forget to name this file Complex.py and place it in the same
# folder as the provided ComplexTest.py file so that they can
# automatically find and use each other.

class Complex:
    # A constructor that takes two values for the real and imaginary
    # portions respectively. Default values for both parameters are 0.
        def __init__(self, real = 0, imaginary = 0):
            self.real = real
            self.imaginary = imaginary
    # Accessors and Mutators for the instance variables
        @property
        def real(self):
                return self._real

        @property
        def imaginary(self):
                return self._imaginary

        @real.setter
        def real(self, value):
            self._real = value

        @imaginary.setter
        def imaginary(self, value):
                self._imaginary = value

    # Overloaded mathematical operators i.e. ==, +, -, *, /
        #addition
        def __add__(self, other):
                real = self.real + other.real
                imaginary = self.imaginary + other.imaginary
                sum = Complex(real, imaginary)
                return sum 

        #subtraction
        def __sub__(self, other):
                real = self.real - other.real
                imaginary = self.imaginary - other.imaginary
                difference = Complex(real, imaginary)
                return difference
        
        #multiplication
        def __mul__(self, other):
                real = ((self.real * other.real) - (self.imaginary * other.imaginary))
                imaginary = ((self.real * other.imaginary) + (self.imaginary * other.real))
                product = Complex(real, imaginary)
                return product
        
        #division
        def __truediv__(self, other):
                divReal = ((other.real * self.real) + (other.imaginary * self.imaginary))
                divImaginary = ((other.real * self.imaginary) - (other.imaginary * self.real))
                den = ((other.real ** 2) + (other.imaginary ** 2))
                divReal = divReal/den
                divImaginary = divImaginary/den
                return Complex(divReal, divImaginary)

        #equality
        def __eq__(self, other):
                if (self.real == other.real and self.imaginary == other.imaginary):
                        return True
                else:
                        return False

    # Other functions e.g. reciprocal, conjugate, and __str__
        #reciprocal
        def reciprocal(self):
                recipReal = (self.real /((self.real **2) + (self.imaginary **2)))
                recipImaginary = (self.imaginary /((self.real **2) + (self.imaginary **2)))
                return Complex(recipReal, recipImaginary*-1)

        #conjugate
        def conjugate(self):
                return Complex(self.real, -self.imaginary)

        #string
        def __str__(self):
                imaginarySplit = list(str(self.imaginary))
                
                if ("-" in imaginarySplit):
                        imaginarySplit.remove('-')
                        return f"{self.real} - {''.join(imaginarySplit)}i"
                else:
                        return f"{self.real} + {self.imaginary}i"
                        