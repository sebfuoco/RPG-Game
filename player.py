from Items import Equipment, Items, QuestItems
from ItemsAction import EquipmentStats
from math import floor
class Magic:
	# Offensive Spells / only used in battle
	Fire = {"name": "FIRE", "type": "OFFENSIVE", "POWER": 5, "ELEMENT": "FIRE", "MANA": 5, "LEVEL": 1}
	Ice = {"name": "ICE", "type": "OFFENSIVE", "POWER": 5, "ELEMENT": "ICE", "MANA": 5, "LEVEL": 1}
	Thunder = {"name": "THUNDER", "type": "OFFENSIVE", "POWER": 5, "ELEMENT": "THUNDER", "MANA": 5, "LEVEL": 1}
	Water = {"name": "WATER", "type": "OFFENSIVE", "POWER": 5, "ELEMENT": "WATER", "MANA": 5, "LEVEL": 22}
	Earth = {"name": "EARTH", "type": "OFFENSIVE", "POWER": 5, "ELEMENT": "EARTH", "MANA": 5, "LEVEL": "QUEST"}
	# Support Spells / can be used outside of battle
	Heal = {"name": "HEAL", "type": "SUPPORT", "heal": "HP", "POWER": 5, "MANA": 10, "LEVEL": 3}
	CurePoison = {"name": "CURE POISON", "type": "SUPPORT", "heal": "POISON", "MANA": 10, "LEVEL": 5}
	Teleport = {"name": "TELEPORT", "type": "SUPPORT", "heal": "TELEPORT", "MANA": 20, "LEVEL": 30}
	SecondLife = {"name": "SECOND LIFE", "type": "SUPPORT", "heal": "REVIVE", "MANA": 50, "LEVEL": "QUEST"}
	# Stat spells, increases stats and can be used outside of battle
	Protect = {"name": "PROTECT", "type": "STAT", "heal": "DEF", "stat": 1.5, "MANA": 10, "cast": 0, "LEVEL": 8}
	Strength = {"name": "STRENGTH", "type": "STAT", "heal": "STR", "stat": 1.5, "MANA": 10, "cast": 0, "LEVEL": 9}
	Enhance = {"name": "ENHANCE", "type": "STAT", "heal": "MagicSTR", "stat": 1.5, "MANA": 10, "cast": 0, "LEVEL": 10}
	Haste = {"name": "HASTE", "type": "STAT", "heal": "SPEED", "stat": 1.5, "MANA": 10, "cast": 0, "LEVEL": 15}
	Evade = {"name": "EVADE", "type": "STAT", "heal": "EVASION", "stat": 10, "MANA": 10, "cast": 0, "LEVEL": 20}

	# Spells that can be cast by player
	learntSpells = [Fire, Ice, Thunder, Water, Heal, CurePoison, Teleport, Protect, Strength, Enhance, Haste, Evade]
	spellBook = []
	selectedMagic = ""

class Classes:
	# DEFAULT CLASSES, HP, MP, STR, MagicSTR, DEF, SPEED, EVASION
	# Warrior Stats + Factors
	class Warrior:
		stats = {"CLASS": "WARRIOR", "HP": 20, "MP": 0, "STR": 500, "MagicSTR": 0, "DEF": 1, "SPEED": 1, "EVASION": 0}
		nextLevel = {"HPIncrease": 5, "MPIncrease": 0, "STRIncrease": 1, "MagicSTRIncrease": 0, "SPEEDIncrease": 0.5}
		equipped = {"HEAD": Equipment.Empty, "CHEST": Equipment.Clothes, "LEFT-HAND": Equipment.Empty,
					"RIGHT-HAND": Equipment.WoodenSword}
	# Mage Stats + Factors
	class Mage:
		stats = {"CLASS": "MAGE", "HP": 15, "MP": 202, "STR": 1, "MagicSTR": 1, "DEF": 0, "SPEED": 3, "EVASION": 0}
		nextLevel = {"HPIncrease": 2, "MPIncrease": 5, "STRIncrease": 1, "MagicSTRIncrease": 0.5, "SPEEDIncrease": 0.5}
		equipped = {"HEAD": Equipment.Empty, "CHEST": Equipment.Clothes, "LEFT-HAND": Equipment.Empty,
					"RIGHT-HAND": Equipment.WoodenWand}
		startingMagic = {Magic.Fire["name"]: Magic.Fire, Magic.Ice["name"]: Magic.Ice, Magic.Thunder["name"]: Magic.Thunder}
	# Thief Stats + Factors
	class Thief:
		stats = {"CLASS": "THIEF", "HP": 18, "MP": 0, "STR": 2, "MagicSTR": 0, "DEF": 0, "SPEED": 5, "EVASION": 20}
		nextLevel = {"HPIncrease": 3, "MPIncrease": 0, "STRIncrease": 1, "MagicSTRIncrease": 0, "SPEEDIncrease": 0.5}
		equipped = {"HEAD": Equipment.Empty, "CHEST": Equipment.Clothes, "LEFT-HAND": Equipment.Empty,
					"RIGHT-HAND": Equipment.WoodenSword}
	# EVOLVED CLASSES, add stats to current player, nextLevel replaces current nextLevel
	# Knight Stats + Factors
	class Knight:
		stats = {"CLASS": "KNIGHT", "HP": 20, "STR": 2, "DEF": 2}
		nextLevel = {"HPIncrease": 10, "MPIncrease": 0, "STRIncrease": 2, "MagicSTRIncrease": 0, "SPEEDIncrease": 0}
	# Ninja Stats + Factors
	class Ninja:
		stats = {"CLASS": "NINJA", "HP": 10, "STR": 1, "SPEED": 2, "EVASION": 15}
		nextLevel = {"HPIncrease": 1, "MPIncrease": 0, "STRIncrease": 1, "MagicSTRIncrease": 0, "SPEEDIncrease": 1.5}
	# Wizard Stats + Factors
	class Wizard:
		stats = {"CLASS": "WIZARD", "HP": 5, "MP": 20, "MagicSTR": 1}
		nextLevel = {"HPIncrease": 1, "MPIncrease": 10, "STRIncrease": 0, "MagicSTRIncrease": 1, "SPEEDIncrease": 0.5}

class Player(object):
	initStats = ["CLASS", "HP", "MP", "STR", "MagicSTR", "DEF", "SPEED", "EVASION"]
	def __init__(self, startingClass, startingStats, nextLevel, equipped):
		# Max Stats used for calculations and display
		self.currentStats = {"CLASS": startingClass, "LEVEL": 1, "MaxHP": startingStats["HP"],
							 "MaxMP": startingStats["MP"], "MaxSTR": startingStats["STR"], "MaxMagicSTR": startingStats["MagicSTR"],
							 "MaxDEF": startingStats["DEF"], "MaxSPEED": startingStats["SPEED"], "MaxEVASION": startingStats["EVASION"], "MaxXP": 20}
		# Base Stats
		self.stats = {"CLASS": startingStats["CLASS"], "HP": startingStats["HP"], "MP": startingStats["MP"], "STR": startingStats["STR"], "MagicSTR": startingStats["MagicSTR"],
					  "DEF": startingStats["DEF"], "SPEED": startingStats["SPEED"], "EVASION": startingStats["EVASION"], "XP": 0}
		self.nextLevel = {"HPIncrease": nextLevel["HPIncrease"], "MPIncrease": nextLevel["MPIncrease"],
						  "STRIncrease": nextLevel["STRIncrease"], "MagicSTRIncrease": nextLevel["MagicSTRIncrease"], "SPEEDIncrease": nextLevel["SPEEDIncrease"]}
		self.equipped = {"HEAD": equipped["HEAD"], "CHEST": equipped["CHEST"], "LEFT-HAND": equipped["LEFT-HAND"],
						 "RIGHT-HAND": equipped["RIGHT-HAND"]}
		self.Inventory = [[Items.HealthPotion, 1], [Items.Antidote, 1]]
		self.Gold = 20
		self.status = "NORMAL"
		self.keyItems = {QuestItems.royalCoin["name"]: QuestItems.royalCoin}
		self.activeQuests = []
		self.manaMultiplier = floor(self.currentStats["LEVEL"] * 2.25)
		if self.manaMultiplier < 1:
			self.manaMultiplier = 1

	def initMagicBook(self):
		for spell in Magic.learntSpells:
			if self.currentStats["LEVEL"] >= spell["LEVEL"]:
				Magic.spellBook.append(spell)
		Magic.selectedMagic = Magic.spellBook[0]

	def initMagicLevel(self):
		for spell in Magic.spellBook:
			if spell["type"] == "OFFENSIVE" or spell["heal"] == "HP":
				spell["POWER"] = floor(spell["POWER"] * self.manaMultiplier)
				spell["MANA"] = floor(spell["MANA"] * self.manaMultiplier)

	def levelUp(self, screen, pos, charInventory):
		while self.stats["XP"] >= self.currentStats["MaxXP"]:
			self.manaMultiplier = floor(self.currentStats["LEVEL"] * 0.25)
			self.initMagicLevel()
			self.stats["XP"] -= self.currentStats["MaxXP"]
			self.currentStats["MaxXP"] = round(self.currentStats["MaxXP"] * 1.5)
			self.currentStats["LEVEL"] += 1
			self.currentStats["MaxHP"] += self.nextLevel["HPIncrease"]
			self.currentStats["MaxMP"] += self.nextLevel["MPIncrease"]
			self.stats["HP"] += self.nextLevel["HPIncrease"]
			self.stats["MP"] += self.nextLevel["MPIncrease"]
			self.stats["STR"] += self.nextLevel["STRIncrease"]
			self.stats["MagicSTR"] += self.nextLevel["MagicSTRIncrease"]
			self.stats["SPEED"] += self.nextLevel["SPEEDIncrease"]
			screen.addstr(pos, 35, f"YOU ARE NOW LEVEL {self.currentStats['LEVEL']}")
			EquipmentStats(screen, self, charInventory)

	def evolve(self, screen, pos, charInventory):
		self.currentStats["MaxHP"] += self.nextLevel["HPIncrease"]
		self.stats["HP"] += self.nextLevel["HPIncrease"]
		self.stats["MP"] += self.nextLevel["MPIncrease"]
		self.currentStats["MaxMP"] += self.nextLevel["MPIncrease"]
		self.currentStats["MaxSTR"] += self.nextLevel["STRIncrease"]
		self.currentStats["MaxMagicSTR"] += self.nextLevel["MagicSTRIncrease"]
		self.currentStats["MaxSPEED"] += self.nextLevel["SPEEDIncrease"]
		screen.addstr(pos, 35, f"YOU ARE NOW A {self.currentStats['CLASS']}")
		EquipmentStats(screen, self, charInventory)
	# store enemies for quest + save game
	visitedMap = {}
