class mobList:
	weakness = {"SUPERWEAK": 2, "WEAK": 1.5, "IMMUNE": 0}
	goblin = {"name": "GOBLIN", "type": "NORMAL", "HP": 10, "STR": 4, "DEF": 0, "SPEED": 3, "XP": 5, "GOLD": 2,
			  "ICON": "g"}
	rat = {"name": "RAT", "type": "NORMAL", "HP": 8, "STR": 6, "DEF": 0, "SPEED": 5, "XP": 8, "GOLD": 4, "ICON": "r"}
	spider = {"name": "SPIDER", "type": "NORMAL", "weakness": ["FIRE", weakness["WEAK"]], "inflict": ("POISONED", 30),
			  "HP": 15, "STR": 6, "DEF": 0, "SPEED": 8, "XP": 12, "GOLD": 6, "ICON": "s"}
	queenSpider = {"name": "QUEEN SPIDER", "type": "BOSS", "weakness": ["FIRE", weakness["WEAK"]],
				   "inflict": ("POISONED", 30), "HP": 50, "STR": 8, "DEF": 2, "SPEED": 3, "XP": 50, "GOLD": 50,
				   "ICON": "q"}
	skeleton = {"name": "SKELETON", "type": "NORMAL", "weakness": ["HOLY", weakness["SUPERWEAK"]], "HP": 30, "STR": 6,
				"DEF": 2, "SPEED": 4, "XP": 30, "GOLD": 20, "ICON": "ŝ"}
	skeletonLord = {"name": "SKELETON LORD", "type": "BOSS", "weakness": ["HOLY", weakness["SUPERWEAK"]], "HP": 200,
					"STR": 10, "DEF": 5, "SPEED": 1, "XP": 100, "GOLD": 100, "ICON": "§"}
	bandit = {"name": "BANDIT", "type": "NORMAL", "HP": 20, "STR": 6, "DEF": 2, "SPEED": 5,
			  "XP": 10, "GOLD": 20, "ICON": "b"}
	soldier = {"name": "SOLDIER", "type": "NORMAL", "HP": 50, "STR": 10, "DEF": 5, "SPEED": 3,
			   "XP": 50, "GOLD": 10, "ICON": "ś"}
	evilMage = {"name": "EVIL MAGE", "type": "NORMAL", "HP": 30, "STR": 2, "MagicSTR": 2, "DEF": 2, "SPEED": 3,
				"XP": 30, "GOLD": 30, "ICON": "m"}

class mobIcons:
	mobs = {}
	list = list(vars(mobList).values())[2:-3]
	for mob in list:
		temp = {mob['ICON']: mob}
		mobs.update(temp)

class currentMobLocation:
	mobLocation = []
	killBoss = {mobList.queenSpider["name"]: False, mobList.skeletonLord["name"]: False}
