class Equipment:
	# Defense Equipment
	# All Class Equipment
	Empty = {"name": "EMPTY", "price": 0, "equipLocation": "ALL", "equipClass": "ALL", "STR": 0, "DEF": 0}
	Clothes = {"name": "CLOTHES", "type": "ARMOUR", "price": 1, "equipLocation": "CHEST", "equipClass": "ALL", "STR": 0, "DEF": 1}
	# Warrior Equipment
	LeatherArmour = {"name": "LEATHER-ARMOUR", "type": "ARMOUR", "price": 10, "equipLocation": "CHEST", "equipClass": "WARRIOR",
						  "STR": 0, "DEF": 2}
	# Mage Equipment
	Robe = {"name": "ROBE", "type": "ARMOUR", "price": 10, "equipLocation": "CHEST", "equipClass": "MAGE", "STR": 0, "DEF": 2}
	# Thief Equipment
	Bandana = {"name": "BANDANA", "type": "ARMOUR", "price": 5, "equipLocation": "HEAD", "equipClass": "THIEF", "STR": 0, "DEF": 1}
	# Offense Equipment
	# All Class Equipment
	Knife = {"name": "KNIFE", "type": "WEAPON", "price": 10, "equipLocation": "HAND", "equipClass": "ALL", "STR": 2, "DEF": 0}
	# Warrior Equipment
	WoodenSword = {"name": "WOODEN-SWORD", "type": "WEAPON", "price": 1, "equipLocation": "HAND", "equipClass": ("WARRIOR", "THIEF"),
				   "STR": 1, "DEF": 0}
	# Mage Equipment
	WoodenWand = {"name": "WOODEN WAND", "type": "WEAPON", "price": 1, "equipLocation": "HAND", "equipClass": "MAGE", "STR": 1, "DEF": 0}
	# Thief Equipment
	Dagger = {"name": "DAGGER", "type": "WEAPON", "price": 40, "equipLocation": "HAND", "equipClass": "ALL", "STR": 5, "DEF": 0}

class Items:
	HealthPotion = {"name": "HEALTH-POTION", "type": "ITEM", "price": 10, "heal": 20}
	ManaPotion = {"name": "MANA-POTION", "type": "ITEM", "price": 20, "heal": 20}
	Antidote = {"name": "ANTIDOTE", "type": "ITEM", "price": 5, "heal": "POISON"}

townMerchant = {"44": (Equipment.Knife, Equipment.Dagger), "84": (Equipment.LeatherArmour, Equipment.Robe, Equipment.Bandana), "124": (Items.HealthPotion, Items.ManaPotion, Items.Antidote)}
