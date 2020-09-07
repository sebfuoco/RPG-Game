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
	elders_homeName = "ELDERS HOME"
	farmName = "FARMS"
	forestName = "FOREST"
	townSquareName = "TOWN SQUARE"
	castleGateName = "CASTLE GATE"
	castleName = "CASTLE"
	castleBasementName = "CASTLE BASEMENT"
	castleThroneName = "THRONE ROOM"
	fieldName = "FIELD"
	caveName = "CAVE"
	westLuciaName = "WEST LUCIA"
	kingStarPubName = "KING STAR PUB"
	allMapNames = [townName, homeName, elders_homeName, farmName, forestName, townSquareName, castleGateName, castleName, fieldName, caveName, westLuciaName, kingStarPubName]

class Maps:
	from MapSettings import merchants
	town = [["+==============X===============+"],
			["ǁ..............................ǁ"],
			["ǁ..###..............▒▒▒▒▒▒▒▒▒▒.ǁ"],
			["ǁ..#˄#..............▒˄˄˄˄˄˄˄˄▒.ǁ"],
			["ǁ..#.#..............▒˄˄˄˄˄˄˄˄▒.ǁ"],
			["ǁ...................X˄˄˄˄˄˄˄˄▒.ǁ"],
			["ǁ..###..............▒˄˄˄˄˄˄˄˄▒.ǁ"],
			["ǁ..#˄#..............▒▒▒▒▒▒▒▒▒▒.ǁ"],
			["ǁ..#.#.........................ǁ"],
			["ǁ...................▒▒▒▒▒▒▒▒▒▒.ǁ"],
			["ǁ..###..............▒˄˄˄˄˄˄˄˄▒.ǁ"],
			["ǁ..#˄#..............X˄˄˄˄˄˄˄˄▒.ǁ"],
			["ǁ..#.#..............▒▒▒▒▒▒▒▒▒▒.ǁ"],
			["ǁ..............................ǁ"],
			["+==============================+"]]
	townData = {"1119": mapNames.homeName, "115": mapNames.farmName, "519": mapNames.elders_homeName}
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

	elders_home = [["+==============================+"],
				   ["ǁ##############################ǁ"],
				   ["ǁ#............................#ǁ"],
				   ["ǁ#............................#ǁ"],
				   ["ǁX............................#ǁ"],
				   ["ǁ#............................#ǁ"],
				   ["ǁ#............................#ǁ"],
				   ["ǁ#............................#ǁ"],
				   ["ǁ##############################ǁ"],
				   ["+==============================+"]]
	elders_homeData = {"42": mapNames.townName}
	elders_homeSpawn = [[4, 2, 1]]
	elders_homeQuest = initQuest(mapNames.elders_homeName)
	allElderHome = [mapNames.elders_homeName, elders_home, elders_homeData, elders_homeSpawn, None, None, elders_homeQuest, None, None]

	farm = [["+==============X===============+"],
			["ǁ*************▒..##############ǁ"],
			["ǁ*************▒..#............#ǁ"],
			["ǁ*************▒...............#ǁ"],
			["ǁ*************▒..#............#ǁ"],
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
			  ["ǁ.....****...**...........*****ǁ"],
			  ["ǁ.*****************************ǁ"],
			  ["ǁ.*****************************ǁ"],
			  ["ǁ.....****...**...........*****ǁ"],
			  ["ǁ..............................ǁ"],
			  ["ǁ*****************.............ǁ"],
			  ["ǁ********.......************...ǁ"],
			  ["ǁ**.........**..*******....**..ǁ"],
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
				  ["ǁ#.#.#.#.#............#.#.#.#.#ǁ"],
				  ["ǁ..............................ǁ"],
				  ["ǁ#########............#########ǁ"],
				  ["ǁ#.#.#.#.#............#.#.#.#.#ǁ"],
				  ["ǁ...........▒▒▒▒▒▒▒▒...........ǁ"],
				  ["X...........▒▒▒˄˄▒▒▒...........X"],
				  ["ǁ...........▒▒▒▒.▒▒▒...........ǁ"],
				  ["ǁ..............................ǁ"],
				  ["ǁ..............................ǁ"],
				  ["ǁ..............................ǁ"],
				  ["ǁ..............................ǁ"],
				  ["ǁ..............................ǁ"],
				  ["+==============X===============+"]]
	townSquareData = {"115": mapNames.castleGateName, "71": mapNames.fieldName, "730": mapNames.westLuciaName, "1315": mapNames.forestName}
	townSquareSpawn = [[1, 15, 1], [7, 1, 1], [7, 30, 0], [13, 15, 0]]
	townSquareQuest = initQuest(mapNames.townSquareName)
	townSquareInfo = initInfo(mapNames.townSquareName)
	allTownSquare = [mapNames.townSquareName, townSquare, townSquareData, townSquareSpawn, None, None, townSquareQuest, townSquareInfo, merchants.townSquareMerchant]

	castleGate = [["+==============X===============+"],
				  ["ǁ..............................ǁ"],
				  ["ǁ..............................ǁ"],
				  ["ǁ▒▒▒▒▒▒▒▒▒▒▒▒▒▒.▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ǁ"],
				  ["ǁ             ...              ǁ"],
				  ["ǁ             ...              ǁ"],
				  ["ǁ             ...              ǁ"],
				  ["ǁ             ...              ǁ"],
				  ["+==============X===============+"]]
	castleGateData = {"115": mapNames.castleName, "715": mapNames.townSquareName}
	castleGateSpawn = [[1, 15, 2], [7, 15, 0]]
	castleGateInfo = initInfo(mapNames.castleGateName)
	allCastleGate = [mapNames.castleGateName, castleGate, castleGateData, castleGateSpawn, None, None, None, castleGateInfo, None]

	castle = [["+==============X===============+"],
			  ["ǁ............▒...▒.............ǁ"],
			  ["ǁ..............................ǁ"],
			  ["ǁ............▒...▒.............ǁ"],
			  ["ǁ..............................ǁ"],
			  ["ǁ............▒...▒.........▒▒.▒ǁ"],
			  ["ǁ..........................▒▒X▒ǁ"],
			  ["ǁ............▒...▒.........▒▒▒▒ǁ"],
			  ["+==============X===============+"]]
	castleData = {"115": mapNames.castleThroneName, "529": mapNames.castleBasementName, "715": mapNames.castleGateName}
	castleSpawn = [[1, 15, 0], [5, 29, 0], [7, 15, 0]]
	castleMobs = initMob(mapNames.castleName)
	allCastle = [mapNames.castleName, castle, castleData, castleSpawn, castleMobs, None, None,
					 None, None]

	castleBasement = [["+=================+"],
					  ["ǁ.▒..▒..▒..▒..▒▒▒▒ǁ"],
					  ["ǁ.............▒▒X▒ǁ"],
					  ["ǁ.............▒▒.▒ǁ"],
					  ["ǁ▒▒▒▒▒▒▒▒▒▒▒..▒..▒ǁ"],
					  ["ǁ.................ǁ"],
					  ["ǁ.................ǁ"],
					  ["ǁ.▒..▒..▒..▒..▒..▒ǁ"],
					  ["+=================+"]]
	castleBasementData = {"316": mapNames.castleName}
	castleBasementSpawn = [[3, 16, 1]]
	castleBasementChest = initChest(mapNames.castleBasementName)
	allCastleBasement = [mapNames.castleBasementName, castleBasement, castleBasementData, castleBasementSpawn, None, castleBasementChest, None,
				 None, None]

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

	westLucia = [["+==============================+"],
				 ["ǁ..............................ǁ"],
				 ["ǁ..............................ǁ"],
				 ["ǁ.▒▒▒▒▒▒▒▒▒▒▒...▒▒▒▒▒▒▒▒▒▒▒....ǁ"],
				 ["ǁ.▒˄˄˄˄˄˄˄˄˄▒...▒˄˄˄˄˄˄˄˄˄▒....ǁ"],
				 ["ǁ.▒˄˄˄˄˄˄˄˄˄▒...▒˄˄˄˄˄˄˄˄˄▒....ǁ"],
				 ["ǁ.▒▒▒▒▒▒▒▒▒▒▒...▒▒▒▒▒▒▒▒▒▒▒....ǁ"],
				 ["X..............................X"],
				 ["ǁ.▒▒▒▒▒▒▒▒▒▒▒...▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ǁ"],
				 ["ǁ.▒˄˄˄˄˄˄˄˄˄▒...X˄˄˄˄˄˄˄˄˄˄˄˄˄▒ǁ"],
				 ["ǁ.▒▒▒▒▒▒▒▒▒▒▒...▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ǁ"],
				 ["+==============================+"]]
	westLuciaData = {"71": mapNames.townSquareName, "915": mapNames.kingStarPubName}
	westLuciaSpawn = [[7, 1, 2], [9, 15, 0]]
	allWestLucia = [mapNames.westLuciaName, westLucia, westLuciaData, westLuciaSpawn, None, None, None, None, None]

	kingStarPub = [["+======================+"],
				   ["ǁ...▒...▒...▒..........ǁ"],
				   ["ǁ...▒...▒...▒..........ǁ"],
				   ["ǁ▒.▒▒▒.▒▒▒.▒▒▒▒▒...▒▒▒▒ǁ"],
				   ["ǁ......................ǁ"],
				   ["ǁ......................ǁ"],
				   ["ǁ▒▒▒▒▒▒▒▒▒▒▒▒▒▒...▒▒▒▒▒ǁ"],
				   ["X.................▒....ǁ"],
				   ["ǁ......................ǁ"],
				   ["+======================+"]]
	kingStarPubData = {"71": mapNames.westLuciaName}
	kingStarPubSpawn = [[7, 1, 1]]
	kingStarPubMobs = initMob(mapNames.kingStarPubName)
	kingStarPubInfo = initInfo(mapNames.kingStarPubName)
	allKingStarPub = [mapNames.kingStarPubName, kingStarPub, kingStarPubData, kingStarPubSpawn, kingStarPubMobs, None, None, kingStarPubInfo, None]

	# allMap template [mapName, map, mapData, mapSpawn, mapMobs, mapChests, mapQuest, mapInfo, mapMerchants]
	allMaps = [allTown, allHome, allElderHome, allFarm, allForest, allTownSquare, allCastleGate, allCastle, allCastleBasement, allField, allCave, allWestLucia, allKingStarPub]

	quickStartMap = [[town, mapNames.townName, townData, townSpawn, None, None, None, None, merchants.townMerchant],
					 [townSquare, mapNames.townSquareName, townSquareData, townSquareSpawn, None, None, townSquareQuest, townSquareInfo, merchants.townSquareMerchant],
					 [castle, mapNames.castleName, castleData, castleSpawn, castleMobs, None, None, None, None]]
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
