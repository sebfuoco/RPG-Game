from Items import *
from UI import mainUI
from curses import napms

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
			self.refresh()
			napms(1000)
	except IndexError:
		pass

def searchInventory(player, target):
	z = 0
	if target != Equipment.Empty:
		for x in player.Inventory:
			# print(x[0], player.equipped["CHEST"])
			if x[0] == target:
				# print(player.Inventory[z][1])
				player.Inventory[z][1] += 1
				break
			z += 1
			if z == len(player.Inventory):
				player.Inventory.append([target, 1])
				break

def use(self, player, temp, i, target):
	if player.stats[target] == player.currentStats["Max" + target]:  # compare HP/MP to MaxHP/MaxMP
		self.addstr(12, 35, f"{temp[0][i][0]['name']} HAD NO EFFECT")
		self.refresh()
		napms(1000)
	else:
		player.stats[target] += temp[0][i][0]["heal"]
		temp[0][i][1] -= 1
	if player.stats[target] > player.currentStats["Max" + target]:
		player.stats[target] = player.currentStats["Max" + target]
	return temp

def useItem(self, player, temp, i):
	try:
		if temp[0][i][0]["name"] == "HEALTH-POTION":
			temp = use(self, player, temp, i, "HP")
		elif temp[0][i][0]["name"] == "MANA-POTION":
			temp = use(self, player, temp, i, "MP")
		elif isinstance(temp[0][i][0]["heal"], str):
			if player.status == "POISONED":
				player.status = "NORMAL"
				temp[0][i][1] -= 1
			else:
				self.addstr(12, 35, f"{temp[0][i][0]['name']} HAD NO EFFECT")
				self.refresh()
				napms(1000)
		mainUI.characterUI(self, player)
		self.refresh()
		return temp, i
	except IndexError:
		pass

def equip(self, player, temp, i, target):
	if player.equipped[target] != temp[0][i][0]:
		searchInventory(player, player.equipped[target])
		temp[0][i][1] -= 1
		player.equipped[target] = temp[0][i][0]
		EquipmentStats(player)
	else:
		self.addstr(12, 35, f"{temp[0][i][0]['name']} ALREADY EQUIPPED")
		self.refresh()
		napms(1000)
	return temp

def equipItem(self, player, temp, i, choice):
	try:
		if temp[0][i][0]["name"] == "EMPTY":
			temp = equip(self, player, temp, i, choice)
			mainUI.charInventoryUI(self, player)
			self.refresh()
		else:
			if player.stats["CLASS"] in temp[0][i][0]["equipClass"]:
				if temp[0][i][0]["equipLocation"] == "HEAD":
					temp = equip(self, player, temp, i, "HEAD")
				elif temp[0][i][0]["equipLocation"] == "CHEST":
					temp = equip(self, player, temp, i, "CHEST")
				elif temp[0][i][0]["equipLocation"] == "HAND":
					if choice == "RIGHT":
						temp = equip(self, player, temp, i, "RIGHT-HAND")
					elif choice == "LEFT":
						temp = equip(self, player, temp, i, "LEFT-HAND")
				mainUI.charInventoryUI(self, player)
				self.refresh()
			else:
				self.addstr(12, 35, f"CANNOT EQUIP {temp[0][i][0]['name']}")
				self.refresh()
				napms(1000)
		return temp, i
	except IndexError:
		pass

def deleteItem(temp, player, i):
	y = 0
	if temp[0][i][1] == 0:
		temp[0][i][1] += 1
		for x in player.Inventory:
			if x == temp[0][i]:
				del player.Inventory[y]
				break
			y += 1
	elif temp[0][i][1] >= 1:
		z = 0
		#print(temp[0][i][0], temp[0][i][1])
		#print(x[i][0], x[i][1])
		while True:
			if player.Inventory[z][0]["name"] == temp[0][i][0]["name"]:
				#print(player.Inventory[i])
				#print(player.Inventory[z], temp[0][i])
				player.Inventory[z][1] = temp[0][i][1]
				#print(player.Inventory[z], temp[0][i])
				break
			z += 1

def EquipmentStats(player):
	strength = 0
	defense = 0
	for key, value in player.equipped.items():
		strength += value["STR"]
		defense += value["DEF"]

	player.currentStats["MaxSTR"] = player.stats["STR"] + strength
	player.currentStats["MaxDEF"] = player.stats["DEF"] + defense
