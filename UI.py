import curses

from Map import *
class mainUI:
	def worldUI(self):
		i = 0
		pos = 0
		loopUI(i, pos, Maps.currentMap, self)
		mainUI.mapNameUI(self)
		# CHARACTER
		mainUI.characterUI(self)
		# INVENTORY
		mainUI.charInventoryUI(self)
		# COMMANDS
		mainUI.commandsUI(self)

	def characterUI(self):
		quickCharacter = [["+-----------------------------+"],
						  ["| WARRIOR                     |"],
						  ["| HEALTH: 20 / 20             |"],
						  ["| MANA:   0 / 0               |"],
						  ["+-----------------------------+"]]
		i = 6
		pos = 33
		loopUI(i, pos, quickCharacter, self)

	def charInventoryUI(self):
		charInv = [["+-----------------------------+"],
				   ["| STR: 5   DEF: 3             |"],
				   ["| HEAD: EMPTY                 |"],
				   ["| CHEST: LEATHER-BREASTPLATE  |"],
				   ["| LEFT-ARM: EMPTY             |"],
				   ["| RIGHT-ARM: WOODEN-SWORD     |"],
				   ["+-----------------------------+"]]
		i = 0
		pos = 33
		loopUI(i, pos, charInv, self)

	def commandsUI(self):
		commands = [["+-----------------------------+"],
					["| INVENTORY   ATTACK   TALK   |"],
					["|                             |"],
					["|                             |"],
					["+-----------------------------+"]]
		i = 10
		pos = 33
		loopUI(i, pos, commands, self)

	def mapNameUI(self):
		mapName = [["+------------------------------+"],
				   ["|                              |"],
				   ["+------------------------------+"]]
		i = 15
		pos = 0
		loopUI(i, pos, mapName, self)
		self.addstr(16, 2, Maps.currentMapData["name"])

	def inventory(self):
		commands = [["+------------------------------+"],
					["| POTION                       |"],
					["| CLOTHES                      |"],
					["| WOODEN-SWORD                 |"],
					["+------------------------------+"]]
		i = 0
		pos = 32
		loopUI(i, pos, commands, self)

def loopUI(i, pos, item, screen):
	for r in item:
		for c in r:
			screen.addstr(i, pos, c)
			i += 1
