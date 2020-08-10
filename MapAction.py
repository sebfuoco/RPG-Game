from Map import Maps
from mobs import mobIcons

def loadNextMap(yCoord, xCoord, spawnLocation):
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
			break
	yCoord, xCoord = respawnPlayer(spawnLocation)
	return yCoord, xCoord

def detectCollision(self, yCoord, xCoord):
	t = self.instr(yCoord, xCoord, 1).decode("utf-8")
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
	elif t in mobIcons.mobs:
		return "Attack"

def currentPosition(self, yCoord, xCoord):
	previousPosition = Maps.currentMap[yCoord][0][xCoord]
	self.addstr(yCoord, xCoord, previousPosition)
	self.refresh()

def movePlayer(self, yCoord, xCoord):
	self.addstr(yCoord, xCoord, "@")
	self.refresh()
	return yCoord, xCoord

def respawnData(yCoord, xCoord, spawnLocation):
	if Maps.currentMapName == Maps.mapNames.townName:
		if yCoord == 1 and xCoord == 15:  # FARM
			spawnLocation = 1
		elif yCoord == 5 and xCoord == 19:  # NEIGHBOUR
			spawnLocation = 0
		elif yCoord == 11 and xCoord == 19:  # HOME
			spawnLocation = 0
	elif Maps.currentMapName == Maps.mapNames.homeName:
		spawnLocation = 2  # TOWN
	elif Maps.currentMapName == Maps.mapNames.neighbour_homeName:
		spawnLocation = 1  # TOWN
	elif Maps.currentMapName == Maps.mapNames.farmName:
		if yCoord == 1 and xCoord == 15:
			spawnLocation = 1
		elif yCoord == 12 and xCoord == 15:
			spawnLocation = 0
	elif Maps.currentMapName == Maps.mapNames.forestName:
		if yCoord == 1 and xCoord == 15:
			spawnLocation = 1
		elif yCoord == 12 and xCoord == 15:
			spawnLocation = 0
	elif Maps.currentMapName == Maps.mapNames.townSquareName:
		if yCoord == 1 and xCoord == 15:
			spawnLocation = 1
	elif Maps.currentMapName == Maps.mapNames.castleGateName:
		if yCoord == 7 and xCoord == 15:
			spawnLocation = 0
	return spawnLocation

def respawnPlayer(spawnLocation):
	y = Maps.currentMapSpawn[spawnLocation][0]
	x = Maps.currentMapSpawn[spawnLocation][1]
	return y, x

def mobKill(kill, yMob, xMob):
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
