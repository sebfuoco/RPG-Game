import curses

from Map import *
class mainUI:
	def worldUI(self, player):
		loopMap(Maps.currentMap, self)
		size = mainUI.mapNameUI(self)
		# CHARACTER
		size = mainUI.characterUI(self, player)
		# INVENTORY
		size = mainUI.charInventoryUI(self, player)
		# BATTLELOG
		size = mainUI.battleLogUI(self)
		return size

	def characterUI(self, player):
		try:
			quickCharacter =   [["+-----------------------------+"],
								["|                             |"],
								["| HP:                         |"],
								["| MP:                         |"],
								["+-----------------------------+"]]
			i = 0
			pos = 33
			loopUI(i, pos, quickCharacter, self)
			self.addstr(1, 35, player.stats["CLASS"] + "          LEVEL: " + str(player.currentStats["LEVEL"]))
			self.addstr(2, 39, str(player.stats["HP"]) + " / " + str(player.currentStats["MaxHP"]))
			self.addstr(3, 39, str(player.stats["MP"]) + " / " + str(player.currentStats["MaxMP"]))
			size = True
		except curses.error:
			print("TERMINAL SIZE TOO SMALL, PLEASE RESIZE!")
			size = False
		return size

	def charInventoryUI(self, player):
		try:
			charInv =  [["+-----------------------------+"],
						["|                             |"],
						["|                             |"],
						["|                             |"],
						["|                             |"],
						["|                             |"],
						["+-----------------------------+"]]
			i = 4
			pos = 33
			loopUI(i, pos, charInv, self)
			self.addstr(5, 35, "STR: " + str(player.stats["STR"]) + " DEF: " + str(player.stats["DEF"]))
			self.addstr(6, 35, "HEAD: " + player.equipped["HEAD"]["name"])
			self.addstr(7, 35, "CHEST: " + player.equipped["CHEST"]["name"])
			self.addstr(8, 35, "LEFT-HAND: " + player.equipped["LEFT-HAND"]["name"])
			self.addstr(9, 35, "RIGHT-HAND: " + player.equipped["RIGHT-HAND"]["name"])
			size = True
		except curses.error:
			print("TERMINAL SIZE TOO SMALL, PLEASE RESIZE!")
			size = False
		return size

	def battleLogUI(self):
		try:
			commands = [["+-----------------------------+"],
						["| BATTLE LOG                  |"],
						["|                             |"],
						["|                             |"],
						["|                             |"],
						["|                             |"],
						["|                             |"],
						["+-----------------------------+"]]
			i = 10
			pos = 33
			loopUI(i, pos, commands, self)
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

	def inventory(self):
		commands = [["+------------------------------+"],
					["| POTION                       |"],
					["| CLOTHES                      |"],
					["| WOODEN-SWORD                 |"],
					["+------------------------------+"]]
		i = 0
		pos = 32
		loopUI(i, pos, commands, self)

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
				elif item[col][0][row] in ("=", "ǁ", "+",".", "#"): # Obstructions not coloured
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
