def getLetterGrade(num):
    if (num>89):
        return "A"
    elif (num>79):
        return "B"
    elif (num>69):
        return "C"
    elif (num>59):
        return "D"
    else:
        return "F"

##########main###########
for x in range(0,5):
    score = float(input("What is your grade? "))
    letter = getLetterGrade(score)
    print(f"A score of {score} is a/an {letter}")
    
