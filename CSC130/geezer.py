
while (1==1):
    
    name = input("What's your name?")
    score = int(input("What was the score you got on the test?"))

    if (score > 100):
        print("How did you get above 100%? Did you cheat?")
    elif (score >= 90):
        print(f"Well, {name}, with a score of {score}, you got an A.")
    elif (score >= 80):
        print(f"Well, {name}, with a score of {score}, you got an B.")
    elif (score >= 70):
        print(f"Well, {name}, with a score of {score}, you got an C.")
    elif (score >= 60):
        print(f"Well, {name}, with a score of {score}, you got an D.")
    else:
        print(f"Wow, {name}, a score of {score} means you failed with a grade of F.")
