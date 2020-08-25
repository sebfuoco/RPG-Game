from curses import A_UNDERLINE

def loopInventory(player, reward, amount):
	i = 0
	item = [player.Inventory for x in player.Inventory]
	for x in item:
		if player.Inventory[i].count(reward):
			player.Inventory[i][1] += amount
			i = "IGNORE"
			break
		i += 1
	if i != "IGNORE":
		player.Inventory.append([reward, amount])

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
	if (len(text) + pos + 2) <= maxPos and text != "tab":
		try:
			text = text.replace("tab", "")
		except AttributeError:
			pass
		addstr(i, pos, text)
	else:
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
