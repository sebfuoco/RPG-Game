from curses import wrapper
from UI import *
from ItemsAction import *

class Classes:
	# Warrior Stats + Factors
	class Warrior:
		stats = {"CLASS": "WARRIOR", "HP": 20, "MP": 0, "STR": 5, "DEF": 1}
		nextLevel = {"HPIncrease": 5, "MPIncrease": 0, "STRIncrease": 1}
		equipped = {"HEAD": Equipment.Empty, "CHEST": Equipment.Clothes, "LEFT-HAND": Equipment.Empty,
					"RIGHT-HAND": Equipment.WoodenSword}

	# Mage Stats + Factors
	class Mage:
		stats = {"CLASS": "MAGE", "HP": 20, "MP": 20, "STR": 1, "DEF": 0}
		nextLevel = {"HPIncrease": 2, "MPIncrease": 5, "STRIncrease": 1}
		equipped = {"HEAD": Equipment.Empty, "CHEST": Equipment.Clothes, "LEFT-HAND": Equipment.Empty,
					"RIGHT-HAND": Equipment.WoodenWand}

	# Thief Stats + Factors
	class Thief:
		stats = {"CLASS": "THIEF", "HP": 20, "MP": 0, "STR": 3, "DEF": 0}
		nextLevel = {"HPIncrease": 3, "MPIncrease": 0, "STRIncrease": 1}
		equipped = {"HEAD": Equipment.Empty, "CHEST": Equipment.Clothes, "LEFT-HAND": Equipment.Empty,
					"RIGHT-HAND": Equipment.WoodenSword}

class Player(object):
	def __init__(self, stats, nextLevel, equipped):
		XP = 20
		self.currentStats = {"LEVEL": 1, "MaxHP": stats["HP"], "MaxMP": stats["MP"]}
		self.stats = {"CLASS": stats["CLASS"], "HP": 11, "MP": stats["MP"], "STR": stats["STR"],
					  "DEF": stats["DEF"]}
		self.nextLevel = {"HPIncrease": nextLevel["HPIncrease"], "MPIncrease": nextLevel["MPIncrease"],
						  "STRIncrease": nextLevel["STRIncrease"]}
		self.equipped = {"HEAD": equipped["HEAD"], "CHEST": equipped["CHEST"], "LEFT-HAND": equipped["LEFT-HAND"],
						 "RIGHT-HAND": equipped["RIGHT-HAND"]}
		self.Inventory = [[Items.HealthPotion, 1], [Items.Antidote, 1]]
		self.Gold = 20
		self.status = "NORMAL"

class mob(object):
	def __init__(self, stats):
		self.stats = {"name": stats["name"], "HP": stats["HP"], "STR": stats["STR"], "DEF": stats["DEF"],
					  "XP": stats["XP"]}

class mobList:
	goblin = mob({"name": "GOBLIN", "HP": 10, "STR": 2, "DEF": 1, "XP": 5})
	rat = mob({"name": "RAT", "HP": 8, "STR": 4, "DEF": 0, "XP": 8})

def my_raw_input(screen, r, c, prompt_string, charlength):
	curses.echo()
	screen.addstr(r, c, "                          ")
	screen.addstr(r, c, prompt_string)
	screen.refresh()
	input = screen.getstr(r + 1, c, charlength)
	screen.addstr(r + 1, c, "                   ")
	curses.noecho()
	return input

def loadMap(self, yCoord, xCoord, spawnLocation, player):
	spawnLocation = respawnData(yCoord, xCoord, spawnLocation)
	yCoord, xCoord = loadNextMap(yCoord, xCoord, spawnLocation)
	self.clear()
	size = mainUI.worldUI(self, player)
	return yCoord, xCoord, spawnLocation, size

def main(main):
	yCoord = 11
	xCoord = 10
	size = True
	spawnLocation = 0
	# print(Equipment.Empty)
	screen = curses.initscr()
	curses.start_color()
	curses.use_default_colors()
	for i in range(0, 15):
		curses.init_pair(i + 1, i, 0)
	# for i in range(0, 15):
	# screen.addstr(str(i), curses.color_pair(i))
	screen.refresh()
	# screen.getstr()
	while True:
		screen.clear()
		screen.addstr(0, 0,
					  f"1. Warrior | HP: {str(Classes.Warrior.stats['HP'])} MP: {str(Classes.Warrior.stats['MP'])} STR: {str(Classes.Warrior.stats['STR'])} DEF: {str(Classes.Warrior.stats['DEF'])}")
		screen.addstr(1, 0,
					  f"2. Mage    | HP: {str(Classes.Mage.stats['HP'])} MP: {str(Classes.Mage.stats['MP'])} STR: {str(Classes.Mage.stats['STR'])} DEF: {str(Classes.Mage.stats['DEF'])}")
		screen.addstr(2, 0,
					  f"3. Thief   | HP: {str(Classes.Thief.stats['HP'])} MP: {str(Classes.Thief.stats['MP'])} STR: {str(Classes.Thief.stats['STR'])} DEF: {str(Classes.Thief.stats['DEF'])}")
		choice = my_raw_input(screen, 3, 0, "Type in a number below:", 1).decode("utf-8")
		screen.refresh()
		if choice == "1":
			player = Player(Classes.Warrior.stats, Classes.Warrior.nextLevel, Classes.Warrior.equipped)
			break
		elif choice == "2":
			player = Player(Classes.Mage.stats, Classes.Mage.nextLevel, Classes.Mage.equipped)
			break
		elif choice == "3":
			player = Player(Classes.Thief.stats, Classes.Thief.nextLevel, Classes.Thief.equipped)
			break
		else:
			screen.clear()
			screen.addstr(0, 0, "Not an option")
			screen.refresh()
			curses.napms(500)
	screen.clear()
	size = mainUI.worldUI(screen, player)
	movePlayer(screen, yCoord, xCoord)
	curses.noecho()
	curses.curs_set(0)
	# findPos(yCoord, xCoord)
	# choice = my_raw_input(screen, 12, 35, "Action?", 10).upper().decode("utf-8")
	while size:
		key = screen.getch()
		if key == curses.KEY_HOME:
			break
		# MOVEMENT
		elif key == curses.KEY_UP:
			x = detectCollision(yCoord - 1, xCoord)
			if x:
				if x == "loadMap":
					yCoord, xCoord, spawnLocation, size = loadMap(screen, yCoord, xCoord, spawnLocation, player)
				elif x == "Merchant":
					mainUI.merchantUI(screen, yCoord - 1, xCoord)
					z = str(str(yCoord - 1) + str(xCoord))
					number = int(my_raw_input(screen, 6, 66, "What will you buy?", 1).decode("utf-8")) - 1
					buyItem(screen, number, player, z)
				elif x == "Chest":
					mainUI.chestUI(screen, yCoord - 1, xCoord, player)
				elif x == "Quest":
					mainUI.questUI(screen, yCoord - 1, xCoord)
				else:
					mainUI.clearOptionalUI(screen)
					currentPosition(screen, yCoord, xCoord)
					yCoord -= 1
				movePlayer(screen, yCoord, xCoord)
		elif key == curses.KEY_DOWN:
			x = detectCollision(yCoord + 1, xCoord)
			if x:
				if x == "loadMap":
					yCoord, xCoord, spawnLocation, size = loadMap(screen, yCoord, xCoord, spawnLocation, player)
				elif x == "Merchant":
					mainUI.merchantUI(screen, yCoord + 1, xCoord)
				elif x == "Chest":
					mainUI.chestUI(screen, yCoord + 1, xCoord, player)
				elif x == "Quest":
					mainUI.questUI(screen, yCoord + 1, xCoord)
				else:
					mainUI.clearOptionalUI(screen)
					currentPosition(screen, yCoord, xCoord)
					yCoord += 1
				movePlayer(screen, yCoord, xCoord)
		elif key == curses.KEY_LEFT:
			x = detectCollision(yCoord, xCoord - 1)
			if x:
				if x == "loadMap":
					yCoord, xCoord, spawnLocation, size = loadMap(screen, yCoord, xCoord, spawnLocation, player)
				elif x == "Merchant":
					mainUI.merchantUI(screen, yCoord, xCoord - 1)
				elif x == "Chest":
					mainUI.chestUI(screen, yCoord, xCoord - 1, player)
				elif x == "Quest":
					mainUI.questUI(screen, yCoord, xCoord - 1)
				else:
					mainUI.clearOptionalUI(screen)
					currentPosition(screen, yCoord, xCoord)
					xCoord -= 1
				movePlayer(screen, yCoord, xCoord)
		elif key == curses.KEY_RIGHT:
			x = detectCollision(yCoord, xCoord + 1)
			if x:
				if x == "loadMap":
					yCoord, xCoord, spawnLocation, size = loadMap(screen, yCoord, xCoord, spawnLocation, player)
				elif x == "Merchant":
					mainUI.merchantUI(screen, yCoord, xCoord + 1)
				elif x == "Chest":
					mainUI.chestUI(screen, yCoord, xCoord + 1, player)
				elif x == "Quest":
					mainUI.questUI(screen, yCoord, xCoord + 1)
				else:
					mainUI.clearOptionalUI(screen)
					currentPosition(screen, yCoord, xCoord)
					xCoord += 1
				movePlayer(screen, yCoord, xCoord)
		elif key in [105, 73]:  # "i" pressed
			mainUI.clearOptionalUI(screen)
			item = [player.Inventory for x in player.Inventory]
			mainUI.inventory(screen, item)
		elif key in [99, 67]:  # "c" pressed
			mainUI.clearOptionalUI(screen)
			command = my_raw_input(screen, 12, 35, "WHAT WOULD YOU LIKE TO DO?", 8).decode("utf-8").upper()
			mainUI.logUI(screen)
			if command == "HELP":
				print("USE")
				print("EQUIP")
			elif command == "USE":
				item = [player.Inventory for x in player.Inventory]
				temp = []
				i = 0
				for x in item:
					if x[i][0]["type"] == "ITEM":
						temp.append([x[i][0], x[i][1]])
					i += 1
				temp = [temp for x in temp]
				mainUI.inventory(screen, temp)
				answer = int(my_raw_input(screen, 12, 35, "WHICH ITEM TO USE?", 8).decode("utf-8")) - 1
				mainUI.logUI(screen)
				mainUI.clearOptionalUI(screen)
				temp = useItem(screen, player, temp, answer)
				deleteItem(player, temp)
				curses.napms(1000)
				mainUI.logUI(screen)
			elif command == "EQUIP":
				item = [player.Inventory for x in player.Inventory]
				temp = []
				i = 0
				for x in item:
					if x[i][0]["type"] != "ITEM":
						temp.append([x[i][0], x[i][1]])
					i += 1
				temp = [temp for x in temp]
				mainUI.inventory(screen, temp)
				answer = int(my_raw_input(screen, 12, 35, "WHICH ITEM TO USE?", 8).decode("utf-8")) - 1
				mainUI.logUI(screen)
				mainUI.clearOptionalUI(screen)
				temp = equipItem(screen, player, temp, answer)
				deleteItem(player, temp)
				curses.napms(1000)
				mainUI.logUI(screen)
		screen.refresh()
	curses.endwin()

if __name__ == "__main__":
	wrapper(main)
