import curses
import mobs
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
			self.addstr(1, 35, f"{player.stats['CLASS']} LEVEL: {str(player.currentStats['LEVEL'])} | {player.status}",
						curses.A_BLINK)
			self.addstr(2, 39, f"{str(player.stats['HP'])} / {str(player.currentStats['MaxHP'])}")
			self.addstr(3, 39, f"{str(player.stats['MP'])} / {str(player.currentStats['MaxMP'])}")
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
			self.addstr(5, 35,
						f"STR: {str(player.currentStats['MaxSTR'])} DEF: {str(player.currentStats['MaxDEF'])}     GOLD: {str(player.Gold)}",
						curses.A_BLINK)
			self.addstr(6, 35, f"HEAD: {player.equipped['HEAD']['name']}")
			self.addstr(7, 35, f"CHEST: {player.equipped['CHEST']['name']}")
			self.addstr(8, 35, f"LEFT-HAND: {player.equipped['LEFT-HAND']['name']}")
			self.addstr(9, 35, f"RIGHT-HAND: {player.equipped['RIGHT-HAND']['name']}")
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
			self.addstr(i + 1, pos + 2, "LOG | PRESS C", curses.A_BLINK)
			size = True
		except curses.error:
			print("TERMINAL SIZE TOO SMALL, PLEASE RESIZE!")
			size = False
		return size

	def mapNameUI(self):
		mapName = [["+------------------------------+"],
				   ["|                              |"],
				   ["+------------------------------+"]]
		i = 15
		pos = 0
		try:
			loopUI(i, pos, mapName, self)
			self.addstr(16, 2, Maps.currentMapName)
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
				self.addstr(i + 2, pos + 2, f"{i + 1}. {j['name']} DEF: {str(j['DEF'])} PRICE: {str(j['price'])}")
			elif j["type"] == "WEAPON":
				self.addstr(i + 2, pos + 2, f"{i + 1}. {j['name']} STR: {str(j['STR'])} PRICE: {str(j['price'])}")
			elif j["type"] == "ITEM":
				self.addstr(i + 2, pos + 2, f"{i + 1}. {j['name']} HEAL: {str(j['heal'])} PRICE: {str(j['price'])}")
			i += 1

	def chestToInventory(self, newItem, key, x):
		if Maps.currentMapName == "HOME":
			self.addstr(newItem[x][0], newItem[x][1], ".")
			print(Maps.homeChest)
			del Maps.homeChest[key][x]
			if len(Maps.homeChest[key]) == 1:
				del Maps.homeChest[key]
			print(Maps.homeChest)

	def chestUI(self, yCoord, xCoord, player):
		z = str(str(yCoord) + str(xCoord))
		chest = [["+-------------------------------------+"],
				 ["|                                     |"],
				 ["+-------------------------------------+"]]
		i = 0
		pos = 65
		loopUI(i, pos, chest, self)
		try:
			for key in Maps.currentMapChest:
				x = 1
				j = 0
				while x < len(Maps.currentMapChest[key]):
					zChest = str(str(Maps.currentMapChest[key][x][0]) + str(Maps.currentMapChest[key][x][1]))
					if zChest == z:
						self.addstr(i + 1, pos + 2, f"CHEST CONTAINS 1 {Maps.currentMapChest[key][x - 1]['name']}")
						item = [player.Inventory for x in player.Inventory]
						for y in item:
							newItem = Maps.currentMapChest[key]
							if player.Inventory[j].count(Maps.currentMapChest[key][0]) >= 1:
								player.Inventory[j][1] += 1
								mainUI.chestToInventory(self, newItem, key, x)
								j = "IGNORE"
								break
							j += 1
							if j != "IGNORE":
								player.Inventory.append([newItem[0], 1])
								mainUI.chestToInventory(self, newItem, key, x)
								break
					x += 1
		except KeyError:
			pass

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
			self.addstr(i + 1, pos + 2, f"QUEST ACTIVATED: {Maps.currentMapQuest[z]['name']}")
			Maps.currentMapData.pop(z, None)
		except KeyError:
			self.addstr(i + 1, pos + 2, "QUEST COMPLETED")

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
				elif item[col][0][row] in ("|", "-"):
					screen.addstr(col, row, item[col][0][row], curses.color_pair(9))
				elif item[col][0][row] in ("=", "ǁ", "+", ".", "#", "▒"):  # Obstructions not coloured
					screen.addstr(col, row, item[col][0][row])
				row += 1
			row = 0
			col += 1
	except curses.error:
		print("TERMINAL SIZE TOO SMALL, PLEASE RESIZE!")
		size = False
		return size

def mobMap(self):
	try:
		i = 0
		mobs.currentMobLocation.mobLocation = []
		for key in Maps.currentMapMobs:
			# print(key, Maps.currentMapMobs[key])
			if key in mobs.mobIcons.mobs:  # MOBS
				for item in Maps.currentMapMobs[key]:
					# print(item)
					if Maps.currentMap[item[0]][0][item[1]] == ".":
						mobs.currentMobLocation.mobLocation += [[mobs.mobIcons.mobs[key].copy(), item[0], item[1]]]
						if mobs.currentMobLocation.mobLocation[i][0]["type"] == "BOSS":
							self.addstr(item[0], item[1], key, curses.color_pair(6))
						else:
							self.addstr(item[0], item[1], key, curses.color_pair(5))
					i += 1
	except TypeError:
		pass


def chestMap(self):
	try:
		for key in Maps.currentMapChest:
			x = 1
			while x < len(Maps.currentMapChest[key]):
				self.addstr(Maps.currentMapChest[key][x][0], Maps.currentMapChest[key][x][1], "C", curses.color_pair(7))
				x += 1
	except TypeError:
		pass


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
