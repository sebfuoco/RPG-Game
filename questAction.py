from mobs import currentMobLocation
from UI import empty

def questReward(self, player, reward, loopInventory, wrapText):
	rewards = f"YOU GAINED {reward['REWARD'][1]} {reward['REWARD'][0]['name']}, {reward['GOLD']} GOLD, and {reward['XP']} XP"
	wrapText(self, "QUEST REWARDS", rewards, 12, 35, empty, "LOG")
	loopInventory(player, reward["REWARD"][0], reward["REWARD"][1])
	player.Gold += reward["GOLD"]
	player.stats["XP"] += reward["XP"]

class quest:
	def checkQuest(self, player, z, Maps, mapNames, loopInventory, wrapText):
		i = 0
		if Maps.currentMapName == mapNames.farmName:
			if not currentMobLocation.mobLocation:
				while i < len(player.activeQuests):
					if Maps.currentMapQuest[z][0] == player.activeQuests[i]:
						questReward(self, player, Maps.currentMapQuest[z][0][2][2], loopInventory, wrapText)
						del Maps.currentMapQuest[z][0]
						del player.activeQuests[i]
						break
					i += 1
