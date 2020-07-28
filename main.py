import MapAction
from curses import wrapper
from UI import *
from ItemsAction import *
from player import Classes, Player
from mobs import attack, currentMobLocation

def my_raw_input(screen, r, c, prompt_string, charlength):
	curses.curs_set(1)
	curses.echo()
	screen.addstr(r, c, "                          ")
	screen.addstr(r, c, prompt_string)
	screen.refresh()
	input = screen.getstr(r + 1, c, charlength)
	screen.addstr(r + 1, c, "                   ")
	screen.move(r + 1, c)
	curses.noecho()
	return input

def loadMap(self, yCoord, xCoord, spawnLocation, player):
	spawnLocation = MapAction.respawnData(yCoord, xCoord, spawnLocation)
	yCoord, xCoord = MapAction.loadNextMap(yCoord, xCoord, spawnLocation)
	self.clear()
	size = mainUI.worldUI(self, player)
	mobMap(self)
	chestMap(self)
	return yCoord, xCoord, spawnLocation, size

def move(self, direction, yCoord, xCoord, spawnLocation, player):
	originalCoord = {"yCoord": yCoord, "xCoord": xCoord}
	if direction == "UP":
		yCoord -= 1
	elif direction == "DOWN":
		yCoord += 1
	elif direction == "LEFT":
		xCoord -= 1
	elif direction == "RIGHT":
		xCoord += 1
	else:
		x = False
	x = MapAction.detectCollision(self, yCoord, xCoord)
	if x:
		if x == "loadMap":
			yCoord, xCoord, spawnLocation, size = loadMap(self, originalCoord["yCoord"], originalCoord["xCoord"], spawnLocation, player)
			yCoord, xCoord = MapAction.movePlayer(self, yCoord, xCoord)
		elif x == "Merchant":
			choice = my_raw_input(self, 12, 35, "BUY OR SELL?", 4).decode("utf-8").upper()
			mainUI.logUI(self)
			if choice == "BUY":
				mainUI.merchantUI(self, yCoord, xCoord)
				z = str(str(yCoord) + str(xCoord))
				number = int(my_raw_input(self, 12, 35, "WHAT WILL YOU BUY?", 1).decode("utf-8")) - 1
				mainUI.logUI(self)
				buyItem(self, number, player, z)
			elif choice == "SELL":
				temp = inventoryUse(("ARMOUR", "WEAPON", "ITEM"), player, False)
				try:
					if temp:
						try:
							mainUI.inventory(self, temp)
							number = int(my_raw_input(self, 12, 35, "WHAT WILL YOU SELL?", 1).decode("utf-8")) - 1
							mainUI.logUI(self)
							sellItem(self, number, player)
						except IndexError:
							pass
				except ValueError:
					pass
			yCoord, xCoord = MapAction.movePlayer(self, originalCoord["yCoord"], originalCoord["xCoord"])
		elif x == "Chest":
			mainUI.chestUI(self, yCoord, xCoord, player)
			yCoord, xCoord = MapAction.movePlayer(self, originalCoord["yCoord"], originalCoord["xCoord"])
		elif x == "Quest":
			mainUI.questUI(self, yCoord, xCoord)
			yCoord, xCoord = MapAction.movePlayer(self, originalCoord["yCoord"], originalCoord["xCoord"])
		elif x == "Attack":
			kill, yMob, xMob = attack(self, player, yCoord, xCoord)
			yCoord, xCoord = MapAction.movePlayer(self, originalCoord["yCoord"], originalCoord["xCoord"])
			if kill:
				MapAction.mobKill(kill, yMob, xMob)
				mainUI.charInventoryUI(self, player)
			mainUI.characterUI(self, player)
			self.refresh()
		else:
			mainUI.clearOptionalUI(self)
			MapAction.currentPosition(self, originalCoord["yCoord"], originalCoord["xCoord"])
			yCoord, xCoord = MapAction.movePlayer(self, yCoord, xCoord)
			if player.status == "POISONED":
				player.stats["HP"] -= 1
				mainUI.characterUI(self, player)
	else:
		return originalCoord["yCoord"], originalCoord["xCoord"], spawnLocation
	return yCoord, xCoord, spawnLocation

def main(main):
	yCoord = 12
	xCoord = 15
	size = True
	spawnLocation = 0
	screen = curses.initscr()
	curses.start_color()
	curses.use_default_colors()
	for i in range(0, 16):
		curses.init_pair(i + 1, i, 0)
	"""
	for i in range(0, 16):
		screen.addstr(str(i), curses.color_pair(i))
	screen.refresh()
	input = screen.getstr(3, 0, 0)
	"""
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
			player = Player("WARRIOR", Classes.Warrior.stats, Classes.Warrior.nextLevel, Classes.Warrior.equipped)
			break
		elif choice == "2":
			player = Player("THIEF", Classes.Mage.stats, Classes.Mage.nextLevel, Classes.Mage.equipped)
			break
		elif choice == "3":
			player = Player("MAGE", Classes.Thief.stats, Classes.Thief.nextLevel, Classes.Thief.equipped)
			break
		else:
			screen.clear()
			screen.addstr(0, 0, "Not an option")
			screen.refresh()
			curses.napms(500)
	EquipmentStats(player)
	screen.clear()
	size = mainUI.worldUI(screen, player)
	MapAction.movePlayer(screen, yCoord, xCoord)
	curses.noecho()
	screen.move(12, 35)
	screen.refresh()
	# findPos(yCoord, xCoord)
	# choice = my_raw_input(screen, 12, 35, "Action?", 10).upper().decode("utf-8")
	while size:
		curses.curs_set(0)
		if player.stats["HP"] <= 0:
			mainUI.logUI(screen)
			screen.refresh()
			screen.addstr(12, 35, f"YOU DIED")
			screen.refresh()
			curses.napms(2000)
			break
		key = screen.getch()
		mainUI.logUI(screen)
		if key == curses.KEY_HOME:
			break
		# MOVEMENT
		elif key == curses.KEY_UP:
			yCoord, xCoord, spawnLocation = move(screen, "UP", yCoord, xCoord, spawnLocation, player)
		elif key == curses.KEY_DOWN:
			yCoord, xCoord, spawnLocation = move(screen, "DOWN", yCoord, xCoord, spawnLocation, player)
		elif key == curses.KEY_LEFT:
			yCoord, xCoord, spawnLocation = move(screen, "LEFT", yCoord, xCoord, spawnLocation, player)
		elif key == curses.KEY_RIGHT:
			yCoord, xCoord, spawnLocation = move(screen, "RIGHT", yCoord, xCoord, spawnLocation, player)
		elif key in [105, 73]:  # "i" pressed
			mainUI.clearOptionalUI(screen)
			item = [player.Inventory for x in player.Inventory]
			mainUI.inventory(screen, item)
		elif key in [99, 67]:  # "c" pressed
			curses.curs_set(1)
			mainUI.clearOptionalUI(screen)
			command = my_raw_input(screen, 12, 35, "WHAT WOULD YOU LIKE TO DO?", 8).decode("utf-8").upper()
			mainUI.logUI(screen)
			if command == "HELP":
				print("USE")
				print("EQUIP")
			elif command == "USE":
				temp = inventoryUse(("ITEM",), player, False)
				if temp:
					mainUI.inventory(screen, temp)
					try:
						answer = int(my_raw_input(screen, 12, 35, "WHICH ITEM TO USE?", 1).decode("utf-8")) - 1
						mainUI.logUI(screen)
						mainUI.clearOptionalUI(screen)
						temp, i = useItem(screen, player, temp, answer)
						deleteItem(temp, player, i)
					except TypeError:
						pass
				else:
					screen.addstr(12, 35, f"NOTHING TO USE")
					screen.refresh()
					curses.napms(1000)
				mainUI.logUI(screen)
				mainUI.clearOptionalUI(screen)
			elif command == "EQUIP":
				temp = inventoryUse(("ARMOUR", "WEAPON"), player, True)
				if temp:
					mainUI.inventory(screen, temp)
					try:
						answer = int(my_raw_input(screen, 12, 35, "WHICH ITEM TO EQUIP?", 1).decode("utf-8")) - 1
						mainUI.logUI(screen)
						mainUI.clearOptionalUI(screen)
						try:
							if temp[0][answer][0]["equipLocation"] == "HAND":
								choice = my_raw_input(screen, 12, 35, "WHICH HAND?", 5).decode("utf-8").upper()
							else:
								choice = temp[0][answer][0]["equipLocation"]
							if temp[0][answer][0]["name"] == "EMPTY":
								choice = my_raw_input(screen, 12, 35, "WHERE TO UNEQUIP?", 5).decode("utf-8").upper()
								mainUI.logUI(screen)
								mainUI.clearOptionalUI(screen)
								if choice == "HAND":
									choice = my_raw_input(screen, 12, 35, "WHICH HAND?", 5).decode("utf-8").upper()
									if choice == "RIGHT":
										choice = "RIGHT-HAND"
									elif choice == "LEFT":
										choice = "LEFT-HAND"
							mainUI.logUI(screen)
							mainUI.clearOptionalUI(screen)
							temp, i = equipItem(screen, player, temp, answer, choice)
							deleteItem(temp, player, i)
						except IndexError:
							mainUI.logUI(screen)
							mainUI.clearOptionalUI(screen)
					except ValueError:
						pass
				else:
					screen.addstr(12, 35, f"NOTHING TO EQUIP")
					screen.refresh()
					curses.napms(1000)
				screen.refresh()
				mainUI.logUI(screen)
				mainUI.clearOptionalUI(screen)
			elif command == "CHECK":
				print(currentMobLocation.mobLocation)
		screen.move(12, 35)
		screen.refresh()
	curses.endwin()

if __name__ == "__main__":
	wrapper(main)
