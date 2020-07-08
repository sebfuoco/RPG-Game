import curses
from curses import wrapper
from UI import *
"""
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
	Level = 1
	XP = 20

	# Warrior Stats + Factors
	class Warrior:
		stats = {"HitPoints": 20, "MagicPoints": 0, "Strength": 5, "Defense": 1, "MagicStrength": 0, "Evasion": 0,
				 "Accuracy": 80}
		XPFactor = 1.6
		nextLevel = {"HealthIncrease": 5, "MagicPointsIncrease": 0, "StrengthIncrease": 1, "MagicStrengthIncrease": 0,
					 "EvasionIncrease": 1, "AccuracyIncrease": 1}

	# Mage Stats + Factors
	class Mage:
		stats = {"HitPoints": 20, "MagicPoints": 20, "Strength": 1, "Defense": 0, "MagicStrength": 5, "Evasion": 0,
				 "Accuracy": 50}
		XPFactor = 1.5
		nextLevel = {"HealthIncrease": 2, "MagicPointsIncrease": 5, "StrengthIncrease": 1, "MagicStrengthIncrease": 1,
					 "EvasionIncrease": 1, "AccuracyIncrease": 1}

	# Thief Stats + Factors
	class Thief:
		stats = {"HitPoints": 20, "MagicPoints": 0, "Strength": 3, "Defense": 1, "MagicStrength": 0, "Evasion": 20,
				 "Accuracy": 70}
		XPFactor = 1.3;
		nextLevel = {"HealthIncrease": 3, "MagicPointsIncrease": 0, "StrengthIncrease": 1, "MagicStrengthIncrease": 0,
					 "EvasionIncrease": 1, "AccuracyIncrease": 1}
"""
def my_raw_input(screen, r, c, prompt_string, charlength):
    curses.echo()
    screen.addstr(r, c, prompt_string)
    screen.refresh()
    input = screen.getstr(r + 1, c, charlength)
    return input  #       ^^^^  reading input at next line

def main(main):
	yCoord = 11
	xCoord = 10
	spawnLocation = 0
	# print(Equipment.Empty)
	screen = curses.initscr()
	curses.start_color()
	curses.use_default_colors()
	for i in range(0, 16):
		curses.init_pair(i + 1, i, -1)
	while True:
		screen.clear()
		choice = my_raw_input(screen, 0, 0, "Start Game?", 3).upper().decode("utf-8")
		screen.refresh()
		if choice == "YES":
			# Update the buffer, adding text at different locations // MAP 15 LINES, 32 LONG
			mainUI.worldUI(screen)
			movePlayer(screen, yCoord, xCoord)
			break
		else:
			screen.clear()
			screen.addstr(0, 0, "why not :((((")
			screen.refresh()
			curses.napms(2000)
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
				print(yCoord, xCoord)
				if x == "loadMap":
					spawnLocation = loadNextMap(spawnLocation, yCoord, xCoord)
					screen.clear()
					yCoord, xCoord, spawnLocation = respawnPlayer(spawnLocation)
					mainUI.worldUI(screen)
				else:
					currentPosition(screen, yCoord, xCoord)
					yCoord -= 1
				movePlayer(screen, yCoord, xCoord)
		elif key == curses.KEY_DOWN:
			x = detectCollision(yCoord + 1, xCoord)
			if x:
				if x == "loadMap":
					spawnLocation = loadNextMap(spawnLocation, yCoord, xCoord)
					screen.clear()
					yCoord, xCoord, spawnLocation = respawnPlayer(spawnLocation)
					mainUI.worldUI(screen)
				else:
					currentPosition(screen, yCoord, xCoord)
					yCoord += 1
				movePlayer(screen, yCoord, xCoord)
		elif key == curses.KEY_LEFT:
			x = detectCollision(yCoord, xCoord - 1)
			if x:
				if x == "loadMap":
					spawnLocation = loadNextMap(spawnLocation, yCoord, xCoord)
					screen.clear()
					yCoord, xCoord, spawnLocation = respawnPlayer(spawnLocation)
					mainUI.worldUI(screen)
				else:
					currentPosition(screen, yCoord, xCoord)
					xCoord -= 1
				movePlayer(screen, yCoord, xCoord)
		elif key == curses.KEY_RIGHT:
			x = detectCollision(yCoord, xCoord + 1)
			if x:
				if x == "loadMap":
					spawnLocation = loadNextMap(spawnLocation, yCoord, xCoord)
					screen.clear()
					yCoord, xCoord, spawnLocation = respawnPlayer(spawnLocation)
					mainUI.worldUI(screen)
				else:
					currentPosition(screen, yCoord, xCoord)
					xCoord += 1
				movePlayer(screen, yCoord, xCoord)

		# Changes go in to the screen buffer and only get
		# displayed after calling `refresh()` to update
		screen.refresh()
	curses.endwin()

if __name__ == "__main__":
	#townSpawn = [[0, 15], [5, 20], [11, 20]]
	#print(townSpawn[0][1])
	wrapper(main)
