class mobList:
	goblin = {"name": "GOBLIN", "type": "NORMAL", "HP": 10, "STR": 4, "DEF": 0, "SPEED": 3, "XP": 5, "GOLD": 2, "ICON": "g"}
	rat = {"name": "RAT", "type": "NORMAL", "HP": 8, "STR": 8, "DEF": 0, "SPEED": 4, "XP": 8, "GOLD": 4, "ICON": "r"}
	spider = {"name": "SPIDER", "type": "NORMAL", "HP": 15, "STR": 6, "DEF": 0, "SPEED": 8, "XP": 12, "GOLD": 6, "ICON": "s"}
	queenSpider = {"name": "QUEEN SPIDER", "type": "BOSS", "HP": 50, "STR": 6, "DEF": 2, "SPEED": 3, "XP": 50, "GOLD": 50, "ICON": "q"}

class mobIcons:
	mobs = {mobList.goblin['ICON']: mobList.goblin, mobList.rat['ICON']: mobList.rat, mobList.spider['ICON']: mobList.spider, mobList.queenSpider['ICON']: mobList.queenSpider}

class currentMobLocation:
	mobLocation = []
