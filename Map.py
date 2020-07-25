from Items import *
from curses import color_pair
from mobs import mobIcons

class Maps:
	town = [["+==============X===============+"],
			["ǁ..............................ǁ"],
			["ǁ..###..............▒▒▒▒▒▒▒▒▒▒.ǁ"],
			["ǁ..#˄#..............▒˄˄˄˄˄˄˄˄▒.ǁ"],
			["ǁ..#M#..............▒˄˄˄˄˄˄˄˄▒.ǁ"],
			["ǁ...................X˄˄˄˄˄˄˄˄▒.ǁ"],
			["ǁ..###..............▒˄˄˄˄˄˄˄˄▒.ǁ"],
			["ǁ..#˄#..............▒▒▒▒▒▒▒▒▒▒.ǁ"],
			["ǁ..#M#.........................ǁ"],
			["ǁ...................▒▒▒▒▒▒▒▒▒▒.ǁ"],
			["ǁ..###..............▒˄˄˄˄˄˄˄˄▒.ǁ"],
			["ǁ..#˄#..............X˄˄˄˄˄˄˄˄▒.ǁ"],
			["ǁ..#M#..............▒▒▒▒▒▒▒▒▒▒.ǁ"],
			["ǁ..............................ǁ"],
			["+==============================+"]]
	townData = {"name": "TOWN", "1119": "HOME", "115": "FARMS", "519": "NEIGHBOURS_HOME"}
	townSpawn = [[1, 15], [5, 19], [11, 19]]
	home = [["+==============================+"],
			["ǁ##############################ǁ"],
			["ǁ#............................#ǁ"],
			["ǁ#............................#ǁ"],
			["ǁX............................#ǁ"],
			["ǁ#............................#ǁ"],
			["ǁ##############################ǁ"],
			["+==============================+"]]
	homeData = {"name": "HOME", "42": "TOWN"}
	homeSpawn = [[4, 2]]
	homeChest = {Items.HealthPotion['name']: [Items.HealthPotion, [3, 29]], Items.ManaPotion['name']: [Items.ManaPotion, [4, 29]]}
	neighbour_home = [["+==============================+"],
                      ["ǁ##############################ǁ"],
                      ["ǁ#............................#ǁ"],
                      ["ǁ#............................#ǁ"],
                      ["ǁX...........................Q#ǁ"],
                      ["ǁ#............................#ǁ"],
                      ["ǁ#............................#ǁ"],
                      ["ǁ#............................#ǁ"],
                      ["ǁ##############################ǁ"],
                      ["+==============================+"]]
	neighbour_homeData = {"name": "NEIGHBOURS_HOME", "42": "TOWN"}
	neighbour_homeSpawn = [[4, 2]]
	farm = [["+==============X===============+"],
			["ǁ*************▒..##############ǁ"],
			["ǁ*************▒..#............#ǁ"],
			["ǁ*************▒...............#ǁ"],
			["ǁ*************▒.Q#............#ǁ"],
			["ǁ*************▒..#............#ǁ"],
			["ǁ*************▒..##############ǁ"],
			["ǁ*************▒.▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ǁ"],
			["ǁ*************▒.▒**************ǁ"],
			["ǁ*************▒.▒**************ǁ"],
			["ǁ*************▒.▒**************ǁ"],
			["ǁ*************▒.▒**************ǁ"],
			["ǁ*************▒.▒**************ǁ"],
			["+==============X===============+"]]
	farmData = {"name": "FARMS", "1215": "TOWN"}
	farmSpawn = [[1, 15], [12,15]]
	farmMobs = {"g": [[2, 25], [3, 29], [4, 27], [5, 22]], "r": [[2, 23]]}
	currentMap = town
	currentMapData = townData
	currentMapSpawn = townSpawn
	currentMapMobs = None
	currentMapChest = None

def loadNextMap(yCoord, xCoord, spawnLocation):
	z = str(str(yCoord) + str(xCoord))
	if Maps.currentMapData[z] == "TOWN":
		Maps.currentMap = Maps.town
		Maps.currentMapData = Maps.townData
		Maps.currentMapSpawn = Maps.townSpawn
		Maps.currentMapMobs = None
		Maps.currentMapChest = None
	elif Maps.currentMapData[z] == "HOME":
		Maps.currentMap = Maps.home
		Maps.currentMapData = Maps.homeData
		Maps.currentMapSpawn = Maps.homeSpawn
		Maps.currentMapMobs = None
		Maps.currentMapChest = Maps.homeChest
	elif Maps.currentMapData[z] == "NEIGHBOURS_HOME":
		Maps.currentMap = Maps.neighbour_home
		Maps.currentMapData = Maps.neighbour_homeData
		Maps.currentMapSpawn = Maps.neighbour_homeSpawn
		Maps.currentMapMobs = None
		Maps.currentMapChest = None
	elif Maps.currentMapData[z] == "FARMS":
		Maps.currentMap = Maps.farm
		Maps.currentMapData = Maps.farmData
		Maps.currentMapSpawn = Maps.farmSpawn
		Maps.currentMapMobs = Maps.farmMobs
		Maps.currentMapChest = None
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
	if Maps.currentMapData["name"] == "TOWN":
		if yCoord == 1 and xCoord == 15:  # FARM
			spawnLocation = 1
		elif yCoord == 5 and xCoord == 19:  # NEIGHBOUR
			spawnLocation = 0
		elif yCoord == 11 and xCoord == 19:  # HOME
			spawnLocation = 0
	elif Maps.currentMapData["name"] == "HOME":
		spawnLocation = 2  # TOWN
	elif Maps.currentMapData["name"] == "NEIGHBOURS_HOME":
		spawnLocation = 1  # TOWN
	elif Maps.currentMapData["name"] == "FARMS":
		spawnLocation = 0
	return spawnLocation

def respawnPlayer(spawnLocation):
	y = Maps.currentMapSpawn[spawnLocation][0]
	x = Maps.currentMapSpawn[spawnLocation][1]
	return y, x

def mobKill(kill, yMob, xMob):
	i = 0
	zMob = str(str(yMob) + str(xMob))
	for item in Maps.currentMapMobs.items():
		# if Maps.currentMapData[key] in mobs.mobIcons.mobs:
		while i < len(item[1]):
			#print(item[1][i][0], item[1][i][1])
			z = str(str(item[1][i][0]) + str(item[1][i][1]))
			if z == zMob:
				if Maps.currentMapData["name"] == "FARMS":
					del Maps.farmMobs[kill][i]
					break
			i += 1
