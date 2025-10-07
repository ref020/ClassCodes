def fib(x):
    if (x==1):
        return 0
    elif (x==2):
        return 1
    else:
        return fib(x-1) + fib(x-2)


x=10
print(f"fib({x})={fib(x)}")
