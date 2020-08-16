class mobList:
	goblin = {"name": "GOBLIN", "type": "NORMAL", "weakness": "NONE", "HP": 10, "STR": 4, "DEF": 0, "SPEED": 3, "XP": 5, "GOLD": 2, "ICON": "g"}
	rat = {"name": "RAT", "type": "NORMAL", "weakness": "NONE", "HP": 8, "STR": 8, "DEF": 0, "SPEED": 4, "XP": 8, "GOLD": 4, "ICON": "r"}
	spider = {"name": "SPIDER", "type": "NORMAL", "weakness": "FIRE", "inflict": ("POISONED", 30), "HP": 15, "STR": 6, "DEF": 0, "SPEED": 8, "XP": 12, "GOLD": 6, "ICON": "s"}
	queenSpider = {"name": "QUEEN SPIDER", "type": "BOSS", "weakness": "FIRE", "inflict": ("POISONED", 30), "HP": 50, "STR": 6, "DEF": 2, "SPEED": 3, "XP": 50, "GOLD": 50, "ICON": "q"}
	skeleton = {"name": "SKELETON", "type": "NORMAL", "weakness": "LIGHT", "HP": 30, "STR": 6, "DEF": 2, "SPEED": 4, "XP": 30, "GOLD": 20, "ICON": "ŝ"}
	skeletonLord = {"name": "SKELETON LORD", "type": "BOSS", "weakness": "LIGHT", "HP": 200, "STR": 10, "DEF": 5, "SPEED": 1, "XP": 100, "GOLD": 100, "ICON": "§"}

class mobIcons:
	mobs = {}
	list = list(vars(mobList).values())[1:-3]
	for mob in list:
		temp = {mob['ICON']: mob}
		mobs.update(temp)

class currentMobLocation:
	mobLocation = []
	killBoss = {mobList.queenSpider["name"]: False, mobList.skeletonLord["name"]: False}
