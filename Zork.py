import re
import sys

exitCmd = re.compile('(?:Exit|Quit|Close|End|Suicide)', flags=re.IGNORECASE)
examineCmd = re.compile('(?:Look at|Examine|Inspect) (\w+)', flags=re.IGNORECASE)
inventoryCmd = re.compile('(?:Inventory|Items)', flags=re.IGNORECASE)
helpCmd = re.compile('(?:Help|H|\?|-H|-Help)(.*)', flags=re.IGNORECASE)

class everything:
	def __init__(self, name, description):
		self.name = name
		self.description = description

	def examine(self):
		#Examine something
		print(self.description)

class creature(everything):
	def __init__(self, name, description=None):
		super(creature, self).__init__(name, description) #Accesses parent class (Item) and calls it's constructor.

class hero(creature):
	def __init__(self, name, room, inventory=None):
		super(hero, self).__init__(name) #Accesses parent class (Item) and calls it's constructor.
		self.room = room #(room) Object reference to the room that the hero currently resides in.
		self.inventory = inventory #(List) List of items that the hero holds
		self.strength = 10.00#(Float) Number representing the max weight hero can hold

class room(everything):
	def __init__(self, name, description, info, interactables=None, north=None, east=None, south=None, west=None, items=None):
		super(room, self).__init__(name, description) #Accesses parent class (Item) and calls it's constructor.
		self.info = info #(String) Information used in describing the room without entering it.
		self.northRoom = north #(Room) Object reference to the room that exists at the north
		self.eastRoom = east #(Room) Object reference to the room that exists at the north
		self.southRoom = south #(Room) Object reference to the room that exists at the north
		self.westRoom = west #(Room) Object reference to the room that exists at the north
		self.items = items #(List) List of items (Dict[name] = Item) that exist in the room. Works like a hash map.
		self.interactables = interactables #(List) List of items (Dict[name] = Item) that can be interacted with in the room.


class Item(everything):
	def __init__(self, name, description, weight):
		self.name = name #(String) Name of the item
		self.description = description #(String) Description of the item
		self.weight = weight #(Float) weight of an item


class weapon(Item):
	def __init__(self, name, description, weight):
		super(weapon, self).__init__(self, name, description) #Accesses parent class (Item) and calls it's constructor.

# class sword(weapon):

# class club(weapon):




def main():
	print(open("README.txt").read())
	hero = buildCharacter()
	print("Goodnight {0}".format(hero.name))
	print("You wake up. Your head hurts and you're thirsty.")
	print(hero.room.description)
	while(True):
		#informUser():
		cmd = input(">>>")
		analyze(cmd, hero)

#def informUser():
	#Informs the user about their location.

	#Items that exist on the ground
	#Directions they can travel
	#if hero.room.north != None:

	#Objects of interest (Mailbox etc)

def buildCharacter():
	return(hero(input("What is your name traveler? "), room("Tunnel", "You are in a dark tunnel. The tunnel extends both east and west", "A dark tunnel extends")))

def analyze(cmd, hero):
	if exitCmd.match(cmd):
		if(input("Are you sure? Y/N: ").lower() == 'y'):
			sys.exit()
		else:
			return
	if examineCmd.match(cmd):
		#Will not match with "examine". Need "examine what?" response, fix regex.
		cmdParams = examineCmd.match(cmd).groups()
		if cmdParams[0] == " ":
			print("Examine what?")
		elif cmdParams[0].lower() == 'room':
			hero.room.examine()
		else:
			print("There is no {0} around here".format(cmdParams[0])) if not cmdParams[0].endswith("s") else print("There are no {0} around here".format(cmdParams[0])) #Crappy plural checker statement


if __name__ == '__main__':
	main()
