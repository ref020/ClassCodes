#################################
#Name:
#Date:
#Description:
#################################
import enchant
import tkinter
def isPrime(n):

    notPrime = False
    if n == 2 or n == 3 :
        return False
    elif n==0 or n==1:
        return True
    else:
    # check for factors
        for x in range(2, n):
            #print(f"Checking if {x} is a factor of {n}")
            if (n % x == 0):
                notPrime = True
                break
        return notPrime


################MAIN######################
