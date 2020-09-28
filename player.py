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
		stats = {"CLASS": "MAGE", "HP": 15, "MP": 202, "STR": 1111, "MagicSTR": 1, "DEF": 0, "SPEED": 3, "EVASION": 0}
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

class Abilities:
	# Warrior Ability, cooldown based on kills
	Slash = {"name": "SLASH", "CLASS": Classes.Warrior.stats['CLASS'], "COOLDOWN": 5, "POWER": 5, "LEVEL": 3, "countdown": 0,
			 "description": "SLASHES ALL NEARBY ENEMIES WITHIN 1 TILE PROXIMITY"}
	Charge = {"name": "CHARGE", "CLASS": Classes.Warrior.stats['CLASS'], "COOLDOWN": 5, "POWER": 5, "LEVEL": 10, "countdown": 0,
			  "description": "CHARGE AT AN ENEMY TO APPEAR BESIDE THEM"}
	Rage = {"name": "RAGE", "CLASS": Classes.Warrior.stats['CLASS'], "COOLDOWN": 5, "POWER": 5, "LEVEL": 15, "countdown": 0,
			"description": "CASTER GOES INTO A RAGE, DOUBLING THEIR STR AND HALVES DEF AND EVASION"}
	# Thief Ability, cooldown based on kills
	Steal = {"name": "STEAL", "CLASS": Classes.Thief.stats['CLASS'], "COOLDOWN": 0, "POWER": 20, "LEVEL": 1, "countdown": 0,
			 "description": "STEALS AN ITEM FROM AN ENEMY, POWER DETERMINES HIT-RATE"}
	SneakAttack = {"name": "SNEAK ATTACK", "CLASS": Classes.Thief.stats['CLASS'], "COOLDOWN": 5, "POWER": 5, "LEVEL": 10, "countdown": 0,
				   "description": "ATTACKS AN ENEMY, WITH A HIGH CRIT RATE"}
	AerialStrike = {"name": "AERIAL STRIKE", "CLASS": Classes.Thief.stats['CLASS'], "COOLDOWN": 10, "POWER": 5, "LEVEL": 15, "countdown": 0,
					"description": "CASTER JUMPS AND STRIKES AN ENEMY FROM THE SKY, DEALING HEAVY DAMAGE TO FLYING ENEMIES"}
	# Mage Ability, based on magic kills, still uses mana
	Absorb = {"name": "ABSORB", "CLASS": Classes.Mage.stats['CLASS'], "COOLDOWN": 5, "POWER": 5, "LEVEL": 2, "countdown": 0,
			  "description": "ABSORBS MANA FROM ENEMIES, MORE EFFECTIVE AGAINST MAGICAL ENEMIES, POWER DETERMINES MANA ABSORBED"}
	ManaShield = {"name": "MANA SHIELD", "CLASS": Classes.Mage.stats['CLASS'], "COOLDOWN": 10, "LEVEL": 15, "countdown": 0,
				  "description": "CASTER SURROUNDINGS THEMSELVES WITH MANA, TAKING DAMAGE TO THEIR MANA INSTEAD OF HEALTH"}
	Teleport = {"name": "TELEPORT", "CLASS": Classes.Mage.stats['CLASS'], "COOLDOWN": 0, "LEVEL": 20, "countdown": 0,
				"description": "TELEPORTS CASTER TO ANOTHER AREA OF CHOICE"}
	# 	# Knight Ability
	HolyStrike = {"name": "HOLY STRIKE", "CLASS": Classes.Knight.stats['CLASS'], "COOLDOWN": 10, "POWER": 5, "ELEMENT": "HOLY",
				  "LEVEL": 20, "countdown": 0, "description": "STRIKE THAT DEALS HOLY DAMAGE TO A ENEMY"}
	Guard = {"name": "GUARD", "CLASS": Classes.Knight.stats['CLASS'], "COOLDOWN": 5, "POWER": 10, "LEVEL": 30, "countdown": 0,
			 "description": "CASTER PREPARES FOR IMPACT, INCREASING DEF"}
	Recover = {"name": "RECOVER", "CLASS": Classes.Knight.stats['CLASS'], "COOLDOWN": 10, "POWER": 10, "LEVEL": 40, "countdown": 0,
			   "description": "CASTER RECOVERS HP"}
	# Ninja Ability
	Stealth = {"name": "STEALTH", "CLASS": Classes.Ninja.stats['CLASS'], "COOLDOWN": 10, "POWER": 25, "LEVEL": 20, "countdown": 0,
			   "description": "HIDES THE CASTER FROM ENEMIES, INCREASING EVASION"}
	Dash = {"name": "DASH", "CLASS": Classes.Ninja.stats['CLASS'], "COOLDOWN": 5, "LEVEL": 30, "countdown": 0, "description":
			"CASTER RUNS IN A DIRECTION, AVOIDING ALL ATTACKS AND DAMAGE"}
	SmokeScreen = {"name": "SMOKESCREEN", "CLASS": Classes.Ninja.stats['CLASS'], "COOLDOWN": 10, "LEVEL": 40, "countdown": 0,
				   "description": "CASTER THROWS SMOKE, CONFUSING THE ENEMY AND MAY CAUSE IT TO ATTACK ITSELF"}
	# Wizard Ability
	FireBlast = {"name": "FIRE BLAST", "CLASS": Classes.Wizard.stats['CLASS'], "COOLDOWN": 10, "POWER": 5, "LEVEL": 20, "countdown": 0,
				 "ELEMENT": "FIRE", "description": "SHOTS A BLAST OF FIRE AROUND THE CASTER, DEALING FIRE DAMAGE"}
	IceStorm = {"name": "ICE STORM", "CLASS": Classes.Wizard.stats['CLASS'], "COOLDOWN": 10, "POWER": 5, "LEVEL": 30, "countdown": 0,
				"ELEMENT": "ICE", "description": "SUMMONS AN ICE STORM THAT AT AN ENEMY, DEALING ICE DAMAGE TO THAT ENEMY AND NEARBY "
												 "ENEMIES WITHIN A 1 TILE PROXIMITY"}
	ThunderStorm = {"name": "THUNDER STORM", "CLASS": Classes.Wizard.stats['CLASS'], "COOLDOWN": 10, "POWER": 5, "LEVEL": 40, "countdown": 0,
					"ELEMENT": "THUNDER", "description": "SUMMONS A THUNDER STORM THAT RANDOMLY HITS ENEMIES, DEALING THUNDER DAMAGE TO THEM"}

	learntAbilities = [Slash, Charge, Steal, SneakAttack, Absorb]
	abilityBook = []

class Player(object):
	initStats = ["CLASS", "HP", "MP", "STR", "MagicSTR", "DEF", "SPEED", "EVASION"]
	def __init__(self, startingClass, startingStats, nextLevel, equipped):
		self.coords = []
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
		self.keyItems = {}
		self.activeQuests = []
		self.manaMultiplier = floor(self.currentStats["LEVEL"] * 0.25)
		if self.manaMultiplier < 1:
			self.manaMultiplier = 1

	def initBook(self, learntBook, book):
		for item in learntBook:
			try:
				if self.currentStats["LEVEL"] >= item["LEVEL"] and self.currentStats['CLASS'] in item['CLASS'] and item not in book:  # Ability Check
					book.append(item)
			except KeyError:
				if self.currentStats["LEVEL"] >= item["LEVEL"] and item not in book:  # Magic Check
					book.append(item)

	def initMagicLevel(self):
		for spell in Magic.spellBook:
			if spell["type"] == "OFFENSIVE" or spell["heal"] == "HP":
				spell["MANA"] = floor(spell["MANA"] * self.manaMultiplier)

	def levelUp(self, screen, pos, charInventory):
		while self.stats["XP"] >= self.currentStats["MaxXP"]:
			self.manaMultiplier = floor(self.currentStats["LEVEL"] * 0.25)
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
		if self.currentStats["CLASS"] in (Classes.Mage.stats["CLASS"], Classes.Wizard.stats["CLASS"]) and self.manaMultiplier < 1:
			self.manaMultiplier = 1
			self.initBook(Magic.learntSpells, Magic.spellBook)
			self.initMagicLevel()
		self.initBook(Abilities.learntAbilities, Abilities.abilityBook)
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
