#function called get larger that takes two numerical arguments and returns the larger of the two
def getLarger(x,y):
    if (x > y):
        return x
    else:
        return y
#function called get number that asks for two number
def getNumber():
    x = int(input("Enter a number: "))
    return x

#######MAIN########
 
a = getNumber()
b = getNumber() 
c = getLarger(a, b)
#Check if the numbers are the same
if( x == y):
    print("The numbers are the same!!!!")
else:
    print(f"The larger number is {c}")