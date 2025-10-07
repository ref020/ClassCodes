#############################################################################
# author: Ray Favaza
# date: 9/28/22
# description: 
#############################################################################
while (1==1):
# A statement that prompts the user for their name
    name = input("What is your name?")
# Statements that prompt the user for their annual income and tax rate
    income = int(input(f"Hello {name}, what is your gross annual income?"))
    rate = float(input("What is the percentage tax rate in your location?"))
# Calculate the user's net income
    net = income - (income * (rate/100))
# Display the final output.
    print(f"Well {name}, that means that your net income is ${net}")