class point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    #x accessor(getter)
    @property
    def x(self):
        return self._x

    #y accessor(getter)
    @property
    def y(self):
        return self._y

    #x Mutator(setter)
    @x.setter
    def x(self, x):
        if (x >= 10):
            self._x = 10
        elif (x <= -10):
            self._x = -10
        else:
            self._x = x
    
    #y Mutator(setter)
    @y.setter
    def y(self, y):
        if (y >= 10):
            self._y = 10
        elif (y <= -10):
            self._y = -10
        else:
            self._y = y


p1 = point(5,5)
p2 = point(50,-50)

print(f"P1 = ({p1.x}, {p1.y})")
print(f"P2 = ({p2.x}, {p2.y})")