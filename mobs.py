class mobList:
	goblin = {"name": "GOBLIN", "type": "NORMAL", "HP": 10, "STR": 4, "DEF": 0, "XP": 5, "GOLD": 2, "ICON": "g"}
	rat = {"name": "RAT", "type": "NORMAL", "HP": 8, "STR": 8, "DEF": 0, "XP": 8, "GOLD": 4, "ICON": "r"}
	spider = {"name": "SPIDER", "type": "NORMAL", "HP": 15, "STR": 6, "DEF": 0, "XP": 12, "GOLD": 6, "ICON": "s"}
	queenSpider = {"name": "QUEEN SPIDER", "type": "BOSS", "HP": 50, "STR": 6, "DEF": 2, "XP": 50, "GOLD": 50, "ICON": "q"}

class mobIcons:
	mobs = {mobList.goblin['ICON']: mobList.goblin, mobList.rat['ICON']: mobList.rat, mobList.spider['ICON']: mobList.spider, mobList.queenSpider['ICON']: mobList.queenSpider}

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
