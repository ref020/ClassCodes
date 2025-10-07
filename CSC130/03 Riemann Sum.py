####################################################################
# author:Ray Favaza
# date: 10/10/2022
# description: reimann sum
####################################################################

# A function that is in charge of prompting the user for any input they
# give. It receives an argument representing the required data, prompts
# the user for that data, and then returns it to the calling statement.
def limits (data):
    return (input(f"What is the value of \"{data}\":"))
# A function that is in charge of printing out the introductory
# statement(s) for the program.
def introduction():
    print("This progrram will calculate the integral of the function f(x) = 3x^3 - 2x^2 between user defined limits: a and b")
# A function that prints out the statement about the accuracy of delta.
def accuracy():
    print("The accuracy of this calculation depends on the value of delta that you use.")
    
# A function to evaluate the given mathematical formula at a given
# point. It takes a numerical argument that represents x, and returns
# the result of f(x).
def f(x):
    y = float((3*(x**3))-(2*(x**2)))
    return y
# A function that calculates an approximation of the integral of f(x)
# using the riemann sum. It takes three arguments that represent the
# lower limit, the upper limit, and the delta value. It then returns the
# integral approximation as a result to the calling statement.
def reimann(a, b, d):
    i = 0
    while (a < b):
        i += f(a)
        a += d
    return d * i
########################### MAIN ##################################
# In the space below, use the functions defined above to solve the
# problem.
###################################################################

# Print the introductory statements of the program
intro = introduction()
# Prompt the user for both the lower and upper limits
a , b = int(limits("a")), int(limits("b"))

# Print the statements about delta
accuracy = accuracy()
# Promt the user for the delta value
delta = float(limits("delta"))
# Calculate the integral approximation
Area = reimann(a, b, delta)
# Print out the result.
print(Area)