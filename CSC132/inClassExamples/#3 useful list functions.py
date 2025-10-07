#3 useful list functions
from functools import reduce
#filter function
def f(x):
    return x % 3 == 0 or x % 5 == 0

#map function
def m(x):
    return x*x

#reduce
def r(x,y):
    return x*y

#filter
#filter syntax
#list(filter(function, list name))
multiples = list(filter(f, range(3,31)))
print(multiples)

#map
#map syntax
#list(map(function, list name))
squares = list(map(m,range(1,11)))
print(squares)

#reduce
#reduce syntax
#list(reduce(function, list name))
factorial = reduce(r, range(1, 11))
print(factorial)