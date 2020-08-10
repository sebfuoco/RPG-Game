import curses
import mobs
from Map import Maps
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

	def spells(self, item):
		i = 0
		pos = 65
		spell = ""
		for x in item:
			spell += f"{i + 1}. {x['name']}: {x['MANA']} MP "
			if x != item[-1]:
				spell += "tab "
			i += 1
		mainUI.wrapText(self, "SPELLS", spell, 1, 67, UI)

	def inventory(self, item):
		i = 0
		inventoryItems = ""
		for x in item:
			inventoryItems += f"{i + 1}. {x[i][1]}x {str(x[i][0]['name'])} "
			if x[i] != item[0][-1]:
				inventoryItems += "tab "
			i += 1
		mainUI.wrapText(self, "INVENTORY", inventoryItems, 1, 67, UI)

	def merchantUI(self, yCoord, xCoord):
		merchantItems = ""
		i = 0
		z = str(str(yCoord) + str(xCoord))
		for j in townMerchant[z]:
			i += 1
			if j["type"] == "ARMOUR":
				merchantItems += f" {i}. {j['name']} DEF: {str(j['DEF'])} PRICE: {str(j['price'])} "
			elif j["type"] == "WEAPON":
				merchantItems += f"{i}. {j['name']} STR: {str(j['STR'])} PRICE: {str(j['price'])} "
			elif j["type"] == "ITEM":
				merchantItems += f"{i}. {j['name']} HEAL: {str(j['heal'])} PRICE: {str(j['price'])} "
			if j != townMerchant[z][-1]:
				merchantItems += "tab "
		amount = i
		mainUI.wrapText(self, "FOR SALE", merchantItems, 1, 67, UI)
		return amount

	def chestToInventory(self, newItem, key, x):
		if Maps.currentMapName == Maps.mapNames.homeName:
			self.addstr(newItem[x][0], newItem[x][1], ".")
			del Maps.homeChest[key][x]
			if len(Maps.homeChest[key]) == 1:
				del Maps.homeChest[key]
		elif Maps.currentMapName == Maps.mapNames.forestName:
			self.addstr(newItem[x][0], newItem[x][1], ".")
			del Maps.forestChest[key][x]
			if len(Maps.forestChest[key]) == 1:
				del Maps.forestChest[key]

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
								break
							j += 1
							if j == len(player.Inventory):
								player.Inventory.append([newItem[0], 1])
								mainUI.chestToInventory(self, newItem, key, x)
					x += 1
		except KeyError:
			pass

	def wrapText(self, title, text, i, pos, mapUI):
		maxPos = pos + 35
		# TITLE
		self.addstr(0, 65, mapUI[0][0])
		self.addstr(i, 65, mapUI[1][0])
		if len(title) + 2 <= maxPos:
			self.addstr(i, pos, title, curses.A_UNDERLINE)
		i += 1
		self.addstr(i, 65, mapUI[1][0])
		# TEXT
		if (len(text) + pos + 2) <= maxPos:
			try:
				text = text.replace("tab", "")
			except AttributeError:
				pass
			self.addstr(i, pos, text)
		else:
			output = text.split()
			for word in output:
				if (len(word) + pos) <= maxPos and "tab" not in word:
					self.addstr(i, pos, word)
					pos += len(word) + 1
				else:
					pos = 67
					i += 1
					self.addstr(i, 65, mapUI[1][0])
					if word != "tab":
						self.addstr(i, pos, word.lstrip())
						pos += len(word) + 1
		self.addstr(i + 1, 65, mapUI[0][0])

	def loopInventory(self, player, reward, amount):
		i = 0
		item = [player.Inventory for x in player.Inventory]
		for x in item:
			if player.Inventory[i].count(reward):
				player.Inventory[i][1] += amount
				i = "IGNORE"
				break
			i += 1
		if i != "IGNORE":
			player.Inventory.append([reward, amount])

	def questReward(self, player, reward):
		mainUI.loopInventory(self, player, reward["REWARD"][0], reward["REWARD"][1])
		player.Gold += reward["GOLD"]
		player.stats["XP"] += reward["XP"]

	def checkQuest(self, player, z):
		i = 0
		if Maps.currentMapName == Maps.mapNames.farmName:
			if not mobs.currentMobLocation.mobLocation:
				while i < len(player.activeQuests):
					print(player.activeQuests[i])
					if Maps.currentMapQuest[z][0] == player.activeQuests[i]:
						mainUI.questReward(self, player, Maps.currentMapQuest[z][0][2][2])
						del Maps.currentMapQuest[z][0]
						del player.activeQuests[i]
						break
					i += 1

	def questUI(self, player, yCoord, xCoord):
		mainUI.clearOptionalUI(self)
		z = str(str(yCoord) + str(xCoord))
		i = 1
		pos = 67
		try:
			mainUI.checkQuest(self, player, z)
			if Maps.currentMapQuest[z][0] in player.activeQuests:
				self.addstr(i, pos, "QUEST IN PROGRESS")
			else:
				mainUI.wrapText(self, Maps.currentMapQuest[z][0][0], Maps.currentMapQuest[z][0][1], i, pos, UI)
				player.activeQuests.append(Maps.currentMapQuest[z][0])
				if Maps.currentMapQuest[z][0][0] == Maps.neighbour_homeQuest["429"][0][0]:
					Maps.townSquareInfo[-1] += 1
		except KeyError:
			if Maps.currentMapQuest[z] == "IN PROGRESS":
				self.addstr(i, pos, "QUEST IN PROGRESS")
		except IndexError:
			self.addstr(i, pos, "QUEST COMPLETE")

	def informationUI(self, yCoord, xCoord):
		mainUI.clearOptionalUI(self)
		z = str(str(yCoord) + str(xCoord))
		i = 1
		pos = 67
		j = Maps.currentMapInfo[-1]
		mainUI.wrapText(self, Maps.currentMapInfo[0], Maps.currentMapInfo[j], i, pos, UI)

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
				elif item[col][0][row] in ("˄", "Q", "I"):
					screen.addstr(col, row, item[col][0][row], curses.color_pair(7))
				elif item[col][0][row] in ("|", "-"):
					screen.addstr(col, row, item[col][0][row], curses.color_pair(9))
				elif item[col][0][row] in "~":  # Obstructions not coloured
					screen.addstr(col, row, item[col][0][row], curses.color_pair(4))
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
			if key in mobs.mobIcons.mobs:  # MOBS
				for item in Maps.currentMapMobs[key]:
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

UI = [["+-------------------------------------+"],
	  ["|                                     |"]]
