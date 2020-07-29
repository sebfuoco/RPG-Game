from Items import Equipment, Items

class Magic:
	Fire = {"name": "FIRE", "POWER": 5, "MANA": 5}
	Ice = {"name": "ICE", "POWER": 5, "MANA": 5}
	Thunder = {"name": "THUNDER", "POWER": 5, "MANA": 5}
	selectedMagic = Fire

class Classes:
	# Warrior Stats + Factors
	class Warrior:
		stats = {"CLASS": "WARRIOR", "HP": 20, "MP": 0, "STR": 3, "MagicSTR": 0, "DEF": 1, "SPEED": 1, "EVASION": 0}
		nextLevel = {"HPIncrease": 5, "MPIncrease": 0, "STRIncrease": 1, "MagicSTRIncrease": 0, "SPEEDIncrease": 0.5}
		equipped = {"HEAD": Equipment.Empty, "CHEST": Equipment.Clothes, "LEFT-HAND": Equipment.Empty,
					"RIGHT-HAND": Equipment.WoodenSword}
	# Mage Stats + Factors
	class Mage:
		stats = {"CLASS": "MAGE", "HP": 15, "MP": 20, "STR": 1, "MagicSTR": 1, "DEF": 0, "SPEED": 3, "EVASION": 0}
		nextLevel = {"HPIncrease": 2, "MPIncrease": 5, "STRIncrease": 1, "MagicSTRIncrease": 0.5, "SPEEDIncrease": 0.5}
		equipped = {"HEAD": Equipment.Empty, "CHEST": Equipment.Clothes, "LEFT-HAND": Equipment.Empty,
					"RIGHT-HAND": Equipment.WoodenWand}
		startingMagic = {Magic.Fire["name"]: Magic.Fire, Magic.Ice["name"]: Magic.Ice, Magic.Thunder["name"]: Magic.Thunder}
	# Thief Stats + Factors
	class Thief:
		stats = {"CLASS": "THIEF", "HP": 18, "MP": 0, "STR": 2, "MagicSTR": 0, "DEF": 0, "SPEED": 5, "EVASION": 20}
		nextLevel = {"HPIncrease": 3, "MPIncrease": 0, "STRIncrease": 1, "MagicSTRIncrease": 0.5, "SPEEDIncrease": 0.5}
		equipped = {"HEAD": Equipment.Empty, "CHEST": Equipment.Clothes, "LEFT-HAND": Equipment.Empty,
					"RIGHT-HAND": Equipment.WoodenSword}

class Player(object):
	def __init__(self, startingClass, startingStats, nextLevel, equipped):
		self.currentStats = {"CLASS": startingClass, "LEVEL": 1, "MaxHP": startingStats["HP"],
							 "MaxMP": startingStats["MP"], "MaxSTR": startingStats["STR"], "MaxMagicSTR": startingStats["MagicSTR"],
							 "MaxDEF": startingStats["DEF"], "MaxSPEED": startingStats["SPEED"], "MaxEVASION": startingStats["EVASION"], "MaxXP": 20}
		self.stats = {"CLASS": startingStats["CLASS"], "HP": startingStats["HP"], "MP": startingStats["MP"], "STR": startingStats["STR"], "MagicSTR": startingStats["MagicSTR"],
					  "DEF": startingStats["DEF"], "SPEED": startingStats["SPEED"], "EVASION": startingStats["EVASION"], "XP": 0}
		self.nextLevel = {"HPIncrease": nextLevel["HPIncrease"], "MPIncrease": nextLevel["MPIncrease"],
						  "STRIncrease": nextLevel["STRIncrease"], "MagicSTRIncrease": nextLevel["MagicSTRIncrease"], "SPEEDIncrease": nextLevel["SPEEDIncrease"]}
		self.equipped = {"HEAD": equipped["HEAD"], "CHEST": equipped["CHEST"], "LEFT-HAND": equipped["LEFT-HAND"],
						 "RIGHT-HAND": equipped["RIGHT-HAND"]}
		self.Inventory = [[Items.HealthPotion, 1], [Items.Antidote, 1], [Equipment.Knife, 1], [Equipment.LeatherArmour, 1]]
		self.Gold = 20
		self.status = "NORMAL"

	def levelUp(self, screen):
		if self.stats["XP"] >= self.currentStats["MaxXP"]:
			self.currentStats["MaxXP"] = round(self.currentStats["MaxXP"] * 1.5)
			self.currentStats["LEVEL"] += 1
			self.currentStats["MaxHP"] += self.nextLevel["HPIncrease"]
			self.stats["HP"] += self.nextLevel["HPIncrease"]
			self.stats["MP"] += self.nextLevel["MPIncrease"]
			self.currentStats["MaxMP"] += self.nextLevel["MPIncrease"]
			self.currentStats["MaxSTR"] += self.nextLevel["STRIncrease"]
			self.currentStats["MaxMagicSTR"] += self.nextLevel["MagicSTRIncrease"]
			self.currentStats["MaxSPEED"] += self.nextLevel["SPEEDIncrease"]
			screen.addstr(15, 35, f"YOU ARE NOW LEVEL {self.currentStats['LEVEL']}")
