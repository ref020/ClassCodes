def candy(x):
    y = x % 2
    if y == 0:
        return y
    else:
        return x

def magic():
    return 3

def display(x):
    print(x)

number = candy(0) + 1
amount = candy(number)
quantity = magic() + candy(amount + 1)
display(quantity)
