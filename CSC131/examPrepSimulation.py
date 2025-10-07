######################################################################
# author:   
# date:    
# desc:   
#####################################################################
from random import *

DEBUG = False   # Activate intermediate output 
def sim(b,q,s):
    #question numbers
    qList = sample(range(1, b+1), k=q)
    #questions studied
    sList = sample(range(1, len(qList)+1), k=s)
    
    #questions passed
    pList = []
    for i in range(0, q):
        if qList[i] in sList:
            pList.insert(1, qList[i])

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


for i in range(1, simNum+1):
        qList, sList, pList, score = sim(numQ,lenTest,studied)
        if DEBUG == True:
            print ("-"*60)
            print (f"Simulation No. {i}")
            print (f"Questions you were asked: {qList}")
            print (f"Questions you studied: {sList}")
            print (f"Questions you passed: {pList}")
            print (f"Which means you scored {score}/{qList}")
        scoreList = []
        scoreList.append(score)

counter = 0
for i in scoreList:
    if i >= pctPass:
        counter += 1
    
passRate = (counter/simNum) * 100

print(f"You passed the test {passRate}% of the time")

