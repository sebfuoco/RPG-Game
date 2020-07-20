import curses
from Map import *
from Items import *
class mainUI:
	def worldUI(self, player):
		loopMap(Maps.currentMap, self)
		size = mainUI.mapNameUI(self)
		# CHARACTER
		size = mainUI.characterUI(self, player)
		# INVENTORY
		size = mainUI.charInventoryUI(self, player)
		# BATTLELOG
		size = mainUI.logUI(self)
		return size

	def characterUI(self, player):
		try:
			quickCharacter = [["+-----------------------------+"],
                              ["|                             |"],
                              ["| HP:                         |"],
                              ["| MP:                         |"],
                              ["+-----------------------------+"]]
			i = 0
			pos = 33
			loopUI(i, pos, quickCharacter, self)
			self.addstr(1, 35, player.stats["CLASS"] + "          LEVEL: " + str(player.currentStats["LEVEL"]), curses.A_BLINK)
			self.addstr(2, 39, str(player.stats["HP"]) + " / " + str(player.currentStats["MaxHP"]))
			self.addstr(3, 39, str(player.stats["MP"]) + " / " + str(player.currentStats["MaxMP"]))
			size = True
		except curses.error:
			print("TERMINAL SIZE TOO SMALL, PLEASE RESIZE!")
			size = False
		return size

	def charInventoryUI(self, player):
		try:
			charInv = [["+-----------------------------+"],
                       ["|                             |"],
                       ["|                             |"],
                       ["|                             |"],
                       ["|                             |"],
                       ["|                             |"],
                       ["+-----------------------------+"]]
			i = 4
			pos = 33
			loopUI(i, pos, charInv, self)
			self.addstr(5, 35, f"STR: {str(player.currentStats['MaxSTR'])} DEF: {str(player.currentStats['MaxDEF'])}     GOLD: {str(player.Gold)}", curses.A_BLINK)
			self.addstr(6, 35, "HEAD: " + player.equipped["HEAD"]["name"])
			self.addstr(7, 35, "CHEST: " + player.equipped["CHEST"]["name"])
			self.addstr(8, 35, "LEFT-HAND: " + player.equipped["LEFT-HAND"]["name"])
			self.addstr(9, 35, "RIGHT-HAND: " + player.equipped["RIGHT-HAND"]["name"])
			size = True
		except curses.error:
			print("TERMINAL SIZE TOO SMALL, PLEASE RESIZE!")
			size = False
		return size

	def logUI(self):
		try:
			commands = [["+-----------------------------+"],
                        ["|                             |"],
                        ["|                             |"],
                        ["|                             |"],
                        ["|                             |"],
                        ["|                             |"],
                        ["|                             |"],
                        ["+-----------------------------+"]]
			i = 10
			pos = 33
			loopUI(i, pos, commands, self)
			self.addstr(i + 1, pos + 2, "LOG", curses.A_BLINK)
			size = True
		except curses.error:
			print("TERMINAL SIZE TOO SMALL, PLEASE RESIZE!")
			size = False
		return size

	def mapNameUI(self):
		mapName =  [["+------------------------------+"],
					["|                              |"],
					["+------------------------------+"]]
		i = 15
		pos = 0
		try:
			loopUI(i, pos, mapName, self)
			self.addstr(16, 2, Maps.currentMapData["name"])
			size = True
		except curses.error:
			print("TERMINAL SIZE TOO SMALL, PLEASE RESIZE!")
			size = False
		return size

	def inventory(self, item):
		inventory = [["+------------------------------+"],
                    ["|                              |"],
                    ["|                              |"],
                    ["|                              |"],
                    ["|                              |"],
                    ["|                              |"],
                    ["|                              |"],
                    ["|                              |"],
                    ["|                              |"],
                    ["|                              |"],
                    ["|                              |"],
                    ["+------------------------------+"]]
		i = 0
		pos = 65
		loopUI(i, pos, inventory, self)
		self.addstr(i + 1, pos + 2, "INVENTORY", curses.A_UNDERLINE)
		#print(item)
		for x in item:
			self.addstr(i + 2, pos + 2, f"{i + 1}. {x[i][1]}x {str(x[i][0]['name'])}")
			i += 1

	def merchantUI(self, yCoord, xCoord):
		merchant = [["+----------------------------------------+"],
                    ["|                                        |"],
                    ["|                                        |"],
                    ["|                                        |"],
                    ["|                                        |"],
                    ["+----------------------------------------+"]]
		i = 0
		pos = 65
		loopUI(i, pos, merchant, self)
		z = str(str(yCoord) + str(xCoord))
		self.addstr(i + 1, pos + 2, "FOR SALE", curses.A_UNDERLINE)
		for j in townMerchant[z]:
			if j["type"] == "ARMOUR":
				self.addstr(i + 2, pos + 2, f"{i+ 1}. {j['name']} DEF: {str(j['DEF'])} PRICE: {str(j['price'])}")
			elif j["type"] == "WEAPON":
				self.addstr(i + 2, pos + 2, f"{i + 1}. {j['name']} STR: {str(j['STR'])} PRICE: {str(j['price'])}")
			elif j["type"] == "ITEM":
				self.addstr(i + 2, pos + 2, f"{i + 1}. {j['name']} HEAL: {str(j['heal'])} PRICE: {str(j['price'])}")
			i += 1

	def chestUI(self, yCoord, xCoord, player):
		z = str(str(yCoord) + str(xCoord))
		chest = [["+-------------------------------------+"],
				 ["|                                     |"],
				 ["+-------------------------------------+"]]
		i = 0
		pos = 65
		loopUI(i, pos, chest, self)
		try:
			self.addstr(i + 1, pos + 2, f"CHEST CONTAINS 1 {Maps.currentMapData[z]['name']}")
			item = [player.Inventory for x in player.Inventory]
			for x in item:
				if player.Inventory[i].count(Maps.currentMapData[z]):
					player.Inventory[i][1] += 1
					i = "IGNORE"
					break
				i += 1
			if i != "IGNORE":
				player.Inventory.append([Maps.currentMapData[z], 1])
			Maps.currentMapData.pop(z, None)
		except KeyError:
			self.addstr(i + 1, pos + 2, "CHEST ALREADY OPENED")

	def questUI(self, yCoord, xCoord):
		z = str(str(yCoord) + str(xCoord))
		quest = [["+-------------------------------------+"],
				 ["|                                     |"],
				 ["|                                     |"],
				 ["|                                     |"],
				 ["+-------------------------------------+"]]
		i = 0
		pos = 65
		loopUI(i, pos, quest, self)
		try:
			self.addstr(i + 1, pos + 2, f"CHEST CONTAINS 1 {Maps.currentMapData[z]['name']}")
			Maps.currentMapData.pop(z, None)
		except KeyError:
			self.addstr(i + 1, pos + 2, "CHEST ALREADY OPENED")

	def clearOptionalUI(self):
		i = 0
		pos = 65
		loopUI(i, pos, empty, self)
		self.refresh()

def loopMap(item, screen):
	try:
		col, row = (0, 0)
		while col < len(item):
			for i in enumerate(item[0][0]):
				if item[col][0][row] in "X":
					screen.addstr(col, row, item[col][0][row], curses.color_pair(1))
				elif item[col][0][row] in "*":
					screen.addstr(col, row, item[col][0][row], curses.color_pair(11))
				elif item[col][0][row] in "M":
					screen.addstr(col, row, item[col][0][row], curses.color_pair(12))
				elif item[col][0][row] in ("˄", "Q"):
					screen.addstr(col, row, item[col][0][row], curses.color_pair(7))
				elif item[col][0][row] in "C":
					screen.addstr(col, row, item[col][0][row], curses.color_pair(7))
				elif item[col][0][row] in ("|", "-"):
					screen.addstr(col, row, item[col][0][row], curses.color_pair(9))
				elif item[col][0][row] in ("=", "ǁ", "+",".", "#", "▒"):  # Obstructions not coloured
					screen.addstr(col, row, item[col][0][row])
				else:
					screen.addstr(col, row, item[col][0][row], curses.color_pair(5))
				row += 1
			row = 0
			col += 1
	except curses.error:
		print("TERMINAL SIZE TOO SMALL, PLEASE RESIZE!")
		size = False
		return size

def loopUI(i, pos, item, screen):
	for r in item:
		for c in r:
			screen.addstr(i, pos, c)
			i += 1

empty = [["                                          "],
         ["                                          "],
         ["                                          "],
         ["                                          "],
         ["                                          "],
         ["                                          "],
         ["                                          "],
         ["                                          "],
         ["                                          "],
         ["                                          "],
         ["                                          "],
         ["                                          "]]