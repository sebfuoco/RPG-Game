from Map import *
class mainUI:
	def worldUI(self, player):
		i = 0
		pos = 0
		loopUI(i, pos, Maps.currentMap, self)
		mainUI.mapNameUI(self)
		# CHARACTER
		mainUI.characterUI(self, player)
		# INVENTORY
		mainUI.charInventoryUI(self, player)
		# COMMANDS
		mainUI.commandsUI(self)

	def characterUI(self, player):
		quickCharacter =   [["+-----------------------------+"],
							[f"| {player.stats['CLASS']}|"],
							[f"| HP: {player.stats['HP']} / {player.currentStats['MaxHP']}                 |"],
							[f"| MP:   {player.stats['MP']} / {player.currentStats['MaxMP']}               |"],
							["+-----------------------------+"]]
		i = 6
		pos = 33
		loopUI(i, pos, quickCharacter, self)

	def charInventoryUI(self, player):
		charInv =  [["+-----------------------------+"],
					[f"| STR: {player.stats['STR']}   DEF: {player.stats['DEF']}             |"],
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
		mapName =  [["+------------------------------+"],
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
