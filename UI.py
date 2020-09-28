import curses
import time
from math import floor
from UIAction import wrapText, loopInventory

class mainUI:
	def worldUI(self, player, Maps, OS):
		loopMap(Maps.currentMap, self, OS)
		mainUI.mapNameUI(self, Maps.currentMapName)
		# CHARACTER
		mainUI.characterUI(self, player)
		# INVENTORY
		mainUI.charInventoryUI(self, player)
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
			# 29 width
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
			text = f"STR: {str(floor(player.currentStats['MaxSTR']))} DEF: {str(floor(player.currentStats['MaxDEF']))} GOLD: {str(player.Gold)}"
			whitespace = 28 - len(text)
			orgText = f"STR: {str(floor(player.currentStats['MaxSTR']))} DEF: {str(floor(player.currentStats['MaxDEF']))}" + whitespace*" " + f"GOLD: {str(player.Gold)}"
			self.addstr(5, 35, f"{orgText}", curses.A_UNDERLINE)
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

	def initWrap(self, MaxMagicSTR, item, title):
		i = 0
		text = ""
		for x in item:
			if title == "INVENTORY":
				text += f"{i + 1}. {x[i][1]}x {str(x[i][0]['name'])} "
				if x[i] != item[0][-1]:
					text += "tab "
			elif title == "KEY ITEMS":
				text += f"{i + 1}. {str(x)} "
				if x != list(item)[-1]:
					text += "tab "
			elif title == "ABILITIES":
				countdown = f"COOLDOWN OF {str(x['countdown'])} KILLS"
				if x['countdown'] == 0:
					countdown = "AVAILABLE TO USE"
				text += f"{i + 1}. {x['name']}: {str(x['description'])}, {x['POWER']} POWER, {countdown}"
				if x != item[-1]:
					text += "tab "
			else:
				try:
					text += f"{i + 1}. {x['name']}: {x['MANA']} MP {x['POWER'] * MaxMagicSTR} DAMAGE "
				except KeyError:
					if x['type'] == "STAT":
						text += f"{i + 1}. {x['name']}: {x['MANA']} MP ADD {x['heal']} "
					else:
						text += f"{i + 1}. {x['name']}: {x['MANA']} MP HEAL {x['heal']} "
				if x != item[-1]:
					text += "tab "
			i += 1

		wrapText(self.addstr, title, text, 1, 67, UI, "SIDE")

	def merchantUI(self, yCoord, xCoord, currentMerchant):
		merchantItems = ""
		i = 0
		z = str(str(yCoord) + str(xCoord))
		for j in currentMerchant[z][0]:
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

	def chestToInventory(self, newItem, key, x, Maps):
		for name in Maps.allMaps:
			if Maps.currentMapName == name[0]:
				self.addstr(newItem[x][0], newItem[x][1], ".")
				del name[5][key][x]
				if len(name[5][key]) == 1:
					del name[5][key]

	def chestUI(self, yCoord, xCoord, player, Maps):
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
						if Maps.currentMapChest[key][0]['type'] == "QUEST":
							wrapText(self.addstr, "CHEST CONTAINS", Maps.currentMapChest[key][x - 1]['name'], 1, 67, UI,
									 "LOG")
							player.keyItems[Maps.currentMapChest[key][0]['name']] = Maps.currentMapChest[key][0]
							mainUI.chestToInventory(self, Maps.currentMapChest[key], key, x, Maps)
							return
						elif Maps.currentMapChest[key][0]['name'] == "GOLD":
							text = f"{Maps.currentMapChest[key][2]} {Maps.currentMapChest[key][x - 1]['name']}"
							wrapText(self.addstr, "CHEST CONTAINS", text, 1, 67, UI,
									 "LOG")
							player.Gold += Maps.currentMapChest[key][2]
							mainUI.chestToInventory(self, Maps.currentMapChest[key], key, x, Maps)
							mainUI.charInventoryUI(self, player)
							return
						else:
							wrapText(self.addstr, "CHEST CONTAINS", Maps.currentMapChest[key][x - 1]['name'], 1, 67, UI,
									 "LOG")
							item = [player.Inventory for x in player.Inventory]
							if len(item) == 0:
								player.Inventory.append([Maps.currentMapChest[key][0], 1])
								mainUI.chestToInventory(self, Maps.currentMapChest[key], key, x, Maps)
								return
							else:
								for _ in item:
									newItem = Maps.currentMapChest[key]
									if player.Inventory[j].count(Maps.currentMapChest[key][0]) >= 1:
										player.Inventory[j][1] += 1
										mainUI.chestToInventory(self, newItem, key, x, Maps)
										return
									j += 1
									if j == len(player.Inventory):
										player.Inventory.append([newItem[0], 1])
										mainUI.chestToInventory(self, newItem, key, x, Maps)
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
			if Maps.currentMapQuest[z][1] in player.activeQuests:
				notComplete = quest.checkQuest(self.addstr, player, z, Maps, mapNames, loopInventory, wrapText, QuestItems)
				if notComplete:
					self.addstr(i, pos, "QUEST IN PROGRESS")
			else:
				wrapText(self.addstr, Maps.currentMapQuest[z][1][0], Maps.currentMapQuest[z][1][2], i, pos, UI, "SIDE")
				player.activeQuests.append(Maps.currentMapQuest[z][1])
				startReward = Maps.currentMapQuest[z][1][3][2]["QUESTITEM"]
				if startReward[0]["type"] == "QUEST":
					player.keyItems[startReward[0]["name"]] = startReward[0]
				else:
					startQuestReward(self.addstr, player, startReward, loopInventory, wrapText)
				if Maps.currentMapQuest[z][1][0] == Maps.elders_homeQuest["429"][1][0]:
					Maps.townSquareInfo[-1] += 1
		except KeyError:
			if Maps.currentMapQuest[z] == "IN PROGRESS":
				self.addstr(i, pos, "QUEST IN PROGRESS")
		except IndexError:
			self.addstr(i, pos, "QUEST COMPLETE")

	def informationUI(self, yCoord, xCoord, Maps, mobs, player, QuestItems, OS):
		mainUI.clearOptionalUI(self)
		z = str(str(yCoord) + str(xCoord))
		i = 1
		pos = 67
		try:
			if Maps.currentMapName == Maps.allFarm[0] and mobs.currentMobLocation.killBoss[mobs.mobList.queenSpider["name"]] and Maps.farmInfo[z][-1] == 2:
				Maps.farmInfo[z][-1] += 1
			elif Maps.currentMapName == Maps.allTownSquare[0] and player.keyItems[QuestItems.letter["name"]]:
				Maps.townSquareInfo[z][-1] += 1
				del player.keyItems[QuestItems.letter["name"]]
				j = Maps.currentMapInfo[z][-1]
				wrapText(self.addstr, Maps.currentMapInfo[z][0], Maps.currentMapInfo[z][j], i, pos, UI, "SIDE")
				Maps.townSquareInfo[z][-1] += 1
				return
			elif Maps.currentMapName == Maps.allKingStarPub[0] and not mobs.currentMobLocation.mobLocation and Maps.kingStarPubInfo[z][-1] == 2:
				Maps.kingStarPubInfo[z][-1] += 1
			elif Maps.currentMapName == Maps.allCastleGate[0] and player.keyItems[QuestItems.royalCoin["name"]]:
				del player.keyItems[QuestItems.royalCoin["name"]]
				Maps.allCastleGate[7][z][-1] += 1
				Maps.allCastleGate[7][z][1][1] -= 1
				Maps.allCastleGate[7]["414"] = Maps.allCastleGate[7][z]
				del Maps.allCastleGate[7][z]
				loopMap(Maps.currentMap, self, OS)
				initEntity(self, Maps.castleGateInfo, OS, "I", 4)
				return
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
				if item[col][0][row] in "X":  # WHITE
					if OS == "LINUX":
						screen.addstr(col, row, item[col][0][row], curses.color_pair(0) | curses.A_REVERSE)
					else:
						screen.addstr(col, row, item[col][0][row], curses.color_pair(1))
				elif item[col][0][row] in "*":  # LIGHT GREEN
					screen.addstr(col, row, item[col][0][row], curses.color_pair(11))
				elif item[col][0][row] in ("˄", "^"):  # YELLOW
					if OS == "LINUX":
						screen.addstr(col, row, item[col][0][row], curses.color_pair(4))
					else:
						screen.addstr(col, row, item[col][0][row], curses.color_pair(7))
				elif item[col][0][row] in ("|", "-"):
					screen.addstr(col, row, item[col][0][row], curses.color_pair(9))
				elif item[col][0][row] in (" ", "~"):  # LIGHT BLUE
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

def colourEntity(self, yCoord, xCoord, ICON, animate):
	from main import OS
	if animate:
		duration = 0.3
		if animate == "FIRE":
			self.addstr(yCoord, xCoord, ICON["ICON"], curses.color_pair(13) | curses.A_REVERSE)
		elif animate == "ICE":
			self.addstr(yCoord, xCoord, ICON["ICON"], curses.color_pair(10) | curses.A_REVERSE)
		elif animate == "THUNDER":
			self.addstr(yCoord, xCoord, ICON["ICON"], curses.color_pair(15) | curses.A_REVERSE)
		elif animate == "WATER":
			self.addstr(yCoord, xCoord, ICON["ICON"], curses.color_pair(2) | curses.A_REVERSE)
		elif animate == "EARTH":
			self.addstr(yCoord, xCoord, ICON["ICON"], curses.color_pair(7) | curses.A_REVERSE)
		elif animate == "HEAL":
			self.addstr(yCoord, xCoord, ICON["ICON"], curses.color_pair(3) | curses.A_REVERSE)
		elif animate == "NORMAL":
			self.addstr(yCoord, xCoord, ICON["ICON"], curses.color_pair(0) | curses.A_REVERSE)
			duration = 0.1
		self.refresh()
		time.sleep(duration)
	else:
		if ICON.get("type") == "BOSS":
			self.addstr(yCoord, xCoord, ICON["ICON"], curses.color_pair(6))
		elif ICON["ICON"] == "@":
			self.addstr(yCoord, xCoord, ICON["ICON"])
		else:
			if OS == "LINUX":
				self.addstr(yCoord, xCoord, ICON["ICON"], curses.color_pair(2))
			else:
				self.addstr(yCoord, xCoord, ICON["ICON"], curses.color_pair(5))
	self.refresh()

def initEntity(self, entity, OS, char, colour):
	target = ""
	try:
		for key in entity:
			if char == "I":
				target = entity[key][1]
			elif char == "Q":
				target = entity[key][1][1]
			elif char == "M":
				target = entity[key][1]
			if OS == "LINUX":
				self.addstr(target[0], target[1], char, curses.color_pair(colour))
			else:
				self.addstr(target[0], target[1], char, curses.color_pair(colour + 3))
	except TypeError:
		pass

def initMob(self, currentMapMobs, mobs, currentMap, OS):
	try:
		i = 0
		mobs.currentMobLocation.mobLocation = []
		for key in currentMapMobs:
			if key in mobs.mobIcons.mobs:  # MOBS
				for item in currentMapMobs[key]:
					if currentMap[item[0]][0][item[1]] == ".":
						try:
							mobs.currentMobLocation.mobLocation += [[mobs.mobIcons.mobs[key].copy(), item[0], item[1], item[2]]]
						except IndexError:
							mobs.currentMobLocation.mobLocation += [[mobs.mobIcons.mobs[key].copy(), item[0], item[1], False]]
						if mobs.currentMobLocation.mobLocation[i][0]["type"] == "BOSS":  # PURPLE
							self.addstr(item[0], item[1], key, curses.color_pair(6))
						else:  # RED
							if OS == "LINUX":
								self.addstr(item[0], item[1], key, curses.color_pair(2))
							else:
								self.addstr(item[0], item[1], key, curses.color_pair(5))
					i += 1
	except TypeError:
		pass

def entityMap(self, currentMapMobs, mobs, currentMap, currentMapInfo, currentMapQuest, currentMapMerchant, OS):
	initMob(self, currentMapMobs, mobs, currentMap, OS)
	initEntity(self, currentMapInfo, OS, "I", 4)  # YELLOW
	initEntity(self, currentMapQuest, OS, "Q", 4)  # YELLOW
	initEntity(self, currentMapMerchant, OS, "M", 9)  # LIGHT BLUE

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

logEmpty = [[""], [""]]