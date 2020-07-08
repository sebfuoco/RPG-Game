class Maps:
	town = [["+==============X===============+"],
			["ǁ..............................ǁ"],
			["ǁ..###..............##########.ǁ"],
			["ǁ..#˄#..............#˄˄˄˄˄˄˄˄#.ǁ"],
			["ǁ..#M#..............#˄˄˄˄˄˄˄˄#.ǁ"],
			["ǁ...................X˄˄˄˄˄˄˄˄#.ǁ"],
			["ǁ..###..............#˄˄˄˄˄˄˄˄#.ǁ"],
			["ǁ..#˄#..............##########.ǁ"],
			["ǁ..#M#.........................ǁ"],
			["ǁ...................##########.ǁ"],
			["ǁ..###..............#˄˄˄˄˄˄˄˄#.ǁ"],
			["ǁ..#˄#..............X˄˄˄˄˄˄˄˄#.ǁ"],
			["ǁ..#M#..............##########.ǁ"],
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
	homeData = {"name": "HOME", "42": "TOWN", "329":"POTION", "429": "POTION"}
	homeSpawn = [[4, 2]]
	neighbour_home = [["+==============================+"],
					  ["ǁ##############################ǁ"],
					  ["ǁ#............................#ǁ"],
					  ["ǁ#............................#ǁ"],
					  ["ǁX............................#ǁ"],
					  ["ǁ#............................#ǁ"],
					  ["ǁ#............................#ǁ"],
					  ["ǁ#............................#ǁ"],
					  ["ǁ#............................#ǁ"],
					  ["ǁ#............................#ǁ"],
					  ["ǁ#............................#ǁ"],
					  ["ǁ#............................#ǁ"],
					  ["ǁ##############################ǁ"],
					  ["+==============================+"]]
	neighbour_homeData = {"name": "NEIGHBOURS_HOME", "42": "TOWN", "329": "POTION", "429": "POTION"}
	neighbour_homeSpawn = [[4, 2]]
	farm = [["+==============X===============+"],
			["ǁ..............................ǁ"],
			["ǁ..............................ǁ"],
			["ǁ..............................ǁ"],
			["ǁ..............................ǁ"],
			["ǁ..............................ǁ"],
			["ǁ..............................ǁ"],
			["ǁ..............................ǁ"],
			["ǁ..............................ǁ"],
			["ǁ..............................ǁ"],
			["ǁ..............................ǁ"],
			["ǁ..............................ǁ"],
			["ǁ..............................ǁ"],
			["+==============X===============+"]]
	farmData = {"name": "FARM", "42": "TOWN", "329": "POTION", "429": "POTION"}
	farmSpawn = [[1, 15], [12,15]]
	currentMap = town
	currentMapData = townData
	currentMapSpawn = townSpawn

def findPos(yCoord, xCoord):
	i = 0
	while i < len(Maps.currentMap):
		for position, char in enumerate(Maps.currentMap[i][0]):
			if char == '@':
				xCoord = position
				yCoord = i
		i += 1
	print(yCoord, xCoord)

def loadNextMap(spawnLocation, yCoord, xCoord):
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
	elif Maps.currentMapData[z] == "FARM":
		Maps.currentMap = Maps.farm
		Maps.currentMapData = Maps.farmData
		Maps.currentMapSpawn = Maps.farmSpawn
	return spawnLocation

def detectCollision(yCoord, xCoord):
	try:
		if Maps.currentMap[yCoord][0].index(".", xCoord, xCoord+1):
			return True
	except ValueError:
		try:
			if Maps.currentMap[yCoord][0].index("X", xCoord, xCoord + 1):
				return "loadMap"
		except ValueError:
			try:
				if Maps.currentMap[yCoord][0].index("M", xCoord, xCoord + 1):
					return True
			except ValueError:
				return False


def currentPosition(self, yCoord, xCoord):
	previousPosition = Maps.currentMap[yCoord][0][xCoord]
	self.addstr(yCoord, xCoord, previousPosition)
	self.refresh()

def movePlayer(self, yCoord, xCoord):
	self.addstr(yCoord, xCoord, "@")
	self.refresh()

def respawnData(spawnLocation):
	if Maps.currentMapData["name"] == "TOWN":
		spawnLocation = 0
	elif Maps.currentMapData["name"] == "HOME":
		spawnLocation = 2
	elif Maps.currentMapData["name"] == "NEIGHBOURS_HOME":
		spawnLocation = 1
	elif Maps.currentMapData["name"] == "FARM":
		spawnLocation = 1
	return spawnLocation

def respawnPlayer(spawnLocation):
	y = Maps.currentMapSpawn[spawnLocation][0]
	x = Maps.currentMapSpawn[spawnLocation][1]
	spawnLocation = respawnData(spawnLocation)
	return y, x, spawnLocation
