import random
import curses
import time
import mobs
from player import Magic
from UI import colourEntity
import math

def mobMove(self, player, mobLocation, currentMapMobs, currentMap, currentPosition, moveEntity, detectCollision, characterUI, OS, color_pair, yCoord, xCoord):
	beforeMob = ""
	i = 0
	for mob in mobLocation:
		currentMob = mob[0]
		if currentMob != beforeMob:
			i = 0
		number = random.randrange(0, 4)
		originalLocation = [mob[1], mob[2]]
		if number == 0 and mob[1] != 1:  # UP
			mob[1] -= 1
		elif number == 1 and mob[1] != (len(currentMap) - 2):  # DOWN
			mob[1] += 1
		elif number == 2 and mob[2] != 1:  # LEFT
			mob[2] -= 1
		elif number == 3 and mob[2] != (len(currentMap[0][0]) - 1):  # RIGHT
			mob[2] += 1
		x = detectCollision(self, mob[1], mob[2], mobs.mobIcons.mobs)
		if (abs(mob[1] - yCoord > 2) or abs(mob[2] - xCoord) > 2) and mob[3] is False:  # check distance between mob and player
			if x and x not in ("loadMap", "Chest", "Merchant", "Quest", "Information", "Attack", "Player"):
				currentPosition(self, currentMapMobs[mob[0]["ICON"]][i][0], currentMapMobs[mob[0]["ICON"]][i][1], currentMap)
				currentMapMobs[mob[0]["ICON"]][i][0] = mob[1]
				currentMapMobs[mob[0]["ICON"]][i][1] = mob[2]
				colour = 2
				if OS == "WINDOWS":
					colour = 5
				moveEntity(self, color_pair, mob[1], mob[2], mob[0]["ICON"], colour)
			else:
				mob[1] = originalLocation[0]
				mob[2] = originalLocation[1]
		elif x == "Player":
			mobAttack(self, player, 0, "MOB", [mob])
			characterUI(self, player)
			mob[1] = originalLocation[0]
			mob[2] = originalLocation[1]
		else:
			mob[1] = originalLocation[0]
			mob[2] = originalLocation[1]
		beforeMob = mob[0]
		i += 1

def mobAttack(self, player, x, order, mobLocation):
	mobDamage = math.floor(mobLocation[x][0]['STR'] - player.currentStats['MaxDEF'])
	evade = random.randrange(0, 100)
	if evade > player.currentStats["MaxEVASION"]:
		if order == "MOB":
			pos = 12
		else:
			pos = 13
		if mobDamage < 0:
			mobDamage = 0
		player.stats["HP"] -= mobDamage
		self.addstr(pos, 35, f"{mobLocation[x][0]['name']} DID {mobDamage} DAMAGE")
		try:
			if mobLocation[x][0]['inflict']:
				statusEffect = random.randrange(0, 100)
				if statusEffect < mobLocation[x][0]['inflict'][1]:
					player.status = mobLocation[x][0]['inflict'][0]
		except KeyError:
			pass
		if player.stats["HP"] < 0:
			player.stats["HP"] = 0
			return True
	else:
		self.addstr(13, 35, f"{mobLocation[x][0]['name']} MISSED")
	self.refresh()

def playerAttack(self, player, x, i, yCoord, xCoord, order, attackType, Maps, MapAction, currentMobLocation, charInventoryUI, newLine):
	if attackType == "MAGIC" and Magic.selectedMagic["type"] == "OFFENSIVE":
		if (player.stats["MP"] - Magic.selectedMagic["MANA"]) >= 0:
			playerDamage = math.floor(player.currentStats["MaxMagicSTR"] * Magic.selectedMagic["POWER"])
			if Magic.selectedMagic["ELEMENT"] == currentMobLocation.mobLocation[x][0]["weakness"]:
				playerDamage *= 2
			player.stats["MP"] -= Magic.selectedMagic["MANA"]
			colourEntity(self, yCoord, xCoord, currentMobLocation.mobLocation[x][0], Magic.selectedMagic["ELEMENT"])
			colourEntity(self, yCoord, xCoord, currentMobLocation.mobLocation[x][0], False)
		else:
			playerDamage = player.currentStats["MaxSTR"] - currentMobLocation.mobLocation[x][0]["DEF"]
	else:
		playerDamage = math.floor(player.currentStats["MaxSTR"] - currentMobLocation.mobLocation[x][0]["DEF"])
	if playerDamage < 0:
		playerDamage = 0
	currentMobLocation.mobLocation[x][0]["HP"] -= playerDamage
	if order == "PLAYER":
		y = 12
	else:
		y = 13
	if currentMobLocation.mobLocation[x][0]["HP"] <= 0:
		if currentMobLocation.mobLocation[x][0]['type'] == "BOSS":
			currentMobLocation.killBoss[currentMobLocation.mobLocation[x][0]['name']] = True
		self.addstr(y, 35, f"{currentMobLocation.mobLocation[x][0]['name']} KILLED!")
		self.addstr(y + 1, 35,
					f"{currentMobLocation.mobLocation[x][0]['XP']} XP AND {currentMobLocation.mobLocation[x][0]['GOLD']} GOLD GAINED!")
		player.stats["XP"] += currentMobLocation.mobLocation[x][0]['XP']
		player.Gold += currentMobLocation.mobLocation[x][0]['GOLD']
		kill = currentMobLocation.mobLocation[x][0]['ICON']
		if player.stats["XP"] >= player.currentStats["MaxXP"]:
			player.levelUp(self, (y + 2), charInventoryUI)
		del currentMobLocation.mobLocation[x]
		self.addstr(yCoord, xCoord, ".")
		self.refresh()
		if kill:
			MapAction.mobKill(kill, i[1], i[2], Maps)
			charInventoryUI(self, player)
			return True
	else:
		from UI import logEmpty
		text = f"DEALT {playerDamage} DAMAGE TO {currentMobLocation.mobLocation[x][0]['name']}"
		pos = 35
		newLine(text, self.addstr, y, pos + 30, pos, pos, logEmpty)
		self.refresh()

def attack(self, player, yCoord, xCoord, attackType, Maps, MapAction, currentMobLocation, charInventoryUI, newLine):
	x = 0
	z = str(str(yCoord) + str(xCoord))
	for i in currentMobLocation.mobLocation:
		zMob = str(str(i[1]) + str(i[2]))
		if zMob == z:
			if player.currentStats["MaxSPEED"] >= currentMobLocation.mobLocation[x][0]["SPEED"]:
				order = "PLAYER"
				death = playerAttack(self, player, x, i, yCoord, xCoord, order, attackType, Maps, MapAction, currentMobLocation, charInventoryUI, newLine)
				if death:
					break
				mobAttack(self, player, x, order, currentMobLocation.mobLocation)
			else:
				order = "MOB"
				death = mobAttack(self, player, x, order, currentMobLocation.mobLocation)
				if death:
					break
				playerAttack(self, player, x, i, yCoord, xCoord, order, attackType, Maps, MapAction, currentMobLocation, charInventoryUI, newLine)
		x += 1
