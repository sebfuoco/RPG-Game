import curses
from curses import wrapper
from UI import *
class Equipment:
	# Defense Equipment (Name, Price, EquipLocation, EquipClass, Stats)
	# Stats: (Attack, AccuracyBoost, Defense, Magic Defense, EvasionBoost, MagicBoost)
	# All Class Equipment
	Empty = {"Empty", 0, 0, "all", (0, 0, 0, 0, 0, 0)}
	Clothes = {"Clothes", 1, 2, "all", (0, 0, 1, 0, 0, 0)}

	# Warrior Equipment
	LeatherBreastplate = {"Leather Breastplate", 0, 2, "warrior", (0, 0, 2, 0, 0, 0)}

	# Mage Equipment
	Robe = {"Robe", 1, 2, "mage", (0, 0, 0, 5, 0, 1)}

	# Thief Equipment
	Bandana = {"Bandana", 0, 1, "thief", (0, 0, 1, 0, 2, 0)}

	# Offense Equipment
	# All Class Equipment
	Knife = {"Knife", 1, "all", (2, 0, 0, 0, 0, 0)}

	# Warrior Equipment
	WoodenSword = {"Wooden Sword", 5, ("warrior", "thief"), (1, 2, 0, 0, 0, 0)}

	# Mage Equipment
	WoodenWand = {"Wooden Wand", 1, "mage", (1, 0, 0, 0, 0, 0)}

	# Thief Equipment
	Dagger = {"Dagger", 10, "all", (5, 0, 0, 0, 0, 0)}

class Classes:
	# Warrior Stats + Factors
	class Warrior:
		stats = {"CLASS": "WARRIOR", "HP": 20, "MP": 0, "STR": 5, "DEF": 1}
		nextLevel = {"HPIncrease": 5, "MPIncrease": 0, "STRIncrease": 1}

	# Mage Stats + Factors
	class Mage:
		stats = {"CLASS": "MAGE","HP": 20, "MP": 20, "STR": 1, "DEF": 0}
		nextLevel = {"HPIncrease": 2, "MPIncrease": 5, "STRIncrease": 1}

	# Thief Stats + Factors
	class Thief:
		stats = {"CLASS": "THIEF", "HP": 20, "MP": 0, "STR": 3, "DEF": 0}
		nextLevel = {"HPIncrease": 3, "MPIncrease": 0, "STRIncrease": 1}

class Player(object):
	def __init__(self,stats, nextLevel):
		Level = 1
		XP = 20
		self.currentStats = {"MaxHP": stats["HP"], "MaxMP": stats["MP"]}
		self.stats = {"CLASS": stats["CLASS"], "HP": stats["HP"], "MP": stats["MP"], "STR": stats["STR"], "DEF": stats["DEF"]}
		self.nextLevel = {"HPIncrease": nextLevel["HPIncrease"], "MPIncrease": nextLevel["MPIncrease"], "STRIncrease": nextLevel["STRIncrease"]}

def my_raw_input(screen, r, c, prompt_string, charlength):
	curses.echo()
	screen.addstr(r, c, prompt_string)
	screen.refresh()
	input = screen.getstr(r + 1, c, charlength)
	return input

def main(main):
	yCoord = 11
	xCoord = 10
	spawnLocation = 0
	# print(Equipment.Empty)
	screen = curses.initscr()
	curses.start_color()
	while True:
		screen.clear()
		screen.addstr(0,0, f"1. Warrior | HP: {str(Classes.Warrior.stats['HP'])} MP: {str(Classes.Warrior.stats['MP'])} STR: {str(Classes.Warrior.stats['STR'])} DEF: {str(Classes.Warrior.stats['DEF'])}")
		screen.addstr(1,0, f"2. Mage    | HP: {str(Classes.Mage.stats['HP'])} MP: {str(Classes.Mage.stats['MP'])} STR: {str(Classes.Mage.stats['STR'])} DEF: {str(Classes.Mage.stats['DEF'])}")
		screen.addstr(2,0, f"3. Thief   | HP: {str(Classes.Thief.stats['HP'])} MP: {str(Classes.Thief.stats['MP'])} STR: {str(Classes.Thief.stats['STR'])} DEF: {str(Classes.Thief.stats['DEF'])}")
		choice = my_raw_input(screen, 3, 0, "Type in a number below:", 1).decode("utf-8")
		screen.refresh()
		if choice == "1":
			player = Player(Classes.Warrior.stats, Classes.Warrior.nextLevel)
			break
		elif choice == "2":
			player = Player(Classes.Mage.stats, Classes.Mage.nextLevel)
			break
		elif choice == "3":
			player = Player(Classes.Thief.stats, Classes.Thief.nextLevel)
			break
		else:
			screen.clear()
			screen.addstr(0, 0, "Not an option")
			screen.refresh()
			curses.napms(2000)
	mainUI.worldUI(screen, player)
	movePlayer(screen, yCoord, xCoord)
	curses.noecho()
	curses.curs_set(0)
	#findPos(yCoord, xCoord)
	#choice = my_raw_input(screen, 12, 35, "Action?", 10).upper().decode("utf-8")
	while True:
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
					mainUI.worldUI(screen, player)
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
					mainUI.worldUI(screen, player)
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
					mainUI.worldUI(screen, player)
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
					mainUI.worldUI(screen, player)
				else:
					currentPosition(screen, yCoord, xCoord)
					xCoord += 1
				movePlayer(screen, yCoord, xCoord)

		screen.refresh()
	curses.endwin()

if __name__ == "__main__":
	wrapper(main)
