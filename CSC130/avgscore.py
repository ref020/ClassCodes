#functions
def name():
    user = input("Please enter your name: ")
    return user

def scores():
    score = int(input("Enter your score: "))
    return score

def average(first, second):
    avg = ((first + second)/2)
    return avg

def output(name, average):
    print(f"Hi {name}, your average score is {average}")



#########MAIN##########

name = name()

firstScore = scores()
secondScore = scores()

avgScore = average(firstScore, secondScore)

output(name, avgScore)
