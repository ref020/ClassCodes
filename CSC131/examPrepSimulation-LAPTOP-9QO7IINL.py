######################################################################
# author:   
# date:    
# desc:   
#####################################################################
from random import *

DEBUG = True   # Activate intermediate output 
def sim(q,s):
    #number of questions
    qList = [] * q
    #question numbers
    for i in range(len(qList)):
        qList[i] = i + 1
    #questions studied
    sList = [] * s
    for i in range (0,s):
        x = randint(0,len(qList)-1)
        sList[i] = qList[x]
    
    #questions passed
    pList = []
    for i in range(len(sList)):
        if i in sList and i in qList:
            pList.apppend(i)

    #get score
    score = len(pList)

    #return to the calling statement
    return qList, sList, pList, score  

print("Simulation Set Up:")
print("="*60)
numQ = int(input("What is the size of the question bank? "))
studied = int(input("How many of those questions have you studied? "))
lenTest = int(input("How many questions does the test have? "))
pctPass = int(input("How many questions must you answer correctly to pass the test? "))
print("="*60)
simNum = int(input("How many simulations do you want to run? "))


for i in range(1, simNum):
        qList, sList, pList, score = sim(numQ,studied)
        if DEBUG == True:
            print ("-"*60)
            print (f"Simulation No. {i}")
            print (f"Questions you were asked: {qList}")
            print (f"Questions you studied: {sList}")
            print (f"Questions you passed: {pList}")
            print (f"Which means you scored {score}/10")

