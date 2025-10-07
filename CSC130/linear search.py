from random import randint

def linSearch(array, key):
    i = 0
    while i < len(array):
        if array[i] == key:
            return i
        i += 1
    return -1

def getMax(array):
    i = 0
    m = i
    while i < len(array):
        if array[i] > array[m]:
            m = i
        i += 1
    return m 


numbers = []
size = int(input("How many numbers do you want in your list"))

while len(numbers) < size:
    num = randint(0, 1000)
    numbers.append(num)

print(f"the list of numbers: {numbers}")


k = int(input("what number are you looking for?"))

pos = linSearch(numbers, k)

maxi = getMax(numbers)

print(f"The number {k} is the {pos} number of the array")
print(f"The largest number is at position {maxi}")
