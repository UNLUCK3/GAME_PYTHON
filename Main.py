import time
import datetime
import random
from random import randint
import GameItems

nowtime = datetime.datetime.now()
time.sleep(2)
print ("This info may be incorrect depending on your timezone. This is only used for initialization, please ignore: " + str(nowtime) + "\n" + "\n")


def intro():
	GameItems.LineWriter("write")
	print ("This is a crappy game by Bryndan Eigl.")
	GameItems.LineWriter("write")
	print ("\n" + "Before you begin the game, it might be wise to check your inventory.")
	InventoryCheck = input("\n" + "To check your inventory, simply type 'inventory': ")
	if (InventoryCheck.lower() == "inventory" or "info" or "help"):
		GameItems.Inventory(InventoryCheck)
		time.sleep(2)
		intro()
	else:
		GameItems.error("error")
		intro()

# This is at the bottom of the script so that the entirety of the code is read before initialization, increasing speeds.

intro()