def loadNextMap(yCoord, xCoord, spawnLocation, Maps):
	z = str(str(yCoord) + str(xCoord))
	for name in Maps.allMaps:
		if Maps.currentMapData[z] == name[0]:
			Maps.currentMapName = name[0]
			Maps.currentMap = name[1]
			Maps.currentMapData = name[2]
			Maps.currentMapSpawn = name[3]
			Maps.currentMapMobs = name[4]
			Maps.currentMapChest = name[5]
			Maps.currentMapQuest = name[6]
			Maps.currentMapInfo = name[7]
			Maps.currentMapMerchant = name[8]
			break
	yCoord, xCoord = respawnPlayer(spawnLocation, Maps)
	return yCoord, xCoord

def detectCollision(self, yCoord, xCoord, mobs):
	t = self.instr(yCoord, xCoord, 1).decode("utf-8")
	self.refresh()
	if t != "":  # some Obstructions are empty in linux
		if t in "X":
			return "loadMap"
		elif t in ".":
			return True
		elif t in "C":
			return "Chest"
		elif t in "M":
			return "Merchant"
		elif t in "Q":
			return "Quest"
		elif t in "I":
			return "Information"
		elif t in mobs:
			return "Attack"
		elif t in "@":
			return "Player"
	else:
		return False

def currentPosition(self, yCoord, xCoord, currentMap):
	previousPosition = currentMap[yCoord][0][xCoord]
	self.addstr(yCoord, xCoord, previousPosition)
	self.refresh()

def moveEntity(self, color_pair, yCoord, xCoord, char, colour):
	self.addstr(yCoord, xCoord, char, color_pair(colour))
	self.refresh()
	return yCoord, xCoord

def respawnData(yCoord, xCoord, Maps):
	for name in Maps.allMaps:
		for coord in name[3]:
			if yCoord == coord[0] and xCoord == coord[1] and Maps.currentMapName == name[0]:
				spawnLocation = coord[2]
				return spawnLocation

def respawnPlayer(spawnLocation, Maps):
	y = Maps.currentMapSpawn[spawnLocation][0]
	x = Maps.currentMapSpawn[spawnLocation][1]
	return y, x

def mobKill(kill, yMob, xMob, Maps):
	zMob = str(str(yMob) + str(xMob))
	i = 0
	temp = []
	for name in Maps.allMaps:
		if Maps.currentMapName == name[0]:
			temp = name
			break

	while i < len(temp[4][kill]):
		z = str(str(temp[4][kill][i][0]) + str(temp[4][kill][i][1]))
		if zMob == z:
			del temp[4][kill][i]
			break
		i += 1
