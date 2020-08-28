from mobs import currentMobLocation, mobList
from UI import empty

def startQuestReward(self, player, reward, loopInventory, wrapText):
	rewards = f"YOU GAINED {reward[1]} {reward[0]['name']}"
	wrapText(self, "GIVEN ITEM", rewards, 12, 35, empty, "LOG")
	loopInventory(player, reward[0]['name'], reward[1])

def questReward(self, player, reward, loopInventory, wrapText):
	rewards = f"YOU GAINED {reward['REWARD'][1]} {reward['REWARD'][0]['name']}, {reward['GOLD']} GOLD, and {reward['XP']} XP"
	wrapText(self, "QUEST REWARDS", rewards, 12, 35, empty, "LOG")
	loopInventory(player, reward["REWARD"][0], reward["REWARD"][1])
	player.Gold += reward["GOLD"]
	player.stats["XP"] += reward["XP"]

class quest:
	numberQuest = 0
	def checkQuest(self, player, z, Maps, mapNames, loopInventory, wrapText, QuestItems):
		i = player.activeQuests.index(Maps.currentMapQuest[z][0])
		if Maps.currentMapName == mapNames.elders_homeName and not player.keyItems.get(QuestItems.letter["name"]) and quest.numberQuest == 0:
			player.activeQuests[i][3][3] = True
			quest.numberQuest += 1
		elif Maps.currentMapName == mapNames.elders_homeName and currentMobLocation.killBoss[mobList.skeletonLord["name"]] is None and quest.numberQuest == 1:
			player.activeQuests[i][3][3] = True
			quest.numberQuest += 1
		elif Maps.currentMapName == mapNames.farmName and player.visitedMap.get(mapNames.farmName) == []:
			player.activeQuests[i][3][3] = True
		elif Maps.currentMapName == mapNames.townSquareName and player.visitedMap.get(mapNames.kingStarPubName) == []:
			player.activeQuests[i][3][3] = True
		if Maps.currentMapQuest[z][0] == player.activeQuests[i] and player.activeQuests[i][3][3]:
			questReward(self, player, Maps.currentMapQuest[z][0][3][2], loopInventory, wrapText)
			del Maps.currentMapQuest[z][0]
			del player.activeQuests[i]
			return False
		return True
