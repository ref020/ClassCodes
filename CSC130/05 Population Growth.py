##########################################################################
# name: Ray Favaza
# date: 10/26/22
# description: A code to create a table of population changes
#########################################################################

# A function that prints out the introduction to the program. It doesn't
# take any arguments and does not return any results.
def intro():
    print("This program will compare the populations of two different countries over time")
# A function that prompts the user for the name of the country. It takes
# in a number that is used in the prompt as an argument. It then returns
# the name of the country.
def countries(n):
    return input(f"What is the name of Country #{n}: ")
# A function that prompts the user for the current population of a
# country. It takes the name of the country as an argument, and then
# returns the resulting population. The function also carries out range
# checking to make sure the value inputed by the user is valid (i.e. not
# negative)
def population(c):
    i = int(input(f"What is the current population of {c}? "))
    if i > 0:
        return i
    else:
        print("That doesn't seem right. Please enter a positive number")
        population(c)
# A function that prompts the user for the population growth rate of a
# country. It takes in the name of the country as an argument and then
# returns a value growth rate. It also carries out range checking to
# make sure that the result is not an unrealistic growth rate i.e. rate
# should be between -5 and 10 inclusive.
def growthRate(c):
    g = float(input(f"What is the annual population growth rate of {c}? "))
    if (g < -5.0 ):
        print("That doesn't seem right. Please enter a value in the range [-5,10] ")
        growthRate(c)
    elif g > 10.0:
        print("That doesn't seem right. Please enter a value in the range [-5,10] ")
        growthRate(c)
    else:
        return g
# A function that prompts the user for the number of years to show in
# the resulting table. The function doesn't take any arguments but
# returns a result. It is also in charge of range checking to make sure
# that the number of years is not less than 1.
def years():
    t = int(input("How many years of comparison should the table show? "))
    if t < 1:
        print("That doesn't seem right. Please enter a value >= 1")
        years()
    else:
        return t
# A function that prompts the user for the duration of the interval in
# the table i.e. how many years between each successive row of the
# resulting table. It doesn't take any arguments and does range checking
# to make sure that the user doesn't enter a value less than 1.
def interval():
    r = int(input("How many years should the intervals be? "))
    if r < 1:
        print("That doesn't seem right. Please enter a value >= 1")
        years()
    else:
        return r
# A function that calculates the population given an intial population,
# a growth rate, and the time. It takes 3 arguments (population, growth
# rate and time) and returns the resulting population.
def calc(p, r, t):
    return  p * (1+(r/100))**t
# A function to print out the header of the table. It takes two
# arguments i.e. the country names, and then prints out the formatting
# lines as well as the first row seen at the top of the table.
def header(c1, c2):
    print("-----------------------------------------------")
    print(f"Years \t {c1} \t {c2}")
    print("-----------------------------------------------")
    print(f"0\t{popC1:,}\t{popC2:,}")
# A function to print out the rest of the table row by row. It receives
# 6 arguments: both country populations, both country rates, the
# duration of the analysis and the interval between each row. It then
# relies on calculate population function to calculate the population
# values for each row and print them out in order.
def table(population1, population2, rate1, rate2, duration, interval):
    header(country1, country2)
    i = 0 + interval
    while i <= duration:
        r1 = calc(population1, rate1, i)
        r2 = calc(population2, rate2, i)
        r1 = int(r1)
        r2 = int(r2)
        print (f"{i}\t{r1:,}\t{r2:,}")
        i += interval
    print("-----------------------------------------------")
############### MAIN ##################################
# print the introduction
intro()
# Get the country names
country1 = countries(1)
country2 = countries(2)
# Get the country initial populations
popC1 = population(country1)
popC2 = population(country2)
# get the country population growth rates
growth1 = growthRate(country1)
growth2 = growthRate(country2)
# get the analysis detais e.g. the duration and the interval
time = years()
gaps = interval()
# Print out the table
table(popC1, popC2, growth1, growth2, time, gaps)