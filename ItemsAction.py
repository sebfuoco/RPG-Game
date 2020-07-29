from Items import *
from UI import mainUI
from curses import napms

def inventoryUse(target, player, addEmpty):
	temp = []
	for x in player.Inventory:
		if x[0]["type"] in target:
			temp.append([x[0], x[1]])
	if addEmpty:
		temp.append([Equipment.Empty, 1])
	temp = [temp for x in temp]
	return temp

def sellItem(self, number, amount, player):
	if player.Inventory[number]:
		if (player.Inventory[number][1] - amount) >= 0:
			player.Gold += (player.Inventory[number][0]["price"] * amount)
			player.Inventory[number][1] -= amount
	if player.Inventory[number][1] == 0:
		del player.Inventory[number]
	mainUI.charInventoryUI(self, player)
	mainUI.logUI(self)

def buyItem(self, number, amount, player, z):
	#print(player.Inventory[0])
	#print(townMerchant[z][number])
	try:
		if (townMerchant[z][number]["price"] * amount) <= player.Gold:
			i = 0
			item = [player.Inventory for x in player.Inventory]
			for x in item:
				if player.Inventory[i].count(townMerchant[z][number]):
					player.Inventory[i][1] += amount
					i = "IGNORE"
					break
				i += 1
			player.Gold -= (townMerchant[z][number]["price"] * amount)
			if i != "IGNORE":
				player.Inventory.append([townMerchant[z][number], amount])
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
	evasion = 0
	speed = 0
	for key, value in player.equipped.items():
		strength += value["STR"]
		defense += value["DEF"]
		if value["type"] == "ARMOUR":
			evasion += value["EVASION"]
		if value["type"] == "ARMOUR":
			speed += value["SPEED"]

	player.currentStats["MaxSTR"] = player.stats["STR"] + strength
	player.currentStats["MaxDEF"] = player.stats["DEF"] + defense
	player.currentStats["MaxEVASION"] = player.stats["EVASION"] + evasion
	player.currentStats["MaxSPEED"] = player.stats["SPEED"] + speed
