from Map import mapNames
from Map import Items, Equipment

class quest:
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
	farmQuest = {"416": [["KILL GOBLINS",
			  f"I NEED YOUR HELP! THERE ARE GOBLINS IN MY BARN, PLEASE GET RID OF THEM FOR ME!",
			  [mapNames.farmName, [4, 16],
			   {"GOLD": 10, "XP": 10, "REWARD": [Equipment.Knife, 1]}]]]}
	allQuests = [neighbour_homeQuest, farmQuest]

class info:
	farmInfo = {"116": ["VILLAGER", f"BE CAREFUL, THE {mapNames.forestName} AHEAD IS FILLED WITH POISONOUS SPIDERS AND A QUEEN SPIDER BLOCKS THE "
									f"WAY TO THE {mapNames.townSquareName}", f"YOU CLEARED THE FOREST?! NOW WE CAN FREELY MOVE TO THE {mapNames.townSquareName} THANKS TO YOU!", 1]}
	townSquareInfo = {"816": ["TOWN ELDER", "AHH FINALLY A MESSAGE... OH YOU DON'T HAVE ONE FOR ME? NEVERMIND THEN",
					  f"THAT LETTER YOU ARE HOLDING, GIVE IT TO ME... OH MY THIS IS BAD! THE SKELETON LORD HAS RISEN WITHIN THE {mapNames.caveName}, "
					  "IF WE DO NOT ACT NOW OUR TOWN WILL BE IN DANGER!",
					  "GO BACK TO YOUR HOME TOWN AND TALK TO THE ELDER, HE WILL KNOW WHAT TO DO",
					  "I HAVE NOTHING TO TELL YOU YOUNG ONE, YOU MUST ADVENTURE ON YOUR OWN", 1]}
	castleGateInfo = {"415": ["CASTLE GUARD", "SORRY, I CANNOT ALLOW YOU IN WITHOUT THE KINGS PERMISSION", 1]}
	allInfo = [farmInfo, townSquareInfo, castleGateInfo]

class merchants:
	townMerchant = {"44": (Equipment.Knife, Equipment.Dagger),
					"84": (Equipment.LeatherArmour, Equipment.Robe, Equipment.Bandana),
					"124": (Items.HealthPotion, Items.ManaPotion, Items.Antidote)}

	allMerchants = [townMerchant]
