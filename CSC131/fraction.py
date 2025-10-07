class fraction:
    def __init__(self, num = 0, den = 1):
        self.num = num
        if (den == 0):
            den = 1
        self.den = den
    
    @property
    def num(self):
        return self._num
    
    @property
    def den(self):
        return self._den

    @num.setter
    def num(self, value):
        self._num = value

    @den.setter
    def den(self, value):
        if (value != 0):
            self._den = value
    #addition
    def __add__(self, other):
        num = (self.num * other.den) + (other.num * self.den)
        den = self.den * other.den
        sum = fraction(num, den)
        sum.reduce()
        return sum
    #subtraction
    def __sub__(self, other):
        num = (self.num * other.den) - (other.num * self.den)
        den = self.den * other.den
        sum = fraction(num, den)
        sum.reduce()
        return sum

    #multiplication
    def __mul__(self, other):
        num = self.num * other.num
        den = self.den * other.den
        prod = fraction(num, den)
        prod.reduce()
        return prod
    
    #division
    def __truediv__(self, other):
        num = self.num * other.den
        den = self.den * other.num
        quot = fraction(num, den)
        quot.reduce()
        return quot
    
    #reduce the fraction
    def reduce(self):
        gcd = 1
        minimum = min(abs(self.num), abs(self.den))

        # find common divisors
        for i in range(2, int(minimum+1)):
            if(self.num % i == 0 and self.den % i == 0):
                gcd = i

        # divide numerator and denominator by the GCD
        self.num /= gcd
        self.den /= gcd
       
        # if the numerator is 0, set denominator to 1
        if(self.num == 0):
            self.den = 1


    def getReal(self):
        return float(self.num) / self.den

    def __str__(self):
        self.reduce()
        return (f"{self.num}/{self.den} ({self.getReal()})")



f1 = fraction(3, 12)
f2 = fraction(5, 7)
f3 = f1 + f2
f4 = f2 - f1
f5 = f1 * f2
f6 = f2 / f1
print(f1)
print(f2)
print(f3)
print(f4)
print(f5)
print(f6)