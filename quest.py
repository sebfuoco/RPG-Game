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
	townSquareInfo = ["TOWN ELDER", "AHH FINALLY A MESSAGE... OH YOU DON'T HAVE ONE FOR ME? NEVERMIND THEN",
					  "THAT LETTER YOU ARE HOLDING, GIVE IT TO ME... OH MY THIS IS BAD! THE SKELETON LORD HAS RISEN WITHIN THE CAVES, "
					  "IF WE DO NOT ACT NOW OUR TOWN WILL BE IN DANGER!",
					  "GO BACK TO YOUR HOME TOWN AND TALK TO THE ELDER, HE WILL KNOW WHAT TO DO",
					  "I HAVE NOTHING TO TELL YOU YOUNG ONE, YOU MUST ADVENTURE ON YOUR OWN", 1]
	castleGateInfo = ["CASTLE GUARD", "SORRY, I CAN'T ALLOW YOU IN WITHOUT THE KINGS PERMISSION", 1]
	allInfo = [townSquareInfo, castleGateInfo]
