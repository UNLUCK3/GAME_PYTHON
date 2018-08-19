# Stores Items for use in the game.

def Inventory(n):
    # Inventory Datas
    food = {'Name': 'Food', 'Description': 'Used for eating. It restores 10 HP, and weighs 10 units.','HP': 10, 'Weight': 10}
    water = {'Name': 'Water', 'Description': 'Drinking water. It restores 10 HP, and weighs 10 units.', 'HP': 10, 'Weight': 10}
    bedkey = {'Name': 'BedroomKey', 'Description': 'A key that unlocks the door to the bedroom', 'Unlock': 'Bedroom', 'Weight': 1}

    currentinventory = [food, water, bedkey]

    # Calling and printing inventories.
    z = n.lower()
    if (z == "inventory"):
        print ("Your inventory contains: ")
        xnum = 0
        for i in currentinventory:
            xnum = xnum + 1
            print (xnum, ": ", i['Name'])
    elif (z == "info"):
        print ("here is the info on your inventory: ")
        for i in currentinventory:
            print (i['Name'], ": ", i['Description'])
    elif (z == "help"):
        print ("Under development, sorry!")
    else:
        error("error")

def LineWriter(n):
    if (n.lower() == "write"):
        print ("\n" + "----------------------------------------" + "\n")

def error(n):
    if (n.lower() == "error"):
        print ("\n" + "That value was not recognized. Reloading..." + "\n")