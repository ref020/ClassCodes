##########################################################################
# author:   Ray Favaza
# date:    12/09/22
# desc:   A program to create a table of the number of ttimes a certain digit appears as the first and last digit of numbers in a list
#########################################################################
from random import randint, seed
SHOWLIST = False 	# a boolean to determine whether to show the list
MIN = 0			# the smallest random number that can be created.
MAX = 1000		# the largest random number that can be created.

# A function that prompts the user for two pieces of information i.e.
# the size of the list they want to create, and the seed that will be
# used for the list creation. It then returns both pieces of information to the
# calling statement.
def createInfo():
    size = int(input("How big a list do you want to create? "))
    key = int(input("What seed should be used for it's creation? "))
    return size, key
# A function that prints out a list. It receives two pieces of data. The
# first is a string representing the name of the list. The second is a
# list containing all the relevant data. It proceeds to print out the
# name, and then all the elements of the data separated using a tab
# space. Both the name and the entire list are printed on a single line.
def printResults(listName, list):
    print(f"{listName}\t{list[0]}\t{list[1]}\t{list[2]}\t{list[3]}\t{list[4]}\t{list[5]}\t{list[6]}\t{list[7]}\t{list[8]}\t{list[9]}")
# A function that creates the list of random numbers. It receives two
# arguments: one for the size of list to be created, and another for the
# seed that will be used to create the list. The function creates the
# list using the global variables MIN and MAX to form a bound for the
# kinds of numbers that are added to the list. The list is then returned
# to the calling statement.
def createList(length, seedKey):
    list = []
    seed(seedKey)
    for i in range(length):
        list.append(randint(MIN, MAX))
    return list

# A function that recieves a list of numbers and returns another list
# containing the frequency of the lists Most Significant Digits (MSD). The
# list created by the function has 10 elements with each value
# corresponding to a different possible MSD i.e. the value in index 0
# shows the number of values in the original number list that have 0 as
# their most significant digit; the value in index 1 shows the number of
# values with 1 as their MSD; and so on and so forth. This 10 element
# list is returned to the calling statemet.
def findMostSigDig(list):
    mostSigDigList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range (len(list)):
        n = list[i]
        while n >= 10:
            n = n // 10
        mostSigDigList[n] += 1
    return mostSigDigList
# Similar to the function above, a function that recieves a list of
# numbers, and returns another list of 10 elements where each element
# represents the frequency of a specific Least Significant Digit in the
# original list.
def findLeastSigDig(list):
    leastSigDigList = [0,0,0,0,0,0,0,0,0,0]
    for x in range(len(list)):
        n = list[x]
        n = float(n / 10)
        n = str(n)
        n.split(".")
        n = n[len(n)-1]
        n = int(n)
        leastSigDigList[n] += 1
    return leastSigDigList
###################################### MAIN ############################
# using the functions defined above:
#   prompt the user for the size of the list to be created as well as the seed.
size, key = createInfo()
#   create the list of random numbers
randList = createList(size, key)
#   If SHOWLIST is selected, print out the list of numbers
if SHOWLIST == True: 
    print("Original List:")
    print(randList)
    print("-"*54)
#   print the head of the table which just shows the numbers 0-9
print("\t 0 \t 1 \t 2 \t 3 \t 4 \t 5 \t 6 \t 7 \t 8 \t 9 ")
print("-"*54)
#   Calculate the MSD and LSD, and print out their statistics.
printResults("MSD", findMostSigDig(randList))
printResults("LSD", findLeastSigDig(randList))