import MapAction
import mobs
from curses import wrapper
from UI import *
from Map import Maps, mapNames
from ItemsAction import *  # Imports Items file as well
from questAction import quest
from UIAction import loopInventory, wrapText, newLine
from player import Classes, Player, Magic, Abilities
from mobAction import attack, mobMove

# check OS, Windows works differently than Linux, supporting less colour.
from sys import platform
class OS:
    if platform == "linux":
        OS = "LINUX"
    elif platform == "win32":
        OS = "WINDOWS"

def my_raw_input(screen, r, c, prompt_string, charlength):
    curses.curs_set(1)
    curses.echo()
    screen.addstr(r, c, "                          ")
    screen.addstr(r, c, prompt_string)
    screen.refresh()
    input = screen.getstr(r + 1, c, charlength)
    screen.addstr(r + 1, c, "                   ")
    screen.move(r + 1, c)
    curses.noecho()
    return input

def loadMap(self, yCoord, xCoord, player):
    spawnLocation = MapAction.respawnData(yCoord, xCoord, Maps)
    yCoord, xCoord = MapAction.loadNextMap(yCoord, xCoord, spawnLocation, Maps)
    self.clear()
    size = mainUI.worldUI(self, player, Maps, OS.OS)
    entityMap(self, Maps.currentMapMobs, mobs, Maps.currentMap, Maps.currentMapInfo, Maps.currentMapQuest, Maps.currentMapMerchant, OS.OS)
    chestMap(self, Maps.currentMapChest, OS.OS)
    EquipmentStats(self, player, mainUI.charInventoryUI)
    for spell in Magic.spellBook:
        if "STAT" in spell["type"]:
            spell["cast"] = 0
    return yCoord, xCoord, spawnLocation, size

def move(self, color_pair, direction, yCoord, xCoord, spawnLocation, player, attackType, mobCounter):
    originalCoord = {"yCoord": yCoord, "xCoord": xCoord}
    if direction == "UP":
        yCoord -= 1
    elif direction == "DOWN":
        yCoord += 1
    elif direction == "LEFT":
        xCoord -= 1
    elif direction == "RIGHT":
        xCoord += 1
    x = MapAction.detectCollision(self, yCoord, xCoord, mobs.mobIcons.mobs)
    if x:
        if x == "loadMap":
            yCoord, xCoord, spawnLocation, size = loadMap(self, originalCoord["yCoord"], originalCoord["xCoord"], player)
            yCoord, xCoord = MapAction.moveEntity(self, color_pair, yCoord, xCoord, "@", 16)
        elif x == "Merchant":
            choice = my_raw_input(self, 12, 35, "BUY OR SELL?", 4).decode("utf-8").upper()
            mainUI.logUI(self)
            if choice in ("BUY", "B"):
                try:
                    z = str(str(yCoord) + str(xCoord))
                    i = mainUI.merchantUI(self, yCoord, xCoord, Maps.currentMapMerchant)
                    number = int(my_raw_input(self, 12, 35, "WHAT WILL YOU BUY?", 1).decode("utf-8")) - 1
                    if (number + 1) > i:
                        raise ValueError
                    mainUI.logUI(self)
                    amount = int(my_raw_input(self, 12, 35, "HOW MANY WILL YOU BUY?", 1).decode("utf-8"))
                    mainUI.logUI(self)
                    buyItem(self, number, amount, player, z, Maps.currentMapMerchant, loopInventory, mainUI.clearOptionalUI)
                except ValueError:
                    mainUI.logUI(self)
                    pass
                mainUI.clearOptionalUI(self)
            elif choice in ("SELL", "S"):
                temp = inventoryUse(("ARMOUR", "WEAPON", "ITEM"), player, False)
                try:
                    if temp:
                        try:
                            mainUI.initWrap(self, None, temp, "INVENTORY")
                            number = int(my_raw_input(self, 12, 35, "WHAT WILL YOU SELL?", 1).decode("utf-8")) - 1
                            if number + 1 > len(temp):
                                raise ValueError
                            mainUI.logUI(self)
                            amount = int(my_raw_input(self, 12, 35, "HOW MANY WILL YOU SELL?", 1).decode("utf-8"))
                            sellItem(self, number, amount, player, mainUI.charInventoryUI, mainUI.logUI)
                        except ValueError:
                            mainUI.logUI(self)
                            pass
                        mainUI.clearOptionalUI(self)
                except ValueError:
                    pass
            yCoord, xCoord = MapAction.moveEntity(self, color_pair, originalCoord["yCoord"], originalCoord["xCoord"], "@", 16)
        elif x == "Chest":
            mainUI.chestUI(self, yCoord, xCoord, player, Maps)
            yCoord, xCoord = MapAction.moveEntity(self, color_pair, originalCoord["yCoord"], originalCoord["xCoord"], "@", 16)
        elif x == "Quest":
            mainUI.questUI(self, player, yCoord, xCoord, Maps, mapNames, quest, QuestItems)
            yCoord, xCoord = MapAction.moveEntity(self, color_pair, originalCoord["yCoord"], originalCoord["xCoord"], "@", 16)
        elif x == "Information":
            mainUI.informationUI(self, yCoord, xCoord, Maps, mobs, player, QuestItems, OS.OS)
            yCoord, xCoord = MapAction.moveEntity(self, color_pair, originalCoord["yCoord"], originalCoord["xCoord"], "@", 16)
            self.refresh()
        elif x == "Attack":
            attack(self, player, yCoord, xCoord, attackType, Maps, MapAction, mobs.currentMobLocation, mainUI.charInventoryUI, newLine)
            yCoord, xCoord = MapAction.moveEntity(self, color_pair, originalCoord["yCoord"], originalCoord["xCoord"], "@", 16)
            if player.status == "POISONED":
                player.stats["HP"] -= 1
            mainUI.characterUI(self, player)
            self.refresh()
        else:
            MapAction.currentPosition(self, originalCoord["yCoord"], originalCoord["xCoord"], Maps.currentMap)
            yCoord, xCoord = MapAction.moveEntity(self, color_pair, yCoord, xCoord, "@", 16)
            if mobCounter == 0:
                mobMove(self, player, mobs.currentMobLocation.mobLocation, Maps.currentMapMobs, Maps.currentMap, MapAction.currentPosition,
                        MapAction.moveEntity, MapAction.detectCollision, mainUI.characterUI, OS.OS, curses.color_pair, yCoord, xCoord)
            elif mobCounter == 1:
                mobCounter = 0
            if player.status == "POISONED":
                player.stats["HP"] -= 1
                mainUI.characterUI(self, player)
    else:
        return originalCoord["yCoord"], originalCoord["xCoord"], spawnLocation, mobCounter
    return yCoord, xCoord, spawnLocation, mobCounter

def main(main):
    yCoord = 9
    xCoord = 15
    spawnLocation = 0
    mobCounter = 0  # go to 1 and then reset to 0,
    attackType = "PHYSICAL" 
    screen = curses.initscr()
    curses.start_color()
    curses.use_default_colors()
    for i in range(0, 100):
        curses.init_pair(i + 1, i, 0)
    """
    for i in range(0, 256):
        screen.addstr(str(i), curses.color_pair(i))
    screen.refresh()
    input = screen.getstr(3, 0, 0)
"""
    while True:
        screen.clear()
        screen.addstr(0, 0,
                f"1. Warrior | HP: {str(Classes.Warrior.stats['HP'])} MP: {str(Classes.Warrior.stats['MP'])} STR: {str(Classes.Warrior.stats['STR'])} DEF: {str(Classes.Warrior.stats['DEF'])}")
        screen.addstr(1, 0,
                      f"2. Mage    | HP: {str(Classes.Mage.stats['HP'])} MP: {str(Classes.Mage.stats['MP'])} STR: {str(Classes.Mage.stats['STR'])} DEF: {str(Classes.Mage.stats['DEF'])}")
        screen.addstr(2, 0,
                      f"3. Thief   | HP: {str(Classes.Thief.stats['HP'])} MP: {str(Classes.Thief.stats['MP'])} STR: {str(Classes.Thief.stats['STR'])} DEF: {str(Classes.Thief.stats['DEF'])}")
        choice = my_raw_input(screen, 3, 0, "Type in a number below:", 1).decode("utf-8")
        screen.refresh()
        if choice == "1":
            player = Player(Classes.Warrior.stats["CLASS"], Classes.Warrior.stats, Classes.Warrior.nextLevel, Classes.Warrior.equipped)
            break
        elif choice == "2":
            player = Player(Classes.Mage.stats["CLASS"], Classes.Mage.stats, Classes.Mage.nextLevel, Classes.Mage.equipped)
            player.initBook(Magic.learntSpells, Magic.spellBook)
            player.initMagicLevel()
            Magic.selectedMagic = Magic.spellBook[0]
            break
        elif choice == "3":
            player = Player(Classes.Thief.stats["CLASS"], Classes.Thief.stats, Classes.Thief.nextLevel, Classes.Thief.equipped)
            break
        else:
            screen.clear()
            screen.addstr(0, 0, "Not an option")
            screen.refresh()
            curses.napms(500)
    player.initBook(Abilities.learntAbilities, Abilities.abilityBook)
    EquipmentStats(screen, player, mainUI.charInventoryUI)
    screen.clear()
    size = mainUI.worldUI(screen, player, Maps, OS.OS)
    MapAction.moveEntity(screen, curses.color_pair, yCoord, xCoord, "@", 16)
    entityMap(screen, Maps.currentMapMobs, mobs, Maps.currentMap, Maps.currentMapInfo, Maps.currentMapQuest, Maps.currentMapMerchant, OS.OS)
    curses.noecho()
    screen.move(12, 35)
    screen.refresh()
    while size:
        player.visitedMap[Maps.currentMapName] = mobs.currentMobLocation.mobLocation
        curses.curs_set(0)
        if player.stats["HP"] <= 0:
            mainUI.logUI(screen)
            screen.refresh()
            screen.addstr(12, 35, f"YOU DIED")
            screen.refresh()
            curses.napms(2000)
            break
        key = screen.getch()
        mainUI.logUI(screen)
        mainUI.clearOptionalUI(screen)
        if key == curses.KEY_HOME:
            break
        # MOVEMENT
        elif key == curses.KEY_UP:
            yCoord, xCoord, spawnLocation, mobCounter = move(screen, curses.color_pair, "UP", yCoord, xCoord, spawnLocation, player, attackType, mobCounter)
        elif key == curses.KEY_DOWN:
            yCoord, xCoord, spawnLocation, mobCounter = move(screen, curses.color_pair, "DOWN", yCoord, xCoord, spawnLocation, player, attackType, mobCounter)
        elif key == curses.KEY_LEFT:
            yCoord, xCoord, spawnLocation, mobCounter = move(screen, curses.color_pair, "LEFT", yCoord, xCoord, spawnLocation, player, attackType, mobCounter)
        elif key == curses.KEY_RIGHT:
            yCoord, xCoord, spawnLocation, mobCounter = move(screen, curses.color_pair, "RIGHT", yCoord, xCoord, spawnLocation, player, attackType, mobCounter)
        elif key in range(49, 58):  # 1-9
            if player.stats["CLASS"] == "MAGE":
                try:
                    Magic.selectedMagic = Magic.spellBook[key - 49]
                    screen.addstr(12, 35, f"{Magic.selectedMagic['name']} IS NOW EQUIPPED")
                except IndexError:
                    pass
        elif key == 96:  # "`" pressed
            if player.stats["CLASS"] == "MAGE":
                if attackType == "PHYSICAL":
                    attackType = "MAGIC"
                elif attackType == "MAGIC":
                    attackType = "PHYSICAL"
                screen.addstr(12, 35, f"YOU ARE NOW USING {attackType}")
        elif key in [105, 73]:  # "i" pressed
            mainUI.clearOptionalUI(screen)
            item = [player.Inventory for _ in player.Inventory]
            mainUI.initWrap(screen, None, item, "INVENTORY")
        elif key in [107, 75]:  # "k" pressed
            mainUI.clearOptionalUI(screen)
            mainUI.initWrap(screen, None, player.keyItems, "KEY ITEMS")
        elif key in [99, 67]:  # "c" pressed
            curses.curs_set(1)
            mainUI.clearOptionalUI(screen)
            command = my_raw_input(screen, 12, 35, "WHAT WOULD YOU LIKE TO DO?", 8).decode("utf-8").upper()
            mainUI.logUI(screen)
            if command == "HELP":
                print("USE")
                print("EQUIP")
            elif command in ("U", "USE"):
                temp = inventoryUse(("ITEM",), player, False)
                if temp:
                    mainUI.initWrap(screen, None, temp, "INVENTORY")
                    try:
                        answer = int(my_raw_input(screen, 12, 35, "WHICH ITEM TO USE?", 1).decode("utf-8")) - 1
                        mainUI.logUI(screen)
                        mainUI.clearOptionalUI(screen)
                        temp, i = useItem(screen, player, temp, answer, mainUI.characterUI)
                        deleteItem(temp, player, i)
                    except (TypeError, ValueError):
                        pass
                else:
                    screen.addstr(12, 35, f"NOTHING TO USE")
                    screen.refresh()
                    curses.napms(1000)
                mainUI.logUI(screen)
                mainUI.clearOptionalUI(screen)
            elif command in ("E", "EQUIP"):
                temp = inventoryUse(("ARMOUR", "WEAPON"), player, True)
                if temp:
                    mainUI.initWrap(screen, None, temp, "INVENTORY")
                    try:
                        answer = int(my_raw_input(screen, 12, 35, "WHICH ITEM TO EQUIP?", 1).decode("utf-8")) - 1
                        mainUI.logUI(screen)
                        mainUI.clearOptionalUI(screen)
                        try:
                            if temp[0][answer][0]["equipLocation"] == "HAND":
                                choice = my_raw_input(screen, 12, 35, "WHICH HAND?", 5).decode("utf-8").upper()
                            else:
                                choice = temp[0][answer][0]["equipLocation"]
                            if temp[0][answer][0]["name"] == "EMPTY":
                                choice = my_raw_input(screen, 12, 35, "WHERE TO UNEQUIP?", 5).decode("utf-8").upper()
                                mainUI.logUI(screen)
                                mainUI.clearOptionalUI(screen)
                            mainUI.logUI(screen)
                            mainUI.clearOptionalUI(screen)
                            temp, i = equipItem(screen, player, temp, answer, choice, mainUI.charInventoryUI)
                            deleteItem(temp, player, i)
                        except (IndexError, KeyError):
                            mainUI.logUI(screen)
                            mainUI.clearOptionalUI(screen)
                    except ValueError:
                        pass
                else:
                    screen.addstr(12, 35, f"NOTHING TO EQUIP")
                    screen.refresh()
                    curses.napms(1000)
                screen.refresh()
                mainUI.logUI(screen)
                mainUI.clearOptionalUI(screen)
            elif command in ("EI", "EINFO"):  # gets info from equipment
                temp = inventoryUse(("WEAPON", "ARMOUR"), player, False)
                if temp:
                    mainUI.initWrap(screen, None, temp, "INVENTORY")
                    try:
                        answer = int(my_raw_input(screen, 12, 35, "WHICH ITEM TO INSPECT?", 1).decode("utf-8")) - 1
                        mainUI.logUI(screen)
                        mainUI.clearOptionalUI(screen)
                        answer = f"{temp[0][answer][0]['name']}: {temp[0][answer][0]['description']}"
                        wrapText(screen.addstr, "INFO", answer, 1, 67, UI, "SIDE")
                    except (TypeError, ValueError, IndexError):
                        pass
                else:
                    screen.addstr(12, 35, f"NOTHING TO INSPECT")
                    screen.refresh()
                    curses.napms(1000)
                mainUI.logUI(screen)
            elif command in ("I", "INFO"):  # gets info from items
                temp = inventoryUse(("ITEM",), player, False)
                if temp:
                    mainUI.initWrap(screen, None, temp, "INVENTORY")
                    try:
                        answer = int(my_raw_input(screen, 12, 35, "WHICH ITEM TO INSPECT?", 1).decode("utf-8")) - 1
                        mainUI.logUI(screen)
                        mainUI.clearOptionalUI(screen)
                        answer = f"{temp[1][answer][0]['name']}: {temp[1][answer][0]['description']}"
                        wrapText(screen.addstr, "INFO", answer, 1, 67, UI, "SIDE")
                    except (TypeError, ValueError, IndexError):
                        pass
                else:
                    screen.addstr(12, 35, f"NOTHING TO INSPECT")
                    screen.refresh()
                    curses.napms(1000)
                mainUI.logUI(screen)
            elif command in ("S", "SPELLS"):  # spells that player can use
                if player.stats["CLASS"] == "MAGE":
                    mainUI.initWrap(screen, player.currentStats['MaxMagicSTR'], Magic.spellBook, "SPELLS")
            elif command in ("C", "CAST"):  # cast support spell
                if player.stats["CLASS"] == "MAGE":
                    try:
                        showSpells = []
                        for spellType in Magic.spellBook:
                            if spellType["type"] in ("SUPPORT", "STAT"):
                                showSpells.append(spellType)
                        if showSpells:
                            mainUI.initWrap(screen, player.currentStats['MaxMagicSTR'], showSpells, "SPELLS")
                            answer = int(my_raw_input(screen, 12, 35, "WHAT SPELL TO CAST?", 1)) - 1
                            spell = showSpells[answer]
                            mainUI.logUI(screen)
                            if spell["type"] == "SUPPORT" or "STAT":
                                if player.stats["MP"] >= spell["MANA"]:
                                    if spell["heal"] == "POISON" and player.status != "NORMAL":
                                        player.status = "NORMAL"
                                        player.stats["MP"] -= spell["MANA"]
                                        mainUI.characterUI(screen, player)
                                    elif spell["heal"] in player.stats:
                                        if spell["heal"] == "HP":
                                            if player.stats["HP"] < player.currentStats["MaxHP"]:
                                                colourEntity(screen, yCoord, xCoord, {"ICON": "@"}, "HEAL")
                                                colourEntity(screen, yCoord, xCoord, {"ICON": "@"}, None)
                                                spellPower = floor(spell["POWER"] * player.currentStats["MaxMagicSTR"])
                                                player.stats[spell["heal"]] += spellPower
                                                if player.stats[spell["heal"]] > player.currentStats["Max" + spell["heal"]]:
                                                    player.stats[spell["heal"]] = player.currentStats["Max" + spell["heal"]]
                                                player.stats["MP"] -= spell["MANA"]
                                                mainUI.characterUI(screen, player)
                                                screen.refresh()
                                            else:
                                                newLine(f"{spell['name']} FAILED", screen.addstr, 12, 64, 35, 35, logEmpty)
                                        else:
                                            if spell["cast"] != 3:
                                                player.currentStats["Max" + spell["heal"]] *= spell["stat"]
                                                player.stats["MP"] -= spell["MANA"]
                                                spell["cast"] += 1
                                                mainUI.charInventoryUI(screen, player)
                                                mainUI.characterUI(screen, player)
                                                screen.refresh()
                                            else:
                                                newLine(f"CANNOT USE {spell['name']} AGAIN", screen.addstr, 12, 64, 35, 35, logEmpty)
                                    else:
                                        newLine(f"{spell['name']} FAILED", screen.addstr, 12, 64, 35, 35, logEmpty)
                                else:
                                    newLine(f"NOT ENOUGH MANA", screen.addstr, 12, 64, 35, 35, logEmpty)
                        else:
                            newLine(f"NO USABLE SPELLS TO CAST", screen.addstr, 12, 64, 35, 35, logEmpty)
                    except (ValueError, IndexError):
                        mainUI.logUI(screen)
                        pass
            elif command in ("CH", "CHARACTER"):  # display other character stats
                mainUI.initWrap(screen, None, Abilities.abilityBook, "ABILITIES")
            elif command in ("A", "ABILITY"):  # display class abilities
                mainUI.initWrap(screen, None, Abilities.abilityBook, "ABILITIES")
            elif command in ("Q", "QUESTS"):
                if not player.activeQuests:
                    screen.addstr(1, 67, "NO ACTIVE QUESTS")
                    screen.refresh()
                else:
                    active = ""
                    i = 0
                    while i < len(player.activeQuests):
                        active += f"{player.activeQuests[i][0]} IN {player.activeQuests[i][3][0]} | GOLD: {player.activeQuests[i][3][2]['GOLD']} XP: {player.activeQuests[i][3][2]['XP']} tab "
                        i += 1
                    wrapText(screen.addstr, "ACTIVE QUESTS", active, 1, 67, UI, "SIDE")
            elif command in ("C", "CHECK"):
                temp = keyItems(player.keyItems)
                wrapText(screen.addstr, "KEY ITEMS", temp, 1, 67, UI, "SIDE")
        screen.move(12, 35)
        screen.refresh()
    curses.endwin()

if __name__ == "__main__":
    wrapper(main)
