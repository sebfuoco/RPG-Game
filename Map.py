from Items import *

class Maps:
	class mapNames:
		townName = "TOWN"
		homeName = "HOME"
		neighbour_homeName = "NEIGHBOURS HOME"
		farmName = "FARMS"
		forestName = "FOREST"
		townSquareName = "TOWN SQUARE"
		castleGateName = "CASTLE GATE"

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
	townSpawn = [[1, 15], [5, 19], [11, 19]]
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
	homeSpawn = [[4, 2]]
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
	neighbour_homeSpawn = [[4, 2]]
	neighbour_homeQuest = {"429": [["DELIVER MESSAGE TO TOWN ELDER",
									f"HELLO YOUNG ONE, I AM TOO WEAK TO DELIVER THIS MESSAGE TO THE TOWN ELDER, CURRENTLY IN THE {mapNames.townSquareName}. "
									f"I WOULD BE DELIGHTED IF YOU SENT IT TO HIM.", [mapNames.townSquareName, [8, 16],
																					 {"GOLD": 10, "XP": 10,
																					  "REWARD": [
																						  Items.SuperHealthPotion,
																						  1]}]],
								   ["DEFEAT THE SKELETON LORD",
									f"AH YOUR BACK! I TAKE IT HE TOLD YOU OF THE DANGERS WITHIN THE CAVES. "
									f"THE SKELETON LORD IS FEARSOME BUT HE IS WEAK TO LIGHT, USE THIS KNOWLEDGE TO DEFEAT HIM!",
									[mapNames.townSquareName, [8, 16],
									 {"GOLD": 10, "XP": 10, "REWARD": Items.HolyWater}]]]}
	allNeighbour = [mapNames.neighbour_homeName, neighbour_home, neighbour_homeData, neighbour_homeSpawn, None, None, neighbour_homeQuest, None]
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
	farmData = {"1215": mapNames.townName, "115": mapNames.forestName}
	farmSpawn = [[1, 15], [12, 15]]
	farmMobs = {"g": [[2, 23], [2, 25], [3, 29], [4, 27], [5, 22]]}
	farmQuest = {"416": [["KILL GOBLINS",
						  f"I NEED YOUR HELP! THERE ARE GOBLINS IN MY BARN, PLEASE GET RID OF THEM FOR ME!.",
						  [mapNames.farmName, [4, 16],
						   {"GOLD": 10, "XP": 10, "REWARD": [Equipment.Knife, 1]}]]]}
	allFarm = [mapNames.farmName, farm, farmData, farmSpawn, farmMobs, None, farmQuest, None]
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
	forestData = {"1215": mapNames.farmName, "115": mapNames.townSquareName}
	forestSpawn = [[1, 15], [12, 15]]
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
	townSquareData = {"1315": mapNames.forestName, "115": mapNames.castleGateName}
	townSquareSpawn = [[1, 15], [13, 15], [7, 1], [7, 31]]
	townSquareInfo = ["TOWN ELDER", "AHH FINALLY A MESSAGE... OH YOU DON'T HAVE ONE FOR ME? NEVERMIND THEN",
					  "THAT LETTER YOU ARE HOLDING, GIVE IT TO ME... OH MY THIS IS BAD! THE SKELETON LORD HAS RISEN WITHIN THE CAVES, "
					  "IF WE DO NOT ACT NOW OUR TOWN WILL BE IN DANGER!", "GO BACK TO YOUR HOME TOWN AND TALK TO THE ELDER, HE WILL KNOW WHAT TO DO",
					  "I HAVE NOTHING TO TELL YOU YOUNG ONE, YOU MUST ADVENTURE ON YOUR OWN", 1]
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
	castleGateSpawn = [[1, 15], [7, 15]]
	castleGateInfo = ["CASTLE GUARD", "SORRY, I CAN'T ALLOW YOU IN WITHOUT THE KINGS PERMISSION", 1]
	allCastleGate = [mapNames.castleGateName, castleGate, castleGateData, castleGateSpawn, None, None, None, castleGateInfo]

	allMaps = [allTown, allHome, allNeighbour, allFarm, allForest, allTownSquare, allCastleGate]
	currentMap = town
	currentMapName = mapNames.townName
	currentMapData = townData
	currentMapSpawn = townSpawn
	currentMapMobs = None
	currentMapChest = None
	currentMapQuest = None
	currentMapInfo = None
