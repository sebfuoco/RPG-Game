import curses
from curses import wrapper
from UI import *


class Equipment:
	# Defense Equipment
	# All Class Equipment
	Empty = {"name": "EMPTY", "price": 0, "equipLocation": "ALL", "equipClass": "ALL", "stats": (0, 0)}
	Clothes = {"name": "CLOTHES", "price": 1, "equipLocation": "CHEST", "equipClass": "ALL", "stats": (0, 1)}
	# Warrior Equipment
	LeatherBreastplate = {"name": "LEATHER-BREASTPLATE", "price": 2, "equipLocation": "CHEST", "equipClass": "WARRIOR",
						  "stats": (0, 2)}
	# Mage Equipment
	Robe = {"name": "ROBE", "price": 1, "equipLocation": "CHEST", "equipClass": "MAGE", "stats": (0, 2)}
	# Thief Equipment
	Bandana = {"name": "BANDANA", "price": 1, "equipLocation": "HEAD", "equipClass": "THIEF", "stats": (0, 1)}
	# Offense Equipment
	# All Class Equipment
	Knife = {"name": "KNIFE", "price": 3, "equipLocation": "HAND", "equipClass": "ALL", "stats": (2, 0)}
	# Warrior Equipment
	WoodenSword = {"name": "WOODEN-SWORD", "price": 1, "equipLocation": "HAND", "equipClass": ("WARRIOR", "THIEF"),
				   "stats": (1, 0)}
	# Mage Equipment
	WoodenWand = {"name": "WOODEN WAND", "price": 1, "equipLocation": "HAND", "equipClass": "MAGE", "stats": (1, 0)}
	# Thief Equipment
	Dagger = {"name": "DAGGER", "price": 10, "equipLocation": "HAND", "equipClass": "ALL", "stats": (5, 0)}


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
		equipped = {"HEAD": Equipment.Bandana, "CHEST": Equipment.Clothes, "LEFT-HAND": Equipment.Empty,
					"RIGHT-HAND": Equipment.WoodenSword}


class Player(object):
	def __init__(self, stats, nextLevel, equipped):
		XP = 20
		self.currentStats = {"LEVEL": 1, "MaxHP": stats["HP"], "MaxMP": stats["MP"]}
		self.stats = {"CLASS": stats["CLASS"], "HP": stats["HP"], "MP": stats["MP"], "STR": stats["STR"],
					  "DEF": stats["DEF"]}
		self.nextLevel = {"HPIncrease": nextLevel["HPIncrease"], "MPIncrease": nextLevel["MPIncrease"],
						  "STRIncrease": nextLevel["STRIncrease"]}
		self.equipped = {"HEAD": equipped["HEAD"], "CHEST": equipped["CHEST"], "LEFT-HAND": equipped["LEFT-HAND"],
						 "RIGHT-HAND": equipped["RIGHT-HAND"]}


class mob(object):
	def __init__(self, stats):
		self.stats = {"name": stats["name"], "HP": stats["HP"], "STR": stats["STR"], "DEF": stats["DEF"],
					  "XP": stats["XP"]}


class mobList:
	goblin = mob({"name": "GOBLIN", "HP": 10, "STR": 2, "DEF": 1, "XP": 5})
	rat = mob({"name": "RAT", "HP": 8, "STR": 4, "DEF": 0, "XP": 8})


def my_raw_input(screen, r, c, prompt_string, charlength):
	curses.echo()
	screen.addstr(r, c, prompt_string)
	screen.refresh()
	input = screen.getstr(r + 1, c, charlength)
	return input


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
	while size == True:
		key = screen.getch()
		if key == curses.KEY_HOME:
			break
		elif key == curses.KEY_UP:
			x = detectCollision(yCoord - 1, xCoord)
			if x:
				if x == "loadMap":
					spawnLocation = respawnData(yCoord, xCoord, spawnLocation)
					yCoord, xCoord = loadNextMap(yCoord, xCoord, spawnLocation)
					screen.clear()
					size = mainUI.worldUI(screen, player)
				else:
					currentPosition(screen, yCoord, xCoord)
					yCoord -= 1
				movePlayer(screen, yCoord, xCoord)
		elif key == curses.KEY_DOWN:
			x = detectCollision(yCoord + 1, xCoord)
			if x:
				if x == "loadMap":
					spawnLocation = respawnData(yCoord, xCoord, spawnLocation)
					yCoord, xCoord = loadNextMap(yCoord, xCoord, spawnLocation)
					screen.clear()
					size = mainUI.worldUI(screen, player)
				else:
					currentPosition(screen, yCoord, xCoord)
					yCoord += 1
				movePlayer(screen, yCoord, xCoord)
		elif key == curses.KEY_LEFT:
			x = detectCollision(yCoord, xCoord - 1)
			if x:
				if x == "loadMap":
					spawnLocation = respawnData(yCoord, xCoord, spawnLocation)
					yCoord, xCoord = loadNextMap(yCoord, xCoord, spawnLocation)
					screen.clear()
					size = mainUI.worldUI(screen, player)
				else:
					currentPosition(screen, yCoord, xCoord)
					xCoord -= 1
				movePlayer(screen, yCoord, xCoord)
		elif key == curses.KEY_RIGHT:
			x = detectCollision(yCoord, xCoord + 1)
			if x:
				if x == "loadMap":
					spawnLocation = respawnData(yCoord, xCoord, spawnLocation)
					yCoord, xCoord = loadNextMap(yCoord, xCoord, spawnLocation)
					screen.clear()
					size = mainUI.worldUI(screen, player)
				else:
					currentPosition(screen, yCoord, xCoord)
					xCoord += 1
				movePlayer(screen, yCoord, xCoord)

		screen.refresh()
	curses.endwin()


if __name__ == "__main__":
	wrapper(main)
