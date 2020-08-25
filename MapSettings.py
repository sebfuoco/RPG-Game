from Map import mapNames
from Items import Items, Equipment, QuestItems

class quest:
	elders_homeQuest = {"429": [["DELIVER MESSAGE TO TOWN ELDER",
									f"HELLO YOUNG ONE, I AM TOO WEAK TO DELIVER THIS MESSAGE TO THE TOWN ELDER, CURRENTLY IN THE {mapNames.townSquareName}. "
									f"I WOULD BE DELIGHTED IF YOU SENT IT TO HIM.", [mapNames.townSquareName, [8, 16],
																					 {"GOLD": 10, "XP": 10,
																					  "REWARD": [
																						  Items.SuperHealthPotion,
																						  1], "QUESTITEM": [QuestItems.letter, 1]}, False]],
								   ["DEFEAT THE SKELETON LORD",
									f"AH YOUR BACK! I TAKE IT HE TOLD YOU OF THE DANGERS WITHIN THE {mapNames.caveName}. "
									f"THE SKELETON LORD IS FEARSOME BUT HE IS WEAK TO LIGHT, USE THIS KNOWLEDGE TO DEFEAT HIM!",
									[mapNames.townSquareName, [8, 16],
									 {"GOLD": 10, "XP": 10, "REWARD": [QuestItems.skeletonKey, 1], "QUESTITEM": [Items.HolyWater, 1]}, False]]]}
	farmQuest = {"416": [["KILL GOBLINS",
			  f"I NEED YOUR HELP! THERE ARE GOBLINS IN MY BARN, PLEASE GET RID OF THEM FOR ME!",
			  [mapNames.farmName, [4, 16],
			   {"GOLD": 10, "XP": 10, "REWARD": [Equipment.Knife, 1]}, False]]]}
	townSquareQuest = {"529": [[f"FIGHT IN {mapNames.kingStarPubName}", f"HELLO BEAUTIFUL, THE NAMES SANDRA. YOU MAY OF HEAR OF ME FROM THE OTHERS AND WHAT I DO, "
									f"BUT DON'T WORRY I CAN CUT US A DEAL WE WOULD BOTH LIKE. THERE'S THIS GUY THAT HAS BEEN BOTHERING ME IN THE {mapNames.kingStarPubName}, "
									f"TAKE HIM OUT AND I'LL REWARD YOU", [mapNames.townSquareName, [5, 29], {"GOLD": 10, "XP": 10, "REWARD": [QuestItems.royalCoin, 1]}, False]]]}
	allQuests = {mapNames.elders_homeName: elders_homeQuest, mapNames.farmName: farmQuest, mapNames.townSquareName: townSquareQuest}

class info:
	farmInfo = {"116": ["VILLAGER", f"BE CAREFUL, THE {mapNames.forestName} AHEAD IS FILLED WITH POISONOUS SPIDERS AND A QUEEN SPIDER BLOCKS THE "
									f"WAY TO THE {mapNames.townSquareName}", f"YOU CLEARED THE FOREST?! NOW WE CAN FREELY MOVE TO THE {mapNames.townSquareName} THANKS TO YOU!", 1]}
	townSquareInfo = {"22": ["MERCHANT", "MY WARES CONSIST OF A VARIETY OF FRUITS AND VEGETABLES", 1], "24": ["MERCHANT", "SORRY SIR FOR MY WARES ARE RUNNING DRY, COME SOME OTHER TIME", 1],
					  "26": ["MERCHANT", "THESE MONSTERS ARE BLEEDING MY STOCKS DRY!", 1], "28": ["MERCHANT", "IF ONLY THE KING DID SOMETHING AGAINST THESE MONSTERS", 1],
					  "223": ["MERCHANT", "IF MY STOCKS KEEP GETTING STOLEN, I MIGHT HAVE TO MOVE SOMEWHERE SAFER", 1], "225": ["MERCHANT", "IF THE CAVES NEARBY WHERE CLEARED, MAYBE I CAN BECOME A MINER INSTEAD", 1],
					  "227": ["MERCHANT", "I FEAR THE WORST FOR THIS TOWN IF THE MERCHANTS KEEP LEAVING", 1], "229": ["MERCHANT", "DEALING WITH SANDRA IS THE ONLY GOOD BUSINESS IN THIS TOWN LEFT", 1],
					  "523": ["MERCHANT", "I DO NOT LIKE BEING NEXT TO THIEVES, THAT SANDRA IS UP TO NO GOOD", 1], "525": ["MERCHANT", "IF YOU WANTED TO GET PAST THE CASTLE GUARDS, I HEARD SANDRA IS YOUR GUY", 1],
					  "527": ["MERCHANT", "I PAY TOO MUCH TAX FOR A KING THAT SITS IDLE WHILST HIS KINGDOM SUFFERS", 1],
					  "816": ["TOWN ELDER", "AHH FINALLY A MESSAGE... OH YOU DON'T HAVE ONE FOR ME? NEVERMIND THEN",
					  f"THAT LETTER YOU ARE HOLDING, GIVE IT TO ME... OH MY THIS IS BAD! THE SKELETON LORD HAS RISEN WITHIN THE {mapNames.caveName}, "
					  "IF WE DO NOT ACT NOW OUR TOWN WILL BE IN DANGER!",
					  "GO BACK TO YOUR HOME TOWN AND TALK TO THE ELDER, HE WILL KNOW WHAT TO DO",
					  "I HAVE NOTHING TO TELL YOU YOUNG ONE, YOU MUST ADVENTURE ON YOUR OWN", 1]}
	castleGateInfo = {"415": ["CASTLE GUARD", "SORRY, I CANNOT ALLOW YOU IN WITHOUT THE KINGS PERMISSION", 1]}
	kingStarPubInfo = {"818": ["TAVERN KEEPER", "HEY KID, BE CAREFUL THERE'S A TROUBLEMAKER IN THE MAIN ROOM",
							   "DAMN KID, YOU CAN TAKE A BEATING, SOMEONE LIKE YOU WOULD ATTRACT A LOT OF ATTENTION SO BE CAREFUL", 1]}
	allInfo = {mapNames.farmName: farmInfo, mapNames.townSquareName: townSquareInfo, mapNames.castleGateName: castleGateInfo, mapNames.kingStarPubName: kingStarPubInfo}

class merchants:
	townMerchant = {"44": (Equipment.Knife, Equipment.Dagger),
					"84": (Equipment.LeatherArmour, Equipment.LeatherShield, Equipment.Robe, Equipment.Bandana),
					"124": (Items.HealthPotion, Items.ManaPotion, Items.Antidote)}
	townSquareMerchant = {"52": (Equipment.IronSword, Equipment.Dagger, Equipment.WoodenStaff), "54": (Equipment.IronArmour, Equipment.IronHelmet, Equipment.IronBuckler),
						  "56": (Items.HealthPotion, Items.SuperHealthPotion, Items.ManaPotion, Items.SuperManaPotion), "58": (Items.Antidote, Items.HolyWater, Items.ThrowingKnife)}
	allMerchants = [townMerchant, townSquareMerchant]

class chests:
	homeChest = {Items.HealthPotion['name']: [Items.HealthPotion, [3, 29]],
				 Items.ManaPotion['name']: [Items.ManaPotion, [4, 29]]}
	forestChest = {Items.HealthPotion['name']: [Items.HealthPotion, [9, 23]], Items.Antidote['name']: [Items.Antidote, [5, 11]]}
	allChest = {mapNames.homeName: homeChest, mapNames.forestName: forestChest}

class mobs:
	farmMobs = {"g": [[2, 23], [2, 25], [3, 29], [4, 27], [5, 22]]}
	forestMobs = {"s": [[9, 7], [9, 14], [9, 24], [11, 3]], "r": [[6, 18], [12, 5]], "q": [[1, 14]]}
	fieldMobs = {"r": [[3, 7], [3, 14], [3, 19]]}
	caveMobs = {"ŝ": [[2, 12], [3, 29], [4, 12], [6, 1], [7, 12], [7, 25], [8, 17], [9, 8]], "§": [[2, 6]]}
	kingStarPubMobs = {"b": [[1, 17]]}
	allMobs = {mapNames.farmName: farmMobs, mapNames.forestName: forestMobs, mapNames.fieldName: fieldMobs, mapNames.caveName: caveMobs, mapNames.kingStarPubName: kingStarPubMobs}
