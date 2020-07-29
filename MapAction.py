from _curses import color_pair
from Map import Maps
from mobs import mobIcons

def loadNextMap(yCoord, xCoord, spawnLocation):
	z = str(str(yCoord) + str(xCoord))
	if Maps.currentMapData[z] == Maps.mapNames.townName:
		Maps.currentMapName = Maps.mapNames.townName
		Maps.currentMap = Maps.town
		Maps.currentMapData = Maps.townData
		Maps.currentMapSpawn = Maps.townSpawn
		Maps.currentMapMobs = None
		Maps.currentMapChest = None
		Maps.currentMapQuest = None
	elif Maps.currentMapData[z] == Maps.mapNames.homeName:
		Maps.currentMapName = Maps.mapNames.homeName
		Maps.currentMap = Maps.home
		Maps.currentMapData = Maps.homeData
		Maps.currentMapSpawn = Maps.homeSpawn
		Maps.currentMapMobs = None
		Maps.currentMapChest = Maps.homeChest
		Maps.currentMapQuest = None
	elif Maps.currentMapData[z] == Maps.mapNames.neighbour_homeName:
		Maps.currentMapName = Maps.mapNames.neighbour_homeName
		Maps.currentMap = Maps.neighbour_home
		Maps.currentMapData = Maps.neighbour_homeData
		Maps.currentMapSpawn = Maps.neighbour_homeSpawn
		Maps.currentMapMobs = None
		Maps.currentMapChest = None
		Maps.currentMapQuest = Maps.neighbour_homeQuest
	elif Maps.currentMapData[z] == Maps.mapNames.farmName:
		Maps.currentMapName = Maps.mapNames.farmName
		Maps.currentMap = Maps.farm
		Maps.currentMapData = Maps.farmData
		Maps.currentMapSpawn = Maps.farmSpawn
		Maps.currentMapMobs = Maps.farmMobs
		Maps.currentMapChest = None
		Maps.currentMapQuest = Maps.farmQuest
	elif Maps.currentMapData[z] == Maps.mapNames.forestName:
		Maps.currentMapName = Maps.mapNames.forestName
		Maps.currentMap = Maps.forest
		Maps.currentMapData = Maps.forestData
		Maps.currentMapSpawn = Maps.forestSpawn
		Maps.currentMapMobs = Maps.forestMobs
		Maps.currentMapChest = Maps.forestChest
		Maps.currentMapQuest = None
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
	elif t in mobIcons.mobs:
		return "Attack"

def currentPosition(self, yCoord, xCoord):
	previousPosition = Maps.currentMap[yCoord][0][xCoord]
	if previousPosition == "M":
		self.addstr(yCoord, xCoord, previousPosition, color_pair(12))
	elif previousPosition == "Q":
		self.addstr(yCoord, xCoord, previousPosition, color_pair(7))
	else:
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
		spawnLocation = 0
	return spawnLocation

def respawnPlayer(spawnLocation):
	y = Maps.currentMapSpawn[spawnLocation][0]
	x = Maps.currentMapSpawn[spawnLocation][1]
	return y, x

def mobKill(kill, yMob, xMob):
	zMob = str(str(yMob) + str(xMob))
	#print(Maps.currentMapMobs)
	def run():
		for item in Maps.currentMapMobs.items():
			i = 0
			while i < len(item[1]):
				z = str(str(item[1][i][0]) + str(item[1][i][1]))
				if z == zMob:
					if Maps.currentMapName == Maps.mapNames.farmName:
						del Maps.farmMobs[kill][i]
						if len(Maps.farmMobs[kill]) == 0:
							del Maps.farmMobs[kill]
						return
					elif Maps.currentMapName == Maps.mapNames.forestName:
						del Maps.forestMobs[kill][i]
						if len(Maps.forestMobs[kill]) == 0:
							del Maps.forestMobs[kill]
						return
				i += 1
	run()


