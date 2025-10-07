####################################################################
# author: Ray Favaza
# date: 10/31/22
# description: point of sale
####################################################################

# A function to print out the introduction to the program. It does not
# take any arguments or return any results.
def intro():
    print("-" * 60)
    print("Welcome to Cyber Groceries")
    print("-" * 60)
# A function that prompts the user for the number of items that the
# customer is buying. It does not take any arguments but it returns the
# number of items being bought to the calling statement.
def itemNumber():
    return int(input("How many items is the customer buying? "))
# A function that creates a list of item names by repeatedly prompting
# the user for product names. It takes an argument representing the
# number of items, and returns a single list containing the product
# names.
def items(number):
    list = []
    n = 1
    while len(list) < number:
        list.append(input(f"What is item number {n}? "))
        n +=1
    return list
# A function that creates a list of prices by repeatedly prompting the
# user for the prices for different products. It takes the list of
# product names as a single argument, and then returns a single list
# containing the prices for each of the products.
def prices(itemList):
    i = 0
    price = []
    while i < len(itemList):
        price.append(float(input(f"What is the price of {itemList[i]}? ")))
        i += 1
    return price
######################### MAIN #####################################
# In the space below, use the functions defined above to solve the
# outlined problem.
####################################################################

# print out the introduction
intro()
# Prompt the user for the appropriate information
numItems = itemNumber()
# Print out items and their costs.
groceryList = items(numItems)
priceList = prices(groceryList)
print("-" * 60)
print(groceryList)
print(priceList)
print("-" * 60)
# Figure out what the cheapest and most expensive items are as well as
# what the total cost would be.

#Find the cheapest item
least = priceList.index(min(priceList))   
cheapest = groceryList[least]
#Find the most expensive item
most = priceList.index(max(priceList))
expensive = groceryList[most]
#Find the total
total = round(sum(priceList),2)
# Print out the information on cheapest, most expensive and total cost.
print(f"The cheapest item is {cheapest}")
print(f"The most expensive item is {expensive}")
print(f"The total cost is {total}")
print("=" * 60)