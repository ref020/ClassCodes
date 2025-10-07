from random import randint



def magicFunction(array):
    larger = []

    for i in range(0,len(array)):
        if array[i] > 500:
            larger.append(array[i])
    return len(larger)
def getSome(array):
    theSum = 0
    for element in array:
        if (element%2==0) or (element%3==0):
            theSum += element
    return theSum

numbers = []

for i in range(5):
    num = randint(0,1000)
    numbers.append(num)

s = magicFunction(numbers)
u = getSome(numbers)
print(f"there are {s} numbers larger than 500 in {numbers}")
print(f" the sum of all numbers divisible by 3 or divisible by 2 is {u}")
