from Items import *

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
	townSpawn = [[1,15],[5,19],[11,19]]
	home = [["+==============================+"],
			["ǁ##############################ǁ"],
			["ǁ#............................#ǁ"],
			["ǁ#...........................C#ǁ"],
			["ǁX...........................C#ǁ"],
			["ǁ#............................#ǁ"],
			["ǁ##############################ǁ"],
			["+==============================+"]]
	homeData = {"name": "HOME", "42": "TOWN", "329": Items.HealthPotion, "429": Items.ManaPotion}
	homeSpawn = [[4, 2]]
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
	neighbour_homeData = {"name": "NEIGHBOURS_HOME", "42": "TOWN", "329": "POTION", "429": "POTION"}
	neighbour_homeSpawn = [[4, 2]]
	farm = [["+==============X===============+"],
			["ǁ*************▒..##############ǁ"],
			["ǁ*************▒..#.......g....#ǁ"],
			["ǁ*************▒..............g#ǁ"],
			["ǁ*************▒.Q#.........g..#ǁ"],
			["ǁ*************▒..#....g.......#ǁ"],
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
	currentMap = town
	currentMapData = townData
	currentMapSpawn = townSpawn

def loadNextMap(yCoord, xCoord, spawnLocation):
	z = str(str(yCoord) + str(xCoord))
	if Maps.currentMapData[z] == "TOWN":
		Maps.currentMap = Maps.town
		Maps.currentMapData = Maps.townData
		Maps.currentMapSpawn = Maps.townSpawn
	elif Maps.currentMapData[z] == "HOME":
		Maps.currentMap = Maps.home
		Maps.currentMapData = Maps.homeData
		Maps.currentMapSpawn = Maps.homeSpawn
	elif Maps.currentMapData[z] == "NEIGHBOURS_HOME":
		Maps.currentMap = Maps.neighbour_home
		Maps.currentMapData = Maps.neighbour_homeData
		Maps.currentMapSpawn = Maps.neighbour_homeSpawn
	elif Maps.currentMapData[z] == "FARMS":
		Maps.currentMap = Maps.farm
		Maps.currentMapData = Maps.farmData
		Maps.currentMapSpawn = Maps.farmSpawn
	yCoord, xCoord = respawnPlayer(spawnLocation)
	return yCoord, xCoord

def detectCollision(yCoord, xCoord):
	if Maps.currentMap[yCoord][0][xCoord] in "X":
		return "loadMap"
	elif Maps.currentMap[yCoord][0][xCoord] in ["."]:
		return True
	elif Maps.currentMap[yCoord][0][xCoord] in ["C"]:
		return "Chest"
	elif Maps.currentMap[yCoord][0][xCoord] in ["M"]:
		return "Merchant"
	elif Maps.currentMap[yCoord][0][xCoord] in ["Q"]:
		return "Quest"

def currentPosition(self, yCoord, xCoord):
	previousPosition = Maps.currentMap[yCoord][0][xCoord]
	if previousPosition == "M":
		self.addstr(yCoord, xCoord, previousPosition, curses.color_pair(12))
	elif previousPosition == "Q":
		self.addstr(yCoord, xCoord, previousPosition, curses.color_pair(7))
	else:
		self.addstr(yCoord, xCoord, previousPosition)
	self.refresh()

def movePlayer(self, yCoord, xCoord):
	self.addstr(yCoord, xCoord, "@")
	self.refresh()

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
