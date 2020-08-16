from mobs import currentMobLocation, mobList
from UI import empty

def questReward(self, player, reward, loopInventory, wrapText):
	rewards = f"YOU GAINED {reward['REWARD'][1]} {reward['REWARD'][0]['name']}, {reward['GOLD']} GOLD, and {reward['XP']} XP"
	wrapText(self, "QUEST REWARDS", rewards, 12, 35, empty, "LOG")
	loopInventory(player, reward["REWARD"][0], reward["REWARD"][1])
	player.Gold += reward["GOLD"]
	player.stats["XP"] += reward["XP"]

class quest:
	def checkQuest(self, player, z, Maps, mapNames, loopInventory, wrapText):
		i = player.activeQuests.index(Maps.currentMapQuest[z][0])
		if Maps.currentMapName == mapNames.farmName and not currentMobLocation.mobLocation:
			player.activeQuests[i][2][3] = True
		elif Maps.currentMapName == mapNames.townSquareName and currentMobLocation.killBoss[mobList.skeletonLord["name"]]:
			player.activeQuests[i][2][3] = True

		if Maps.currentMapQuest[z][0] == player.activeQuests[i] and player.activeQuests[i][2][3]:
			questReward(self, player, Maps.currentMapQuest[z][0][2][2], loopInventory, wrapText)
			del Maps.currentMapQuest[z][0]
			del player.activeQuests[i]
			return False
		return True
