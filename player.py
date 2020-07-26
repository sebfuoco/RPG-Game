from Items import Equipment, Items

class Classes:
	# Warrior Stats + Factors
	class Warrior:
		stats = {"CLASS": "WARRIOR", "HP": 20, "MP": 0, "STR": 3, "DEF": 1}
		nextLevel = {"HPIncrease": 5, "MPIncrease": 0, "STRIncrease": 1}
		equipped = {"HEAD": Equipment.Empty, "CHEST": Equipment.Clothes, "LEFT-HAND": Equipment.Empty,
					"RIGHT-HAND": Equipment.WoodenSword}
	# Mage Stats + Factors
	class Mage:
		stats = {"CLASS": "MAGE", "HP": 15, "MP": 20, "STR": 1, "DEF": 0}
		nextLevel = {"HPIncrease": 2, "MPIncrease": 5, "STRIncrease": 1}
		equipped = {"HEAD": Equipment.Empty, "CHEST": Equipment.Clothes, "LEFT-HAND": Equipment.Empty,
					"RIGHT-HAND": Equipment.WoodenWand}
	# Thief Stats + Factors
	class Thief:
		stats = {"CLASS": "THIEF", "HP": 18, "MP": 0, "STR": 2, "DEF": 0}
		nextLevel = {"HPIncrease": 3, "MPIncrease": 0, "STRIncrease": 1}
		equipped = {"HEAD": Equipment.Empty, "CHEST": Equipment.Clothes, "LEFT-HAND": Equipment.Empty,
					"RIGHT-HAND": Equipment.WoodenSword}

class Player(object):
	def __init__(self, startingClass, startingStats, nextLevel, equipped):
		self.currentStats = {"CLASS": startingClass, "LEVEL": 1, "MaxHP": startingStats["HP"],
							 "MaxMP": startingStats["MP"], "MaxSTR": startingStats["STR"],
							 "MaxDEF": startingStats["DEF"], "MaxXP": 20}
		self.stats = {"CLASS": startingStats["CLASS"], "HP": 10, "MP": startingStats["MP"], "STR": startingStats["STR"],
					  "DEF": startingStats["DEF"], "XP": 0}
		self.nextLevel = {"HPIncrease": nextLevel["HPIncrease"], "MPIncrease": nextLevel["MPIncrease"],
						  "STRIncrease": nextLevel["STRIncrease"]}
		self.equipped = {"HEAD": equipped["HEAD"], "CHEST": equipped["CHEST"], "LEFT-HAND": equipped["LEFT-HAND"],
						 "RIGHT-HAND": equipped["RIGHT-HAND"]}
		self.Inventory = [[Items.HealthPotion, 1], [Items.Antidote, 1]]
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
			screen.addstr(15, 35, f"YOU ARE NOW LEVEL {self.currentStats['LEVEL']}")
