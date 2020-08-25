import curses
from UIAction import wrapText, loopInventory

class mainUI:
	def worldUI(self, player, Maps, OS):
		loopMap(Maps.currentMap, self, OS)
		size = mainUI.mapNameUI(self, Maps.currentMapName)
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
			loopUI(i, pos, quickCharacter, self.addstr)
			self.addstr(1, 35, f"{player.stats['CLASS']} LEVEL: {str(player.currentStats['LEVEL'])} | {player.status}",
						curses.A_UNDERLINE)
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
			loopUI(i, pos, charInv, self.addstr)
			self.addstr(5, 35,
						f"STR: {str(player.currentStats['MaxSTR'])} DEF: {str(player.currentStats['MaxDEF'])}     GOLD: {str(player.Gold)}",
						curses.A_UNDERLINE)
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
			loopUI(i, pos, commands, self.addstr)
			self.addstr(i + 1, pos + 2, "LOG | PRESS C", curses.A_UNDERLINE)
			size = True
		except curses.error:
			print("TERMINAL SIZE TOO SMALL, PLEASE RESIZE!")
			size = False
		return size

	def mapNameUI(self, currentMapName):
		mapName = [["+------------------------------+"],
				   ["|                              |"],
				   ["+------------------------------+"]]
		i = 15
		pos = 0
		try:
			loopUI(i, pos, mapName, self.addstr)
			self.addstr(16, 2, currentMapName)
			size = True
		except curses.error:
			print("TERMINAL SIZE TOO SMALL, PLEASE RESIZE!")
			size = False
		return size

	def spells(self, item):
		i = 0
		spell = ""
		for x in item:
			spell += f"{i + 1}. {x['name']}: {x['MANA']} MP "
			if x != item[-1]:
				spell += "tab "
			i += 1
		wrapText(self.addstr, "SPELLS", spell, 1, 67, UI, "SIDE")

	def inventory(self, item):
		i = 0
		inventoryItems = ""
		for x in item:
			inventoryItems += f"{i + 1}. {x[i][1]}x {str(x[i][0]['name'])} "
			if x[i] != item[0][-1]:
				inventoryItems += "tab "
			i += 1
		wrapText(self.addstr, "INVENTORY", inventoryItems, 1, 67, UI, "SIDE")

	def merchantUI(self, yCoord, xCoord, currentMerchant):
		merchantItems = ""
		i = 0
		z = str(str(yCoord) + str(xCoord))
		for j in currentMerchant[z]:
			i += 1
			if j["type"] == "ARMOUR":
				merchantItems += f" {i}. {j['name']} DEF: {str(j['DEF'])} PRICE: {str(j['price'])} "
			elif j["type"] == "WEAPON":
				merchantItems += f"{i}. {j['name']} STR: {str(j['STR'])} PRICE: {str(j['price'])} "
			elif j["type"] == "ITEM":
				if j["throwable"]:
					merchantItems += f"{i}. {j['name']} DAMAGE: {str(j['damage'])} PRICE: {str(j['price'])} "
				else:
					merchantItems += f"{i}. {j['name']} HEAL: {str(j['heal'])} PRICE: {str(j['price'])} "
			if j != currentMerchant[z][-1]:
				merchantItems += "tab "
		amount = i
		wrapText(self.addstr, "FOR SALE", merchantItems, 1, 67, UI, "SIDE")
		return amount

	def chestToInventory(self, newItem, key, x, Maps, mapNames):
		if Maps.currentMapName == mapNames.homeName:
			self.addstr(newItem[x][0], newItem[x][1], ".")
			del Maps.homeChest[key][x]
			if len(Maps.homeChest[key]) == 1:
				del Maps.homeChest[key]
		elif Maps.currentMapName == mapNames.forestName:
			self.addstr(newItem[x][0], newItem[x][1], ".")
			del Maps.forestChest[key][x]
			if len(Maps.forestChest[key]) == 1:
				del Maps.forestChest[key]

	def chestUI(self, yCoord, xCoord, player, Maps, mapNames):
		z = str(str(yCoord) + str(xCoord))
		i = 0
		pos = 65
		loopUI(i, pos, UI, self.addstr)
		try:
			for key in Maps.currentMapChest:
				x = 1
				j = 0
				while x < len(Maps.currentMapChest[key]):
					zChest = str(str(Maps.currentMapChest[key][x][0]) + str(Maps.currentMapChest[key][x][1]))
					if zChest == z:
						wrapText(self.addstr, "CHEST CONTAINS", Maps.currentMapChest[key][x - 1]['name'], 1, 67, UI, "LOG")
						item = [player.Inventory for x in player.Inventory]
						if len(item) == 0:
							player.Inventory.append([Maps.currentMapChest[key][0], 1])
							mainUI.chestToInventory(self, Maps.currentMapChest[key], key, x, Maps, mapNames)
							return
						else:
							for _ in item:
								newItem = Maps.currentMapChest[key]
								if player.Inventory[j].count(Maps.currentMapChest[key][0]) >= 1:
									player.Inventory[j][1] += 1
									mainUI.chestToInventory(self, newItem, key, x, Maps, mapNames)
									return
								j += 1
								if j == len(player.Inventory):
									player.Inventory.append([newItem[0], 1])
									mainUI.chestToInventory(self, newItem, key, x, Maps, mapNames)
									return
					x += 1
		except KeyError:
			pass

	def questUI(self, player, yCoord, xCoord, Maps, mapNames, quest, QuestItems):
		mainUI.clearOptionalUI(self)
		z = str(str(yCoord) + str(xCoord))
		i = 1
		pos = 67
		try:
			from questAction import startQuestReward
			if Maps.currentMapQuest[z][0] in player.activeQuests:
				notComplete = quest.checkQuest(self.addstr, player, z, Maps, mapNames, loopInventory, wrapText, QuestItems)
				if notComplete:
					self.addstr(i, pos, "QUEST IN PROGRESS")
			else:
				wrapText(self.addstr, Maps.currentMapQuest[z][0][0], Maps.currentMapQuest[z][0][1], i, pos, UI, "SIDE")
				player.activeQuests.append(Maps.currentMapQuest[z][0])
				startReward = Maps.currentMapQuest[z][0][2][2]["QUESTITEM"]
				if startReward[0]["type"] == "QUEST":
					player.keyItems[startReward[0]["name"]] = startReward[0]
				else:
					startQuestReward(self.addstr, player, startReward, loopInventory, wrapText)
				if Maps.currentMapQuest[z][0][0] == Maps.elders_homeQuest["429"][0][0]:
					Maps.townSquareInfo[-1] += 1
		except KeyError:
			if Maps.currentMapQuest[z] == "IN PROGRESS":
				self.addstr(i, pos, "QUEST IN PROGRESS")
		except IndexError:
			self.addstr(i, pos, "QUEST COMPLETE")

	def informationUI(self, yCoord, xCoord, Maps, mobs, player, QuestItems):
		mainUI.clearOptionalUI(self)
		z = str(str(yCoord) + str(xCoord))
		i = 1
		pos = 67
		try:
			if Maps.currentMapName == Maps.allFarm[0] and mobs.currentMobLocation.killBoss[mobs.mobList.queenSpider["name"]] and Maps.farmInfo[z][-1] == 1:
				Maps.farmInfo[z][-1] += 1
			elif Maps.currentMapName == Maps.allTownSquare[0] and player.keyItems[QuestItems.letter["name"]]:
				Maps.townSquareInfo[z][-1] += 1
				del player.keyItems[QuestItems.letter["name"]]
				j = Maps.currentMapInfo[z][-1]
				wrapText(self.addstr, Maps.currentMapInfo[z][0], Maps.currentMapInfo[z][j], i, pos, UI, "SIDE")
				Maps.townSquareInfo[z][-1] += 1
				return
			elif Maps.currentMapName == Maps.allKingStarPub[0] and not mobs.currentMobLocation.mobLocation and Maps.kingStarPubInfo[z][-1] == 1:
				Maps.kingStarPubInfo[z][-1] += 1
		except KeyError:
			pass
		j = Maps.currentMapInfo[z][-1]
		wrapText(self.addstr, Maps.currentMapInfo[z][0], Maps.currentMapInfo[z][j], i, pos, UI, "SIDE")

	def clearOptionalUI(self):
		i = 0
		pos = 65
		loopUI(i, pos, empty, self.addstr)
		self.refresh()

def loopMap(item, screen, OS):
	try:
		col, row = (0, 0)
		while col < len(item):
			for _ in enumerate(item[0][0]):
				if item[col][0][row] in "X":
					if OS == "LINUX":
						screen.addstr(col, row, item[col][0][row], curses.color_pair(0) | curses.A_REVERSE)
					else:
						screen.addstr(col, row, item[col][0][row], curses.color_pair(1))
				elif item[col][0][row] in "*":
					screen.addstr(col, row, item[col][0][row], curses.color_pair(11))
				elif item[col][0][row] in "M":
					screen.addstr(col, row, item[col][0][row], curses.color_pair(12))
				elif item[col][0][row] in ("˄", "^", "Q", "I"):
					if OS == "LINUX":
						screen.addstr(col, row, item[col][0][row], curses.color_pair(4))
					else:
						screen.addstr(col, row, item[col][0][row], curses.color_pair(7))
				elif item[col][0][row] in ("|", "-"):
					screen.addstr(col, row, item[col][0][row], curses.color_pair(9))
				elif item[col][0][row] in "~":  # Obstructions not coloured
					if OS == "LINUX":
						screen.addstr(col, row, item[col][0][row], curses.color_pair(7) | curses.A_REVERSE)
					else:
						screen.addstr(col, row, item[col][0][row], curses.color_pair(4) | curses.A_REVERSE)
				elif item[col][0][row] in ("=", "ǁ", "+", ".", "#", "▒"):  # Obstructions not coloured
					screen.addstr(col, row, item[col][0][row])
				row += 1
			row = 0
			col += 1
	except curses.error:
		print("TERMINAL SIZE TOO SMALL, PLEASE RESIZE!")
		size = False
		return size

def mobMap(self, currentMapMobs, mobs, currentMap, OS):
	try:
		i = 0
		mobs.currentMobLocation.mobLocation = []
		for key in currentMapMobs:
			if key in mobs.mobIcons.mobs:  # MOBS
				for item in currentMapMobs[key]:
					if currentMap[item[0]][0][item[1]] == ".":
						mobs.currentMobLocation.mobLocation += [[mobs.mobIcons.mobs[key].copy(), item[0], item[1]]]
						if mobs.currentMobLocation.mobLocation[i][0]["type"] == "BOSS":
							self.addstr(item[0], item[1], key, curses.color_pair(6))
						else:
							if OS == "LINUX":
								self.addstr(item[0], item[1], key, curses.color_pair(2))
							else:
								self.addstr(item[0], item[1], key, curses.color_pair(5))
					i += 1
	except TypeError:
		pass

def chestMap(self, currentMapChest, OS):
	try:
		for key in currentMapChest:
			x = 1
			while x < len(currentMapChest[key]):
				if OS == "LINUX":
					self.addstr(currentMapChest[key][x][0], currentMapChest[key][x][1], "C", curses.color_pair(95) | curses.A_REVERSE)
				else:
					self.addstr(currentMapChest[key][x][0], currentMapChest[key][x][1], "C", curses.color_pair(7))
				x += 1
	except TypeError:
		pass

def loopUI(i, pos, item, addstr):
	for r in item:
		for c in r:
			addstr(i, pos, c)
			i += 1

clearLog = "                           "

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
