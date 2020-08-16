def initMob(i):
	from MapSettings import mobs
	output = mobs.allMobs[i]
	return output

def initChest(i):
	from MapSettings import chests
	output = chests.allChest[i]
	return output

def initQuest(i):
	from MapSettings import quest
	output = quest.allQuests[i]
	return output

def initInfo(i):
	from MapSettings import info
	output = info.allInfo[i]
	return output

class mapNames:
	townName = "TOWN"
	homeName = "HOME"
	neighbour_homeName = "NEIGHBOURS HOME"
	farmName = "FARMS"
	forestName = "FOREST"
	townSquareName = "TOWN SQUARE"
	castleGateName = "CASTLE GATE"
	fieldName = "FIELD"
	caveName = "CAVE"

class Maps:
	from MapSettings import merchants
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
	townData = {"1119": mapNames.homeName, "115": mapNames.farmName, "519": mapNames.neighbour_homeName}
	#  yCoord, xCoord, spawnLocation
	townSpawn = [[1, 15, 1], [5, 19, 0], [11, 19, 0]]
	allTown = [mapNames.townName, town, townData, townSpawn, None, None, None, None, merchants.townMerchant]

	home = [["+==============================+"],
			["ǁ##############################ǁ"],
			["ǁ#............................#ǁ"],
			["ǁ#............................#ǁ"],
			["ǁX............................#ǁ"],
			["ǁ#............................#ǁ"],
			["ǁ##############################ǁ"],
			["+==============================+"]]
	homeData = {"42": mapNames.townName}
	homeSpawn = [[4, 2, 2]]
	homeChest = initChest(mapNames.homeName)
	allHome = [mapNames.homeName, home, homeData, homeSpawn, None, homeChest, None, None, None]

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
	neighbour_homeData = {"42": mapNames.townName}
	neighbour_homeSpawn = [[4, 2, 1]]
	neighbour_homeQuest = initQuest(mapNames.neighbour_homeName)
	allNeighbour = [mapNames.neighbour_homeName, neighbour_home, neighbour_homeData, neighbour_homeSpawn, None, None, neighbour_homeQuest, None, None]

	farm = [["+==============X===============+"],
			["ǁ*************▒.I##############ǁ"],
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
	farmData = {"1215": mapNames.townName, "115": mapNames.forestName}
	farmSpawn = [[1, 15, 1], [12, 15, 0]]
	farmMobs = initMob(mapNames.farmName)
	farmInfo = initInfo(mapNames.farmName)
	farmQuest = initQuest(mapNames.farmName)
	allFarm = [mapNames.farmName, farm, farmData, farmSpawn, farmMobs, None, farmQuest, farmInfo, None]

	forest = [["+==============X===============+"],
			  ["ǁ..............................ǁ"],
			  ["ǁ.....****...***..........*****ǁ"],
			  ["ǁ.*****************************ǁ"],
			  ["ǁ.*****************************ǁ"],
			  ["ǁ.....****...***..........*****ǁ"],
			  ["ǁ..............................ǁ"],
			  ["ǁ*****************.............ǁ"],
			  ["ǁ********......*************...ǁ"],
			  ["ǁ**.........**.********....**..ǁ"],
			  ["ǁ**.........**.....*****...**..ǁ"],
			  ["ǁ**.*************..*****...**..ǁ"],
			  ["ǁ**.............*..............ǁ"],
			  ["+==============X===============+"]]
	forestData = {"115": mapNames.townSquareName, "1215": mapNames.farmName}
	forestSpawn = [[1, 15, 3], [12, 15, 0]]
	forestChest = initChest(mapNames.forestName)
	forestMobs = initMob(mapNames.forestName)
	allForest = [mapNames.forestName, forest, forestData, forestSpawn, forestMobs, forestChest, None, None, None]

	townSquare = [["+==============X===============+"],
				  ["ǁ#########............#########ǁ"],
				  ["ǁ#I#I#I#I#............#I#I#I#I#ǁ"],
				  ["ǁ..............................ǁ"],
				  ["ǁ#########............#########ǁ"],
				  ["ǁ#M#M#M#M#............#I#I#I#Q#ǁ"],
				  ["ǁ...........▒▒▒▒▒▒▒▒...........ǁ"],
				  ["X...........▒▒▒..▒▒▒...........X"],
				  ["ǁ...........▒▒▒▒I▒▒▒...........ǁ"],
				  ["ǁ..............................ǁ"],
				  ["ǁ..............................ǁ"],
				  ["ǁ..............................ǁ"],
				  ["ǁ..............................ǁ"],
				  ["ǁ..............................ǁ"],
				  ["+==============X===============+"]]
	townSquareData = {"115": mapNames.castleGateName, "71": mapNames.fieldName, "1315": mapNames.forestName}
	townSquareSpawn = [[1, 15, 1], [7, 1, 1], [7, 30], [13, 15, 0]]
	townSquareInfo = initInfo(mapNames.townSquareName)
	allTownSquare = [mapNames.townSquareName, townSquare, townSquareData, townSquareSpawn, None, None, None, townSquareInfo, merchants.townSquareMerchant]

	castleGate = [["+==============X===============+"],
				  ["ǁ..............................ǁ"],
				  ["ǁ..............................ǁ"],
				  ["ǁ▒▒▒▒▒▒▒▒▒▒▒▒▒▒.▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ǁ"],
				  ["ǁ~~~~~~~~~~~~~.I.~~~~~~~~~~~~~~ǁ"],
				  ["ǁ~~~~~~~~~~~~~...~~~~~~~~~~~~~~ǁ"],
				  ["ǁ~~~~~~~~~~~~~...~~~~~~~~~~~~~~ǁ"],
				  ["ǁ~~~~~~~~~~~~~...~~~~~~~~~~~~~~ǁ"],
				  ["+==============X===============+"]]
	castleGateData = {"715": mapNames.townSquareName}
	castleGateSpawn = [[1, 15], [7, 15, 0]]
	castleGateInfo = initInfo(mapNames.castleGateName)
	allCastleGate = [mapNames.castleGateName, castleGate, castleGateData, castleGateSpawn, None, None, None, castleGateInfo, None]

	field = [["+==============================+"],
			 ["ǁ................*.*.*.*.......ǁ"],
			 ["ǁ.................*.*.*.*......ǁ"],
			 ["X..............................X"],
			 ["ǁ.................*.*.*.*......ǁ"],
			 ["ǁ................*.*.*.*.......ǁ"],
			 ["+==============================+"]]
	fieldData = {"31": mapNames.caveName, "330": mapNames.townSquareName}
	fieldSpawn = [[3, 1, 0], [3, 30, 1]]
	fieldMobs = initMob(mapNames.fieldName)
	allField = [mapNames.fieldName, field, fieldData, fieldSpawn, fieldMobs, None, None, None, None]

	cave = [["+=============================+"],
			["ǁ.....ǁ.......................ǁ"],
			["ǁ.............................ǁ"],
			["ǁ============================.ǁ"],
			["ǁ.............................ǁ"],
			["ǁ.............................ǁ"],
			["ǁ.============================ǁ"],
			["ǁ.................ǁǁ..........ǁ"],
			["ǁ..ǁǁǁ.....ǁǁǁǁ.........ǁǁ....ǁ"],
			["ǁ..ǁǁǁ.....ǁǁǁǁ.........ǁǁ....ǁ"],
			["ǁ..ǁǁǁ............ǁǁ....ǁǁ....X"],
			["+=============================+"]]
	caveData = {"1029": mapNames.fieldName}
	caveSpawn = [[10, 29, 0]]
	caveMobs = initMob(mapNames.caveName)
	allCave = [mapNames.caveName, cave, caveData, caveSpawn, caveMobs, None, None, None, None]

	allMaps = [allTown, allHome, allNeighbour, allFarm, allForest, allTownSquare, allCastleGate, allField, allCave]

	quickStartMap = [[town, mapNames.townName, townData, townSpawn, None, None, None, None, merchants.townMerchant],
					 [townSquare, mapNames.townSquareName, townSquareData, townSquareSpawn, None, None, None, townSquareInfo, merchants.townSquareMerchant]]
	i = 1
	currentMap = quickStartMap[i][0]
	currentMapName = quickStartMap[i][1]
	currentMapData = quickStartMap[i][2]
	currentMapSpawn = quickStartMap[i][3]
	currentMapMobs = quickStartMap[i][4]
	currentMapChest = quickStartMap[i][5]
	currentMapQuest = quickStartMap[i][6]
	currentMapInfo = quickStartMap[i][7]
	currentMapMerchant = quickStartMap[i][8]
