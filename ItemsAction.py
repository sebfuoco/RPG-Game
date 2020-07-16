from Items import *
from UI import mainUI

def buyItem(self, number, player, z):
	#print(player.Inventory[0])
	#print(townMerchant[z][number])
	try:
		if townMerchant[z][number]["price"] <= player.Gold:
			i = 0
			item = [player.Inventory for x in player.Inventory]
			for x in item:
				if player.Inventory[i].count(townMerchant[z][number]):
					player.Inventory[i][1] += 1
					i = "IGNORE"
					break
				i += 1
			player.Gold -= townMerchant[z][number]["price"]
			if i != "IGNORE":
				player.Inventory.append([townMerchant[z][number], 1])
			mainUI.charInventoryUI(self, player)
		else:
			mainUI.clearOptionalUI(self)
			self.addstr(0, 66, "NOT ENOUGH GOLD")
	except IndexError:
		pass

def useItem(self, player, temp, i):
	try:
		if temp[0][i][0]["name"] == "HEALTH-POTION":
			if player.stats["HP"] == player.currentStats["MaxHP"]:
				self.addstr(12, 35, f"{temp[0][i][0]['name']} HAD NO EFFECT")
			else:
				player.stats["HP"] += temp[0][i][0]["heal"]
				temp[0][i][1] -= 1
		elif temp[0][i][0]["name"] == "MANA-POTION":
			if player.stats["MP"] == player.currentStats["MaxMP"]:
				self.addstr(12, 35, f"{temp[0][i][0]['name']} HAD NO EFFECT")
			else:
				player.stats["MP"] += temp[0][i][0]["heal"]
				temp[0][i][1] -= 1
		elif isinstance(temp[0][i][0]["heal"], str):
			if player.status == "POISONED":
				player.status = "NORMAL"
				temp[0][i][1] -= 1
			else:
				self.addstr(12, 35, f"{temp[0][i][0]['name']} HAD NO EFFECT")
		if player.stats["HP"] > player.currentStats["MaxHP"]:
			player.stats["HP"] = player.currentStats["MaxHP"]
		elif player.stats["MP"] > player.currentStats["MaxMP"]:
			player.stats["MP"] = player.currentStats["MaxMP"]
		mainUI.characterUI(self, player)
		self.refresh()
		return temp
	except IndexError:
		pass

def equipItem(self, player, temp, i):
	print(temp[0][i][0])

	if temp[0][i][0]["equipLocation"] == "HEAD":
		player.equipped["HEAD"] = temp[0][i][0]
	elif temp[0][i][0]["equipLocation"] == "CHEST":
		player.equipped["CHEST"] = temp[0][i][0]
		temp[0][i][1] -= 1
	elif temp[0][i][0]["equipLocation"] == "HAND":
		player.equipped["RIGHT-HAND"] = temp[0][i][0]

	mainUI.charInventoryUI(self, player)
	self.refresh()
	return temp

def deleteItem(player, item):
	i = 0
	for x in item:
		if x[0][1] == 0:
			del x[0]
			del player.Inventory[i]
		i += 1
