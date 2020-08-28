from curses import A_UNDERLINE

def loopInventory(player, reward, amount):
	i = 0
	item = [player.Inventory for _ in player.Inventory]
	if reward["type"] == "QUEST":
		player.keyItems[reward["name"]] = reward["name"]
	for _ in item:
		if player.Inventory[i].count(reward):
			player.Inventory[i][1] += amount
			i = "IGNORE"
			break
		i += 1
	if i != "IGNORE":
		player.Inventory.append([reward, amount])

def newLine(text, addstr, i, maxPos, startPos, pos, mapUI):
	output = text.split()
	for word in output:
		if (len(word) + pos) < maxPos and "tab" not in word:
			addstr(i, pos, word)
			pos += len(word) + 1
		else:
			pos = startPos
			i += 1
			addstr(i, 65, mapUI[1][0])
			if word != "tab":
				addstr(i, pos, word.lstrip())
				pos += len(word) + 1
	addstr(i + 1, 65, mapUI[0][0])

def wrapText(addstr, title, text, i, pos, mapUI, location):
	startPos = pos
	if location == "SIDE":
		maxPos = pos + 34
	else:
		maxPos = pos + 29
	# TITLE
	addstr(i-1, 65, mapUI[0][0])
	addstr(i, 65, mapUI[1][0])
	if len(title) + 2 <= maxPos:
		addstr(i, pos, title, A_UNDERLINE)
	i += 1
	addstr(i, 65, mapUI[1][0])
	# TEXT
	newLine(text, addstr, i, maxPos, startPos, pos, mapUI)
