class Equipment:
	# STR, DEF, SPEED, EVASION, ELEMENT
	# Defense Equipment
	# All Class Equipment
	Empty = {"name": "EMPTY", "type": "EQUIPMENT", "rarity": "NORMAL", "price": 0, "equipLocation": "ALL", "equipClass": ("WARRIOR", "THIEF", "MAGE")}
	Clothes = {"name": "CLOTHES", "type": "ARMOUR", "rarity": "NORMAL", "price": 1, "equipLocation": "CHEST", "equipClass": ("WARRIOR", "THIEF", "MAGE"), "DEF": 1}

	# Multiple Class Equipment
	IronBuckler = {"name": "IRON BUCKLER", "type": "ARMOUR", "rarity": "NORMAL", "price": 10, "equipLocation": "HAND", "equipClass": ("WARRIOR", "THIEF"), "DEF": 1, "EVASION": 2}

	# Warrior Equipment
	LeatherShield = {"name": "LEATHER SHIELD", "type": "ARMOUR", "rarity": "NORMAL", "price": 10, "equipLocation": "HAND", "equipClass": ("WARRIOR",),
					 "STR": 0, "DEF": 1, "SPEED": 0, "EVASION": 3}
	LeatherArmour = {"name": "LEATHER ARMOUR", "type": "ARMOUR", "rarity": "NORMAL", "price": 10, "equipLocation": "CHEST", "equipClass": ("WARRIOR",),
						  "STR": 0, "DEF": 2, "SPEED": 0, "EVASION": -1}
	LeatherHelmet = {"name": "LEATHER HELMET", "type": "ARMOUR", "rarity": "NORMAL", "price": 10,
					 "equipLocation": "CHEST", "equipClass": ("WARRIOR", "THIEF"),
					 "DEF": 1}
	IronHelmet = {"name": "IRON HELMET", "type": "ARMOUR", "rarity": "NORMAL", "price": 20,
					 "equipLocation": "CHEST", "equipClass": ("WARRIOR",),
					 "DEF": 2}
	IronArmour = {"name": "IRON ARMOUR", "type": "ARMOUR", "rarity": "NORMAL", "price": 30,
					 "equipLocation": "CHEST", "equipClass": ("WARRIOR",),
					 "DEF": 3, "EVASION": -2}
	# Mage Equipment
	Robe = {"name": "ROBE", "type": "ARMOUR", "rarity": "NORMAL", "price": 10, "equipLocation": "CHEST", "equipClass": ("MAGE",), "DEF": 2}
	# Thief Equipment
	Bandana = {"name": "BANDANA", "type": "ARMOUR", "rarity": "NORMAL", "price": 5, "equipLocation": "HEAD", "equipClass": ("THIEF",), "DEF": 1, "SPEED": 1, "EVASION": 1}

	# Offense Equipment
	# All Class Equipment
	Knife = {"name": "KNIFE", "type": "WEAPON", "rarity": "NORMAL", "price": 10, "equipLocation": "HAND", "equipClass": ("WARRIOR", "THIEF", "MAGE"), "STR": 2}
	Dagger = {"name": "DAGGER", "type": "WEAPON", "rarity": "NORMAL", "price": 40, "equipLocation": "HAND",
			  "equipClass": ("WARRIOR", "THIEF", "MAGE"), "STR": 5, "SPEED": 1}
	# Warrior Equipment
	WoodenSword = {"name": "WOODEN SWORD", "type": "WEAPON", "rarity": "NORMAL", "price": 1, "equipLocation": "HAND", "equipClass": ("WARRIOR", "THIEF"),
				   "STR": 1}
	IronSword = {"name": "IRON SWORD", "type": "WEAPON", "rarity": "NORMAL", "price": 60, "equipLocation": "HAND",
				   "equipClass": ("WARRIOR", "THIEF"),
				   "STR": 7}
	SteelSword = {"name": "STEEL SWORD", "type": "WEAPON", "rarity": "NORMAL", "price": 100, "equipLocation": "HAND",
				 "equipClass": ("WARRIOR", "THIEF"),
				 "STR": 10}
	# Mage Equipment
	WoodenWand = {"name": "WOODEN WAND", "type": "WEAPON", "rarity": "NORMAL", "price": 1, "equipLocation": "HAND", "equipClass": ("MAGE",), "STR": 1}
	WoodenStaff = {"name": "WOODEN STAFF", "type": "WEAPON", "rarity": "NORMAL", "price": 20, "equipLocation": "HAND", "equipClass": ("MAGE",), "STR": 2}
	# Thief Equipment
	Rapier = {"name": "RAPIER", "type": "WEAPON", "rarity": "NORMAL", "price": 40, "equipLocation": "HAND",
			  "equipClass": ("THIEF",), "STR": 7}
class Items:
	Gold = {"name": "GOLD", "type": "GOLD"}
	HealthPotion = {"name": "HEALTH POTION", "description": f"HEALS 20 HEALTH", "type": "ITEM", "throwable": False, "price": 10, "heal": 20}
	SuperHealthPotion = {"name": "S-HEALTH POTION", "description": f"HEALS 50 HEALTH", "type": "ITEM", "throwable": False, "price": 30, "heal": 50}
	ManaPotion = {"name": "MANA POTION", "description": "HEALS 20 MANA", "type": "ITEM", "throwable": False, "price": 20, "heal": 20}
	SuperManaPotion = {"name": "S-MANA POTION", "description": "HEALS 50 MANA", "type": "ITEM", "throwable": False, "price": 40, "heal": 50}
	Antidote = {"name": "ANTIDOTE", "description": "HEALS POISON", "type": "ITEM", "throwable": False, "price": 5, "heal": "POISON"}

	# Throwables
	HolyWater = {"name": "HOLY WATER", "description": "DEALS 25 HOLY DAMAGE TO ENEMIES, IGNORES DEFENSE", "type": "ITEM", "throwable": True, "price": 50, "damage": 25, "ELEMENT": "HOLY"}
	ThrowingKnife = {"name": "THROWING KNIFE", "description": "DEALS 10 DAMAGE TO ENEMIES, IGNORES DEFENSE", "type": "ITEM", "throwable": True, "price": 10, "damage": 10}

class QuestItems:
	letter = {"name": "LETTER", "type": "QUEST"}
	skeletonKey = {"name": "SKELETON KEY", "type": "QUEST"}
	royalCoin = {"name": "ROYAL COIN", "type": "QUEST"}
	skeletonCrown = {"name": "SKELETON CROWN", "type": "QUEST"}
