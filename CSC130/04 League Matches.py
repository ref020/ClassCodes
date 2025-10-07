####################################################################
# author:
# date:
# description:
####################################################################

# A function to prompt the user for the number of teams in a league. It
# does not take any arguments and returns the result to the calling
# statement.
def teamsNumber():
    n = int(input("How many teams are in this league? "))
    return n
# A function that calculates the number of matches in a league. It
# receives a single numerical argument representing the number of teams
# in the league, and uses RECURSION to calculate the minimum number of
# matches required. It then returns the result to the calling statement.
def matches(k):
    if(k == 1):
       return 0
    else:
        return (k-1) + matches(k-1)
    

# A function that prints out the final results. It receives two
# arguments that represent the number of teams and matches.
def results(a,b):
    matches(b)
    print(f"A league of {n} teams would require at least {a} matches")
############################ MAIN #################################
# get the number of teams
n = teamsNumber()
# calculate the number of matches
m = matches(n)
# print the results to the screen.
results(matches(n), n)