#######################################################################
# author:Ray Favaza
# date: 12/5/22
# desc:How Many Primes
########################################################################
5
# A function to prompt the user for a number and return that value to
# the calling statement.
def askNumber():
    lim = int(input("What limit are you interested in? "))
    return lim

# A function that receives a number and tests that number to see whether
# it is prime or not. It returns the boolean response to the calling
# statement.
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

################### MAIN ######################################
# Using the functions declared above, ask the user for a number, then
# create a list of all the prime numbers less than that number. Proceed
# to print out the relevant information related to that list.

#ask for the limit of the program
num = askNumber()

#Count up to the limit
primes = []
for i in range(0,num):
    f = isPrime(i)
    if f == False:
        primes.append(i)


#print the output
print(f"There are {len(primes)} primes less than {num}")
print(primes)