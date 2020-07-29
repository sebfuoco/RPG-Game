import random
import math
import MapAction
from UI import mainUI
from player import Magic
from mobs import currentMobLocation

def mobAttack(self, player, x, order):
	mobDamage = currentMobLocation.mobLocation[x][0]['STR'] - player.currentStats['MaxDEF']
	evade = random.randrange(0, 100)
	if evade > player.currentStats["MaxEVASION"]:
		if order == "MOB":
			pos = 12
		else:
			pos = 13
		if mobDamage < 0:
			mobDamage = 0
		player.stats["HP"] -= mobDamage
		self.addstr(pos, 35, f"{currentMobLocation.mobLocation[x][0]['name']} DID {mobDamage} DAMAGE")
		if player.stats["HP"] < 0:
			player.stats["HP"] = 0
			return True
	else:
		self.addstr(13, 35, f"{currentMobLocation.mobLocation[x][0]['name']} MISSED")
	self.refresh()

def playerAttack(self, player, x, i, yCoord, xCoord, order, attackType):
	if attackType == "MAGIC":
		if (player.stats["MP"] - Magic.selectedMagic["MANA"]) >= 0:
			playerDamage = (player.currentStats["MaxMagicSTR"] * Magic.selectedMagic["POWER"]) - currentMobLocation.mobLocation[x][0]["DEF"]
			player.stats["MP"] -= Magic.selectedMagic["MANA"]
		else:
			playerDamage = player.currentStats["MaxSTR"] - currentMobLocation.mobLocation[x][0]["DEF"]
	else:
		playerDamage = math.floor(player.currentStats["MaxSTR"] - currentMobLocation.mobLocation[x][0]["DEF"])
	if playerDamage < 0:
		playerDamage = 0
	currentMobLocation.mobLocation[x][0]["HP"] -= playerDamage
	if order == "PLAYER":
		pos = 12
	else:
		pos = 13
	self.addstr(pos, 35, f"DEALT {playerDamage} DAMAGE TO {currentMobLocation.mobLocation[x][0]['name']}")
	if currentMobLocation.mobLocation[x][0]["HP"] <= 0:
		self.addstr(pos + 1, 35, f"{currentMobLocation.mobLocation[x][0]['name']} KILLED!")
		self.addstr(pos + 2, 35,
					f"{currentMobLocation.mobLocation[x][0]['XP']} XP AND {currentMobLocation.mobLocation[x][0]['GOLD']} GOLD GAINED!")
		player.stats["XP"] += currentMobLocation.mobLocation[x][0]['XP']
		player.Gold += currentMobLocation.mobLocation[x][0]['GOLD']
		kill = currentMobLocation.mobLocation[x][0]['ICON']
		player.levelUp(self)
		del currentMobLocation.mobLocation[x]
		self.addstr(yCoord, xCoord, ".")
		self.refresh()
		if kill:
			MapAction.mobKill(kill, i[1], i[2])
			mainUI.charInventoryUI(self, player)
			return True

def attack(self, player, yCoord, xCoord, attackType):
	x = 0
	z = str(str(yCoord) + str(xCoord))
	for i in currentMobLocation.mobLocation:
		zMob = str(str(i[1]) + str(i[2]))
		if zMob == z:
			if player.currentStats["MaxSPEED"] >= currentMobLocation.mobLocation[x][0]["SPEED"]:
				order = "PLAYER"
				death = playerAttack(self, player, x, i, yCoord, xCoord, order, attackType)
				if death:
					break
				mobAttack(self, player, x, order)
			else:
				order = "MOB"
				death = mobAttack(self, player, x, order)
				if death:
					break
				playerAttack(self, player, x, i, yCoord, xCoord, order, attackType)
		x += 1
	return False, None, None
