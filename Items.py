class Equipment:
	# Defense Equipment
	# All Class Equipment
	Empty = {"name": "EMPTY", "type": "EQUIPMENT", "rarity": "NORMAL", "price": 0, "equipLocation": "ALL", "equipClass": ("WARRIOR", "THIEF", "MAGE"), "STR": 0, "DEF": 0}
	Clothes = {"name": "CLOTHES", "type": "ARMOUR", "rarity": "NORMAL", "price": 1, "equipLocation": "CHEST", "equipClass": ("WARRIOR", "THIEF", "MAGE"), "STR": 0, "DEF": 1, "SPEED": 0, "EVASION": 0}
	IronBuckler = {"name": "IRON-BUCKLER", "type": "ARMOUR", "rarity": "NORMAL", "price": 10, "equipLocation": "HAND", "equipClass": ("WARRIOR", "THIEF"), "STR": 0, "DEF": 1, "SPEED": 0, "EVASION": 2}

	# Warrior Equipment
	LeatherArmour = {"name": "LEATHER ARMOUR", "type": "ARMOUR", "rarity": "NORMAL", "price": 10, "equipLocation": "CHEST", "equipClass": ("WARRIOR",),
						  "STR": 0, "DEF": 2, "SPEED": 0, "EVASION": 0}
	LeatherHelmet = {"name": "LEATHER HELMET", "type": "ARMOUR", "rarity": "NORMAL", "price": 10,
					 "equipLocation": "CHEST", "equipClass": ("WARRIOR", "THIEF"),
					 "STR": 0, "DEF": 1, "SPEED": 0, "EVASION": 0}
	IronHelmet = {"name": "IRON HELMET", "type": "ARMOUR", "rarity": "NORMAL", "price": 20,
					 "equipLocation": "CHEST", "equipClass": ("WARRIOR",),
					 "STR": 0, "DEF": 2, "SPEED": 0, "EVASION": 0}
	IronArmour = {"name": "IRON ARMOUR", "type": "ARMOUR", "rarity": "NORMAL", "price": 30,
					 "equipLocation": "CHEST", "equipClass": ("WARRIOR",),
					 "STR": 0, "DEF": 3, "SPEED": 0, "EVASION": 0}
	# Mage Equipment
	Robe = {"name": "ROBE", "type": "ARMOUR", "rarity": "NORMAL", "price": 10, "equipLocation": "CHEST", "equipClass": ("MAGE",), "STR": 0, "DEF": 2, "SPEED": 0, "EVASION": 0}
	# Thief Equipment
	Bandana = {"name": "BANDANA", "type": "ARMOUR", "rarity": "NORMAL", "price": 5, "equipLocation": "HEAD", "equipClass": ("THIEF",), "STR": 0, "DEF": 1, "SPEED": 1, "EVASION": 1}

	# Offense Equipment
	# All Class Equipment
	Knife = {"name": "KNIFE", "type": "WEAPON", "rarity": "NORMAL", "price": 10, "equipLocation": "HAND", "equipClass": ("WARRIOR", "THIEF", "MAGE"), "STR": 2, "DEF": 0}
	# Warrior Equipment
	WoodenSword = {"name": "WOODEN SWORD", "type": "WEAPON", "rarity": "NORMAL", "price": 1, "equipLocation": "HAND", "equipClass": ("WARRIOR", "THIEF"),
				   "STR": 1, "DEF": 0}
	IronSword = {"name": "IRON SWORD", "type": "WEAPON", "rarity": "NORMAL", "price": 60, "equipLocation": "HAND",
				   "equipClass": ("WARRIOR", "THIEF"),
				   "STR": 7, "DEF": 0}
	# Mage Equipment
	WoodenWand = {"name": "WOODEN WAND", "type": "WEAPON", "rarity": "NORMAL", "price": 1, "equipLocation": "HAND", "equipClass": ("MAGE",), "STR": 1, "DEF": 0}
	# Thief Equipment
	Dagger = {"name": "DAGGER", "type": "WEAPON", "rarity": "NORMAL", "price": 40, "equipLocation": "HAND", "equipClass": ("WARRIOR", "THIEF", "MAGE"), "STR": 5, "DEF": 0}

class Items:
	HealthPotion = {"name": "HEALTH POTION", "type": "ITEM", "price": 10, "heal": 20}
	SuperHealthPotion = {"name": "S-HEALTH POTION", "type": "ITEM", "price": 30, "heal": 50}
	ManaPotion = {"name": "MANA POTION", "type": "ITEM", "price": 20, "heal": 20}
	SuperManaPotion = {"name": "S-MANA POTION", "type": "ITEM", "price": 40, "heal": 50}
	Antidote = {"name": "ANTIDOTE", "type": "ITEM", "price": 5, "heal": "POISON"}

	# Throwables
	HolyWater = {"name": "HOLY WATER", "type": "ITEM", "price": 50, "heal": 25}

townMerchant = {"44": (Equipment.Knife, Equipment.Dagger), "84": (Equipment.LeatherArmour, Equipment.Robe, Equipment.Bandana), "124": (Items.HealthPotion, Items.ManaPotion, Items.Antidote)}
