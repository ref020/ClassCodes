####################################################################
# name: Ray Favaza
# date: 10/3/22
# description: annual compound interest
####################################################################

# A function that receives no arguments, prompts the user for their
# name, and returns that value to the calling statement.
def getName():
    name = str(input("Please enter your name: "))
    return name

# A function that receives a single argument (a string that describes a
# piece of data), prompts the user for that data, and then returns the
# data to the calling statement.
def getData(P, r, t):
    data = str("Please enter the")
    P = float(input(getData("principle")))
    r = float(input(getData("percentage rate")))
    t = float(input(getData("years")))
# A function that receives three arguments that represent the principal
# amount, annual compound interest rate, and the number of years, and
# returns the total amount after compound interest growth.
def interest(P, r, t):
    A = float(P*(1+(r/100)**t))
    return A

###################### MAIN #########################
# using the function(s) above as appropriate, complete the algorithm
# below.

# prompt the user for their name
name = getName()
# prompt the user for the principal amount, annual compound interest
# rate, and number of years
getData = getData(P)

# Calculate the total amount
A = interest(P, r, t)
# Print out the final amount
print(f"Hello {name}, the final amount after {t} years at {r}% is ${A}")