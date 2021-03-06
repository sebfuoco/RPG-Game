from Map import mapNames
from Items import Items, Equipment, QuestItems
from mobs import mobList

class quest:
	elders_homeQuest = {"429": [0, ["DELIVER MESSAGE TO TOWN ELDER", [4, 29],
									f"HELLO YOUNG ONE, I AM TOO WEAK TO DELIVER THIS MESSAGE TO THE TOWN ELDER, CURRENTLY IN THE {mapNames.townSquareName}. "
									f"I WOULD BE DELIGHTED IF YOU SENT IT TO HIM.", [mapNames.townSquareName, [8, 16],
																					 {"GOLD": 10, "XP": 10,
																					  "REWARD": [
																						  Items.SuperHealthPotion,
																						  1], "QUESTITEM": [QuestItems.letter, 1]}, False]],
								   ["DEFEAT THE SKELETON LORD", [4, 29],
									f"AH YOUR BACK! I TAKE IT HE TOLD YOU OF THE DANGERS WITHIN THE {mapNames.caveName}. "
									f"THE SKELETON LORD IS FEARSOME BUT HE IS WEAK TO LIGHT, WHICH HOLY WATER IS MADE OUT OF! "
									f"USE THIS KNOWLEDGE TO DEFEAT HIM AND TAKE SOME HOLY WATER TO HELP BEAT HIM!",
									[mapNames.townSquareName, [8, 16],
									 {"GOLD": 10, "XP": 10, "REWARD": [QuestItems.skeletonKey, 1], "QUESTITEM": [Items.HolyWater, 1]}, False]]]}
	farmQuest = {"416": [0, ["KILL GOBLINS", [4, 16],
			  f"I NEED YOUR HELP! THERE ARE GOBLINS IN MY BARN, PLEASE GET RID OF THEM FOR ME!",
			  [mapNames.farmName, [4, 16],
			   {"GOLD": 10, "XP": 10, "REWARD": [Equipment.Knife, 1]}, False]]]}
	townSquareQuest = {"529": [0, [f"FIGHT IN {mapNames.kingStarPubName}", [5, 29], f"HELLO BEAUTIFUL, THE NAMES SANDRA. YOU MAY OF HEAR OF ME FROM THE OTHERS AND WHAT I DO, "
									f"BUT DON'T WORRY I CAN CUT US A DEAL WE WOULD BOTH LIKE. THERE'S THIS GUY THAT HAS BEEN BOTHERING ME IN THE {mapNames.kingStarPubName}, "
									f"TAKE HIM OUT AND I'LL REWARD YOU", [mapNames.townSquareName, [5, 29], {"GOLD": 10, "XP": 10, "REWARD": [QuestItems.royalCoin, 1]}, False]],
							   ["STEAL CASTLE TREASURE", [5, 29], f"BACK FOR MORE?, THAT {QuestItems.royalCoin['name']} I GAVE YOU WILL GIVE YOU ACCESS TO THE CASTLE, IF THE GUARD IS GREEDY. ANYWAYS,"
									f"THERE IS A RUMOUR ABOUT TREASURE IN THE CASTLE BASEMENT. PROBLEM IS THAT IT REQUIRES A {QuestItems.skeletonKey['name']} TO OPEN IT. "
									f"DON'T WORRY, THE MONEY IS WORTH THE TROUBLES", [mapNames.townSquareName, [5, 29], {"GOLD": 100, "XP": 10, "REWARD": [QuestItems.royalCoin, 1]}, False]]]}
	allQuests = {mapNames.elders_homeName: elders_homeQuest, mapNames.farmName: farmQuest, mapNames.townSquareName: townSquareQuest}

class info:
	farmInfo = {"116": ["VILLAGER", [1, 16], f"BE CAREFUL, THE {mapNames.forestName} AHEAD IS FILLED WITH POISONOUS SPIDERS AND A QUEEN SPIDER BLOCKS THE "
									f"WAY TO THE {mapNames.townSquareName}", f"YOU CLEARED THE FOREST?! NOW WE CAN FREELY MOVE TO THE {mapNames.townSquareName} THANKS TO YOU!", 2]}
	townSquareInfo = {"22": ["MERCHANT", [2, 2], "MY WARES CONSIST OF A VARIETY OF FRUITS AND VEGETABLES", 2], "24": ["MERCHANT", [2, 4], "SORRY SIR FOR MY WARES ARE RUNNING DRY, COME SOME OTHER TIME", 2],
					  "26": ["MERCHANT", [2, 6], "THESE MONSTERS ARE BLEEDING MY STOCKS DRY!", 2], "28": ["MERCHANT", [2, 8], "IF ONLY THE KING DID SOMETHING AGAINST THESE MONSTERS", 2],
					  "223": ["MERCHANT", [2, 23], "IF MY STOCKS KEEP GETTING STOLEN, I MIGHT HAVE TO MOVE SOMEWHERE SAFER", 2], "225": ["MERCHANT", [2, 25], "IF THE CAVES NEARBY WHERE CLEARED, MAYBE I CAN BECOME A MINER INSTEAD", 2],
					  "227": ["MERCHANT", [2, 27], "I FEAR THE WORST FOR THIS TOWN IF THE MERCHANTS KEEP LEAVING", 2], "229": ["MERCHANT", [2, 29], "DEALING WITH SANDRA IS THE ONLY GOOD BUSINESS IN THIS TOWN LEFT", 2],
					  "523": ["MERCHANT", [5, 23], "I PAY TOO MUCH TAX FOR A KING THAT SITS IDLE WHILST HIS KINGDOM SUFFERS", 2], "525": ["MERCHANT", [5, 25], "IF YOU WANTED TO GET PAST THE CASTLE GUARDS, I HEARD SANDRA IS YOUR GUY", 2],
					  "527": ["MERCHANT", [5, 27], "I DO NOT LIKE BEING NEXT TO THIEVES, THAT SANDRA IS UP TO NO GOOD", 2],
					  "816": ["TOWN ELDER", [8, 16], "AHH FINALLY A MESSAGE... OH YOU DON'T HAVE ONE FOR ME? NEVERMIND THEN",
					  f"THAT LETTER YOU ARE HOLDING, GIVE IT TO ME... OH MY THIS IS BAD! THE SKELETON LORD HAS RISEN WITHIN THE {mapNames.caveName}, "
					  "IF WE DO NOT ACT NOW OUR TOWN WILL BE IN DANGER!",
					  "GO BACK TO YOUR HOME TOWN AND TALK TO THE ELDER, HE WILL KNOW WHAT TO DO",
					  "I HAVE NOTHING TO TELL YOU YOUNG ONE, YOU MUST ADVENTURE ON YOUR OWN", 2]}
	castleGateInfo = {"415": ["CASTLE GUARD", [4, 15], "SORRY, I CANNOT ALLOW YOU IN WITHOUT THE KINGS PERMISSION", "DON'T TELL ANYONE ABOUT THIS EXCHANGE", 2]}
	castleThroneInfo = {"18": ["KING OF LUCIA", [1, 8], "HOW DID YOU GET INSIDE? GET OUT OF HERE BEFORE I GET YOUR EXECUTED!", 2]}
	kingStarPubInfo = {"818": ["TAVERN KEEPER", [8, 18], "HEY KID, BE CAREFUL THERE'S A TROUBLEMAKER IN THE MAIN ROOM",
							   "DAMN KID, YOU CAN TAKE A BEATING, SOMEONE LIKE YOU WOULD ATTRACT A LOT OF ATTENTION SO BE CAREFUL", 2]}
	northLuciaInfo = {"115": ["TOWN GUARD", [1, 15], f"SORRY, I CANNOT LET YOU THROUGH WHILE THE {mobList.skeletonLord['name']} LIVES, ITS TOO DANGEROUS!", 2]}
	abandonedChurchInfo = {"111": ["PRIEST", [1, 11], "PLEASE HELP! THESE DEMONS ARE CORRUPTING THE CHURCH!", "THANK YOU, BRAVE ADVENTURER "
																											  "YOU HAVE SAVED THIS CHURCH FROM EVIL", 2]}
	allInfo = {mapNames.farmName: farmInfo, mapNames.townSquareName: townSquareInfo, mapNames.castleGateName: castleGateInfo,
			   mapNames.castleThroneName: castleThroneInfo, mapNames.kingStarPubName: kingStarPubInfo, mapNames.northLuciaName: northLuciaInfo, mapNames.abandonedChurch: abandonedChurchInfo}

class merchants:
	townMerchant = {"44": [[Equipment.Knife, Equipment.Dagger], [4, 4]],
					"84": [[Equipment.LeatherArmour, Equipment.LeatherShield, Equipment.Robe, Equipment.Bandana], [8, 4]],
					"124": [[Items.HealthPotion, Items.ManaPotion, Items.Antidote], [12, 4]]}
	townSquareMerchant = {"52": [[Equipment.IronSword, Equipment.Dagger, Equipment.WoodenStaff], [5, 2]], "54": [[Equipment.IronArmour, Equipment.IronHelmet, Equipment.IronBuckler], [5, 4]],
						  "56": [[Items.HealthPotion, Items.SuperHealthPotion, Items.ManaPotion, Items.SuperManaPotion], [5, 6]], "58": [[Items.Antidote, Items.HolyWater, Items.ThrowingKnife], [5, 8]]}
	allMerchants = [townMerchant, townSquareMerchant]

class chests:
	homeChest = {Items.HealthPotion['name']: [Items.HealthPotion, [3, 29]],
				 Items.ManaPotion['name']: [Items.ManaPotion, [4, 29]]}
	forestChest = {Items.HealthPotion['name']: [Items.HealthPotion, [9, 23]], Items.Antidote['name']: [Items.Antidote, [5, 11]]}
	castleBasementChest = {QuestItems.skeletonCrown['name']: [QuestItems.skeletonCrown, [1, 1]], "GOLD": [Items.Gold, [1, 3], 100]}
	allChest = {mapNames.homeName: homeChest, mapNames.forestName: forestChest, mapNames.castleBasementName: castleBasementChest}

class mobs:
	farmMobs = {mobList.goblin["ICON"]: [[2, 23], [2, 25], [3, 29], [4, 27], [5, 22]]}
	forestMobs = {mobList.spider["ICON"]: [[9, 7], [9, 14], [9, 24, True], [11, 3]], mobList.rat["ICON"]: [[6, 18], [12, 5]], mobList.queenSpider["ICON"]: [[1, 14, True]]}
	fieldMobs = {mobList.rat["ICON"]: [[3, 7], [3, 14], [3, 19, True]]}
	caveMobs = {mobList.skeleton["ICON"]: [[2, 12], [3, 29, True], [4, 12], [6, 1, True], [7, 12], [7, 25, True], [8, 17], [9, 8]], mobList.skeletonLord["ICON"]: [[2, 6, True]]}
	kingStarPubMobs = {mobList.bandit["ICON"]: [[1, 17, True]]}
	castleMobs = {mobList.soldier["ICON"]: [[1, 15, True], [4, 29, True], [5, 29, True]]}
	luciaGatesMobs = {mobList.bandit["ICON"]: [[1, 14, True], [4, 5], [4, 18, True], [8, 14]]}
	abandonedChurchMobs = {mobList.evilMage["ICON"]: [[5, 11], [9, 5], [10, 8]]}
	allMobs = {mapNames.farmName: farmMobs, mapNames.forestName: forestMobs, mapNames.fieldName: fieldMobs, mapNames.caveName: caveMobs,
			   mapNames.kingStarPubName: kingStarPubMobs, mapNames.castleName: castleMobs, mapNames.luciaGates: luciaGatesMobs, mapNames.abandonedChurch: abandonedChurchMobs}
