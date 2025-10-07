####################################################################
# author: Ray Favaza
# date: 11/5/22
# description: A program to show store records
####################################################################

# A function to print out the introduction to the program. It does not
# take any arguments or return any results.
def intro():
    print("-" * 60)
    print("Welcome to Cyber Groceries")
    print("-" * 60)
# A function that prompts the user for the number of items that the
# store carries. It does not take any arguments but it returns the
# number of items to the calling statement.
def stock():
    return int(input("How many items does the store carry? "))
# A function that creates a list of item names by repeatedly prompting
# the user for item names. It takes an argument representing the
# number of items, and returns a single list containing the item
# names.
def itemList(number):
    list = []
    n = 1
    while len(list) < number:
        list.append(input(f"What is item number {n}? "))
        n +=1
    return list
# A function that creates a list of prices by repeatedly prompting the
# user for the prices for different items. It takes the list of
# item names as a single argument, and then returns a single list
# containing the prices for each of the items.
def prices(itemList):
    price = []
    for i in range(0, len(itemList)):
        price.append(float(input(f"What is the price of {itemList[i]}? ")))
        i += 1
    return price
# A function that creates a list that contains the number of units that
# were sold of each of the items in the store. It takes a single
# argument i.e. the list of item names, and after repeatedly asking the
# user for item amounts, returns the list of item units that were sold.
def quantities(itemList):
    sales = []
    for s in range(0, len(itemList)):
        sales.append(float(input(f"How many units of {itemList[s]} were sold today? ")))
        s += 1
    return sales
# A function that prints out the summary table. It takes 3 arguments
# i.e. the list containing the item names, the list containing the item
# prices, and the list containing the item amounts. It uses these 3
# arguments to create a 4 column table that contains the name, unit
# price, number of units sold, and total amount made from that unit for
# each item. It does not return any arguments.
def table(itemNames, itemPrices, itemAmmounts):
    print("-" * 60)
    print("Item Names \t Unit Price \t Number \t Total Cost")
    print("-" * 60)
    for f in range(0, len(itemNames)):
        print(f"{itemNames[f]}\t\t${itemPrices[f]:.2f}\t\t{itemAmmounts[f]}\t\t${(itemPrices[f])*(itemAmmounts[f]):.2f}")
    print("=" * 60)
######################### MAIN #####################################
# In the space below, use the functions defined above to solve the
# outlined problem.
####################################################################

# print out the introduction
intro()
# Prompt the user for the appropriate information
n = stock()
stockList = itemList(n)
prices = prices(stockList)
saleAmmount = quantities(stockList)
# Print out items and their costs.
table(stockList, prices, saleAmmount)