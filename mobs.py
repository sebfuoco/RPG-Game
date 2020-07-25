from curses import napms

class mobList:
	goblin = {"name": "GOBLIN", "HP": 10, "STR": 4, "DEF": 0, "XP": 5, "GOLD": 2, "ICON": "g"}
	rat = {"name": "RAT", "HP": 8, "STR": 8, "DEF": 0, "XP": 8, "GOLD": 4, "ICON": "r"}

class mobIcons:
	mobs = {"g": mobList.goblin, "r": mobList.rat}

class currentMobLocation:
	mobLocation = []

def attack(self, player, yCoord, xCoord):
	x = 0
	z = str(str(yCoord) + str(xCoord))
	for i in currentMobLocation.mobLocation:
		zMob = str(str(i[1]) + str(i[2]))
		if zMob == z:
			playerDamage = player.currentStats["MaxSTR"] - currentMobLocation.mobLocation[x][0]["DEF"]
			if playerDamage < 0:
				playerDamage = 0
			currentMobLocation.mobLocation[x][0]["HP"] -= playerDamage
			self.addstr(12, 35, f"DEALT {playerDamage} DAMAGE TO {currentMobLocation.mobLocation[x][0]['name']}")
			self.refresh()
			if currentMobLocation.mobLocation[x][0]["HP"] <= 0:
				self.addstr(13, 35, f"{currentMobLocation.mobLocation[x][0]['name']} KILLED!")
				self.addstr(14, 35, f"{currentMobLocation.mobLocation[x][0]['XP']} XP AND {currentMobLocation.mobLocation[x][0]['GOLD']} GOLD GAINED!")
				player.stats["XP"] += currentMobLocation.mobLocation[x][0]['XP']
				player.Gold += currentMobLocation.mobLocation[x][0]['GOLD']
				kill = currentMobLocation.mobLocation[x][0]['ICON']
				player.levelUp(self)
				del currentMobLocation.mobLocation[x]
				self.addstr(yCoord, xCoord, ".")
				self.refresh()
				return kill, i[1], i[2]
			mobDamage = currentMobLocation.mobLocation[x][0]['STR'] - player.currentStats['MaxDEF']
			if mobDamage < 0:
				mobDamage = 0
			player.stats["HP"] -= mobDamage
			self.addstr(13, 35, f"{currentMobLocation.mobLocation[x][0]['name']} DID {mobDamage} DAMAGE")
			if player.stats["HP"] < 0:
				player.stats["HP"] = 0
		x += 1
	return False, None, None
