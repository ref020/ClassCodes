from random import randint
hiddenRoom = True
def winScreen():
    print("you win")

def soClose():
    return str(f"You fall down the chimney due to the weight of the statue. /n *a flash of red* /n HO HO HO")
print('-'*33)
print((((((('|'+ ' '*15+'|'+ ' '*15+'|''\n')*3))+((('|'+ ' '*15+' '*16+'|''\n')*3)))+(((('|'+ ' '*15+'|'+ ' '*15+'|''\n')*3))+('-'*7))+(' '*3))+('-'*7)+('-'*6))+(' '*3)+('-'*7))
print(((((('|'+ ' '*15+'|'+ ' '*15+'|''\n')*3))+((('|'+ ' '*15+' '*16+'|''\n')*3)))+(((('|'+ ' '*15+'|'+ ' '*15+'|''\n')*3))+('-'*17))+('-'*6)+(' '*3)+('-'*7)))
print('The top left room is room 1, the room to its right is room 2. The bottom left room is room 3, the room to its right is room 4')
no = ['no','No','NO','n','N']
desc = "it's made of oak and a golden key rests on top"
secretDeath = soClose()
class Room:
    def __init__(self, name):
    # Constructor
        self.name = name
        self.exits = []
        self.exitLocations = []
        self.items = []
        self.itemDescriptions = []
        self.grabbables = []
        
    # getters and setters for the instance variables
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def exits(self):
        return self._exits

    @exits.setter
    def exits(self, value):
        self._exits = value
    
    @property
    def exitLocations(self):
        return self._exitLocations
    
    @exitLocations.setter
    def exitLocations(self, value):
        self._exitLocations = value
    
    @property
    def items(self):
        return self._items
    
    @items.setter
    def items(self, value):
        self._items = value
    
    @property
    def itemDescriptions(self):
        return self._itemDescriptions
    
    @itemDescriptions.setter
    def itemDescriptions(self, value):
        self._itemDescriptions = value
    
    @property
    def grabbables(self):
        return self._grabbables
    
    @grabbables.setter
    def grabbables(self, value):
        self._grabbables = value
    
    # adds an exit to the room
    # the exit is a string
    # the room is an instance of a room
    def addExit(self, exit, room):
        # append the exit and room to the appropriate lists
        self._exits.append(exit)
        self._exitLocations.append(room)
    
    # adds an item to the room
    # the item is a string (e.g., table)
    # the desc is a string that describes the item (e.g., it is made of wood)
    def addItem(self, item, desc):
        # append the item and description to the appropriate lists
        self._items.append(item)
        self._itemDescriptions.append(desc)

    # adds a grabbable item to the room
    # the item is a string (e.g., key)
    def addGrabbable(self, item,desc):
        # append the item to the list
        self._grabbables.append(item)

    # removes a grabbable item from the room
    # the item is a string (e.g., key)
    def delGrabbable(self, item):
        # remove the item from the list
        self._grabbables.remove(item)

    # returns a string description of the room
    def __str__(self):
        # first, the room name
        s = f"You are in {self.name}.\n"

        # next, the items in the room
        s += "You see: "
        for item in self.items:
            s += item + " "
        s += "\n"

        # next, the grabbable items in the room
        s += "You can take: "
        for grabbable in self.grabbables:
            s += grabbable + " "
        s += "\n"

        # next, the exits from the room
        s += "Exits: "
        for exit in self.exits:
            s += exit + " "

        return s


######################################################################
#Create rooms
def createRooms():
    global currentRoom

    #create the rooms and give them meaningful names
    r1 = Room("Room 1")
    r2 = Room("Room 2")
    r3 = Room("Room 3")
    r4 = Room("Room 4")
    r5 = Room("Sleigh")
    r6 = Room("Hidden Room")
    roof = Room("Roof")
    #create room 1
    r1.addExit("east", r2)
    r1.addExit("south", r3)
    r1.addGrabbable("key", "It is gold... and a key")
    r1.addItem("chair", "it's made of wicker")
    r1.addItem("table", desc)

    #create room 2
    r2.addExit("west",r1)
    r2.addExit("south",r4)
    r2.addExit("fireplace", roof)
    r2.addItem("rug", "it should probably be vaccumed")
    r2.addItem("fireplace", "cold and full of ashes")
    
    #create room 3
    r3.addExit("north", r1)
    r3.addExit("east", r4)
    r3.addExit("west", r6)
    r3.addGrabbable("book", "It is flamable, maybe.")
    r3.addGrabbable("statue", "There is nothing special about it, it looks heavy though.")
    r3.addItem("bookshelves", "They are empty. Go figure.")
    r3.addItem("desk", "The statue is resting on it. So is a book.")
    
    #create room 4
    r4.addExit("north", r2)
    r4.addExit("west", r3)
    r4.addExit("south", None)
    r4.addGrabbable("6-pack", "Fizzy drinks")
    r4.addItem("brew_rig","It's brewing some delicious beverage")

    #Create room 5
    roof.addGrabbable("Santa", "He looks like he needs a drink or six")
    roof.addExit("Sleigh", r5)

    #Create room 6
    r6.addExit("east", r3)
    r6.addItem("workbenches","Some assortments of toy parts and scattered tools")
    r6.addGrabbable("toys", "they look like something you wanted as a kid")
    
    #set the default room
    currentRoom = r1

def death():
    if (verb == "go" and noun == "fireplace" and "statue" in inventory):
        print(secretDeath)
        print(" " * 17 + "u" * 7)
        print(" " * 13 + "u" * 2 + "$" * 11 + "u" * 2)
        print(" " * 10 + "u" * 2 + "$" * 17 + "u" * 2)
        print(" " * 9 + "u" + "$" * 21 + "u")
        print(" " * 8 + "u" + "$" * 23 + "u")
        print(" " * 7 + "u" + "$" * 25 + "u")
        print(" " * 7 + "u" + "$" * 25 + "u")
        print(" " * 7 + "u" + "$" * 6 + "\"" + " " * 3 + "\"" + "$" * 3 + "\"" + " " * 3 + "\"" + "$" * 6 + "u")
        print(" " * 7 + "\"" + "$" * 4 + "\"" + " " * 6 + "u$u" + " " * 7 + "$" * 4 + "\"")
        print(" " * 8 + "$" * 3 + "u" + " " * 7 + "u$u" + " " * 7 + "u" + "$" * 3)
        print(" " * 8 + "$" * 3 + "u" + " " * 6 + "u" + "$" * 3 + "u" + " " * 6 + "u" + "$" * 3)
        print(" " * 9 + "\"" + "$" * 4 + "u" * 2 + "$" * 3 + " " * 3 + "$" * 3 + "u" * 2 + "$" * 4 + "\"")
        print(" " * 10 + "\"" + "$" * 7 + "\"" + " " * 3 + "\"" + "$" * 7 + "\"")
        print(" " * 12 + "u" + "$" * 7 + "u" + "$" * 7 + "u")
        print(" " * 13 + "u$\"$\"$\"$\"$\"$\"$u")
        print(" " * 2 + "u" * 3 + " " * 8 + "$" * 2 + "u$ $ $ $ $u" + "$" * 2 + " " * 7 + "u" * 3)
        print(" u" + "$" * 4 + " " * 8 + "$" * 5 + "u$u$u" + "$" * 3 + " " * 7 + "u" + "$" * 4)
        print(" " * 2 + "$" * 5 + "u" * 2 + " " * 6 + "\"" + "$" * 9 + "\"" + " " * 5 + "u" * 2 + "$" * 6)
        print("u" + "$" * 11 + "u" * 2 + " " * 4 + "\"" * 5 + " " * 4 + "u" * 4 + "$" * 10)
        print("$" * 4 + "\"" * 3 + "$" * 10 + "u" * 3 + " " * 3 + "u" * 2 + "$" * 9 + "\"" * 3 + "$" * 3 + "\"")
        print(" " + "\"" * 3 + " " * 6 + "\"" * 2 + "$" * 11 + "u" * 2 + " " + "\"" * 2 + "$" + "\"" * 3)
        print(" " * 11 + "u" * 4 + " \"\"" + "$" * 10 + "u" * 3)
        print(" " * 2 + "u" + "$" * 3 + "u" * 3 + "$" * 9 + "u" * 2 + " \"\"" + "$" * 11 + "u" * 3 + "$" * 3)
        print(" " * 2 + "$" * 10 + "\"" * 4 + " " * 11 + "\"\"" + "$" * 11 + "\"")
        print(" " * 3 + "\"" + "$" * 5 + "\"" + " " * 22 + "\"\"" + "$" * 4 + "\"\"")
    else:
        print("you got dedded")
        print(" " * 17 + "u" * 7)
        print(" " * 13 + "u" * 2 + "$" * 11 + "u" * 2)
        print(" " * 10 + "u" * 2 + "$" * 17 + "u" * 2)
        print(" " * 9 + "u" + "$" * 21 + "u")
        print(" " * 8 + "u" + "$" * 23 + "u")
        print(" " * 7 + "u" + "$" * 25 + "u")
        print(" " * 7 + "u" + "$" * 25 + "u")
        print(" " * 7 + "u" + "$" * 6 + "\"" + " " * 3 + "\"" + "$" * 3 + "\"" + " " * 3 + "\"" + "$" * 6 + "u")
        print(" " * 7 + "\"" + "$" * 4 + "\"" + " " * 6 + "u$u" + " " * 7 + "$" * 4 + "\"")
        print(" " * 8 + "$" * 3 + "u" + " " * 7 + "u$u" + " " * 7 + "u" + "$" * 3)
        print(" " * 8 + "$" * 3 + "u" + " " * 6 + "u" + "$" * 3 + "u" + " " * 6 + "u" + "$" * 3)
        print(" " * 9 + "\"" + "$" * 4 + "u" * 2 + "$" * 3 + " " * 3 + "$" * 3 + "u" * 2 + "$" * 4 + "\"")
        print(" " * 10 + "\"" + "$" * 7 + "\"" + " " * 3 + "\"" + "$" * 7 + "\"")
        print(" " * 12 + "u" + "$" * 7 + "u" + "$" * 7 + "u")
        print(" " * 13 + "u$\"$\"$\"$\"$\"$\"$u")
        print(" " * 2 + "u" * 3 + " " * 8 + "$" * 2 + "u$ $ $ $ $u" + "$" * 2 + " " * 7 + "u" * 3)
        print(" u" + "$" * 4 + " " * 8 + "$" * 5 + "u$u$u" + "$" * 3 + " " * 7 + "u" + "$" * 4)
        print(" " * 2 + "$" * 5 + "u" * 2 + " " * 6 + "\"" + "$" * 9 + "\"" + " " * 5 + "u" * 2 + "$" * 6)
        print("u" + "$" * 11 + "u" * 2 + " " * 4 + "\"" * 5 + " " * 4 + "u" * 4 + "$" * 10)
        print("$" * 4 + "\"" * 3 + "$" * 10 + "u" * 3 + " " * 3 + "u" * 2 + "$" * 9 + "\"" * 3 + "$" * 3 + "\"")
        print(" " + "\"" * 3 + " " * 6 + "\"" * 2 + "$" * 11 + "u" * 2 + " " + "\"" * 2 + "$" + "\"" * 3)
        print(" " * 11 + "u" * 4 + " \"\"" + "$" * 10 + "u" * 3)
        print(" " * 2 + "u" + "$" * 3 + "u" * 3 + "$" * 9 + "u" * 2 + " \"\"" + "$" * 11 + "u" * 3 + "$" * 3)
        print(" " * 2 + "$" * 10 + "\"" * 4 + " " * 11 + "\"\"" + "$" * 11 + "\"")
        print(" " * 3 + "\"" + "$" * 5 + "\"" + " " * 22 + "\"\"" + "$" * 4 + "\"\"")
        print(" " * 5 + "$" * 3 + "\"" + " " * 25 + "$" * 4 + "\"")
        

######################################################################
#START THE GAME!!!

inventory = []
createRooms()

#game loop, play forever unitl death or ask quit
while(True):
    status = f"{currentRoom}\nYou are carrying {inventory}"

    if (currentRoom == None):
        death()
        break
    
    #display status
    print("======================")
    print(status)

    #prompt player for input
    #game supports a simple language of <verb><noun>
    #valid vrebs are go, look, and take
    #valid nouns depend on the verb
    action = input("What to do?")
    action = action.lower()

    #exit the game if the player types exit, quit or bye
    leaveResponses = ["exit", "quit", "bye"]
    if (action in leaveResponses):
        break

    #set a default response
    response = "I don't undertand. Try <verb><noun>. Valid verbs are take, go, place, and look"

    #split the user input into words and store the words in a list
    words = action.split()

    # the game only understands two word inputs
    if (len(words) == 2):
        # isolate the verb and noun
        verb = words[0]
        noun = words[1]

        # the verb is: go
        if (verb == "go"):
            # set a default room variable
            y = currentRoom
            
            # set a default response
            response = "Invalid exit."                

            # check for valid exits in the current room
            for i in range(len(currentRoom.exits)):
                # a valid exit is found
                if (noun == currentRoom.exits[i]):
                # change the current room to the one that is
                # associated with the specified exit
                    currentRoom = currentRoom.exitLocations[i]
                    
                    # set the response (success)
                    response = "Room changed."
                    # no need to check any more exits
                    break
                
                elif (noun == "fireplace" and "statue" in inventory):
                    death()
                    currentRoom = None
                    break

            #Check to see if acess is allowed into hidden room
            x = str(y).split()
            x = x[4]
            if(noun == "west" and x == "3." and hiddenRoom == True):
                response = "You can't come here yet, try agian later."
                currentRoom = y

        # the verb is: look
        elif (verb == "look"):
            # set a default response
            response = "I don't see that item."
            
            # check for valid items in the current room
            for i in range(len(currentRoom.items)):
                # a valid item is found
                if (noun == currentRoom.items[i]):
                    # set the response to the item's description
                    response = currentRoom.itemDescriptions[i]
                    # no need to check any more items
                    break
            for i in range(len(currentRoom.grabbables)):
                # a valid item is found
                if (noun == currentRoom.grabbables[i]):
                    # set the response to the item's description
                    response = currentRoom.itemDescriptions[i]
                    # no need to check any more items
                    break
            
        # the verb is: take
        elif (verb == "take"):
            # set a default response
            response = "I don't see that item."
            
            # check for valid grabbable items in the current room
            for grabbable in currentRoom.grabbables:
                # a valid grabbable item is found
                if (noun == grabbable):
                    # add the grabbable item to the player's
                    # inventory
                    inventory.append(grabbable)
                    # remove the grabbable item from the room
                    currentRoom.delGrabbable(grabbable)
                
                    # set the response (success)
                    response = "Item grabbed."

                    # code for key
                    if(noun == 'key'):
                        desc = 'The table is made of oak and there is an imprint in the dust of a key of unknown color, but most definetly a key, maybe.'
                        createRooms()
                        currentRoom.delGrabbable('key')
                    # code for Santa
                    if(noun == 'Santa'):
                        santaStrength = randint(0,20)
                        playerStrength = randint(0,20)
                        if(santaStrength >= playerStrength):
                            death()
                            currentRoom = None
                            break
                        else:
                            response = "After a struggle, item grabbed"
                            
                    if(noun == 'statue'):
                        print('it is heavy, and carrying it will wear on you')
                        answer = input('Are you sure you want to grab it?')
                        if(answer in no):
                            response = 'Item will not be taken'
                            inventory.remove('statue')
                            currentRoom.addGrabbable("statue")
                        else:
                            pass
        elif (verb == "place"):
            
                    if(noun == 'key'):
                       currentRoom._itemDescriptions.append("it's made of oak, and there is a dust imprint where a key used to be")
                    elif(noun == 'statue' or 'book'):
                        if("bookshelves" in currentRoom.items):
                            response = "You put the item on the bookshelf, and it starts moving, revealing a hidden room"
                            if(noun == 'statue'):
                                inventory.remove('statue')
                            else:
                                inventory.remove('book')
                            hiddenRoom = False
                        else:
                            response = "I don't see that item."
                            
                    # no need to check any more grabbable items
                    #break

    # display the response
    print(f"\n{response}")


