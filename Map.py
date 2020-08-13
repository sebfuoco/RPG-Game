from Items import *

def initQuest(i):
	from quest import quest
	output = quest.allQuests[i]
	return output

def initInfo(i):
	from quest import info
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
	allTown = [mapNames.townName, town, townData, townSpawn, None, None, None, None]
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
	homeChest = {Items.HealthPotion['name']: [Items.HealthPotion, [3, 29]],
				 Items.ManaPotion['name']: [Items.ManaPotion, [4, 29]]}
	allHome = [mapNames.homeName, home, homeData, homeSpawn, None, homeChest, None, None]
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
	neighbour_homeQuest = initQuest(0)

	allNeighbour = [mapNames.neighbour_homeName, neighbour_home, neighbour_homeData, neighbour_homeSpawn, None, None, neighbour_homeQuest, None]
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
	farmMobs = {"g": [[2, 23], [2, 25], [3, 29], [4, 27], [5, 22]]}
	farmInfo = initInfo(0)
	farmQuest = initQuest(1)
	allFarm = [mapNames.farmName, farm, farmData, farmSpawn, farmMobs, None, farmQuest, farmInfo]
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
	forestChest = {Items.HealthPotion['name']: [Items.HealthPotion, [9, 23]],
				   Items.Antidote['name']: [Items.Antidote, [5, 11]]}
	forestMobs = {"s": [[9, 7], [9, 14], [9, 24], [11, 3]], "r": [[6, 18], [12, 5]], "q": [[1, 14]]}
	allForest = [mapNames.forestName, forest, forestData, forestSpawn, forestMobs, forestChest, None, None]
	townSquare = [["+==============X===============+"],
				  ["ǁ..............................ǁ"],
				  ["ǁ..............................ǁ"],
				  ["ǁ..............................ǁ"],
				  ["ǁ..............................ǁ"],
				  ["ǁ..............................ǁ"],
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
	townSquareInfo = initInfo(1)
	allTownSquare = [mapNames.townSquareName, townSquare, townSquareData, townSquareSpawn, None, None, None, townSquareInfo]
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
	castleGateInfo = initInfo(2)
	allCastleGate = [mapNames.castleGateName, castleGate, castleGateData, castleGateSpawn, None, None, None, castleGateInfo]
	field = [["+==============================+"],
			 ["ǁ................*.*.*.*.......ǁ"],
			 ["ǁ.................*.*.*.*......ǁ"],
			 ["X..............................X"],
			 ["ǁ.................*.*.*.*......ǁ"],
			 ["ǁ................*.*.*.*.......ǁ"],
			 ["+==============================+"]]
	fieldData = {"31": mapNames.caveName, "330": mapNames.townSquareName}
	fieldSpawn = [[3, 1], [3, 30, 1]]
	allField = [mapNames.fieldName, field, fieldData, fieldSpawn, None, None, None,
					 None]
	cave = [["+==============================+"],
			 ["ǁ.....ǁ.......................ǁ"],
			 ["ǁ.............................ǁ"],
			 ["ǁ===========================..ǁ"],
			 ["ǁ.............................ǁ"],
			 ["ǁ.............................ǁ"],
			 ["ǁ..===========================ǁ"],
			 ["ǁ.................ǁǁ..........ǁ"],
			 ["ǁ..ǁǁǁ.....ǁǁǁǁ.........ǁǁ....ǁ"],
			 ["ǁ..ǁǁǁ.....ǁǁǁǁ.........ǁǁ....ǁ"],
			 ["ǁ..ǁǁǁ............ǁǁ....ǁǁ....X"],
			 ["+==============================+"]]
	caveData = {"31": mapNames.caveName, "330": mapNames.townSquareName}
	caveSpawn = [[3, 1], [3, 30, 1]]
	allCave = [mapNames.caveName, cave, caveData, caveSpawn, None, None, None,
					 None]

	allMaps = [allTown, allHome, allNeighbour, allFarm, allForest, allTownSquare, allCastleGate, allField]

	quickStartMap = [[town, mapNames.townName, townData, townSpawn, None, None, None, None],
					 [townSquare, mapNames.townSquareName, townSquareData, townSquareSpawn, None, None, None, townSquareInfo]]
	i = 0
	currentMap = quickStartMap[i][0]
	currentMapName = quickStartMap[i][1]
	currentMapData = quickStartMap[i][2]
	currentMapSpawn = quickStartMap[i][3]
	currentMapMobs = quickStartMap[i][4]
	currentMapChest = quickStartMap[i][5]
	currentMapQuest = quickStartMap[i][6]
	currentMapInfo = quickStartMap[i][7]
