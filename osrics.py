import sys, os
from random import randint

def header():                           #Graphical Header
	print(" ---------- Osric Shinies ----------\n ")

def cont():                             #Function to continue
	input("\nPress Return to continue...")

def fail():                             #Fail Checker
	print("\nYou messed up.")
	cont()

def close():                            #Close Osric Shinies
	clear_screen()
	header()
	print("Thank you for using Osric Shinies!")
	cont()
	clear_screen()

def clear_screen():                     #Clears the screen - OS specific
	if sys.platform == 'linux2' or sys.platform == 'linux':
		os.system('clear')
	elif sys.platform == 'darwin':
		os.system('clear')
	elif sys.platform == 'win32':
		os.system('cls')
	else:
		print("\n") * 5

def int_check(a):                       #Check user input is an integer
	check = a.isdigit()
	return check

def dice(a):                            #Dice rolling function
    total = 0
    number_of_dice = a[2]
    while number_of_dice >= 1:
        roll = randint(a[0], a[1])
        number_of_dice = number_of_dice - 1
        total = total + roll
    return total

def menu_1():							#Menu 1
	clear_screen()
	header()
	print("1: Roll some Gems.")
	print("2: Roll some Jewellery.")
	print("3: Roll some random Magic Items.(disabled)")
	print("4: Roll some specific Magic Items.")
	print("5: Quit Osric Shinies.")
	choice = input("\nWhat would you like to do? > ")
	if choice == "1":
		g_j_r(gem_str)
	elif choice == "2":
		g_j_r(jewellery_str)
	elif choice == "3":
		#menu_2()
		menu_1()
	elif choice == "4":
		menu_2()
	elif choice == "5":
		close()
	else:
		fail()
		menu_1()

def item_r(function): 					#doesn't work 8(
	choice = input("\nHow many would you like to roll? > ")
	check = int_check(choice)
	if check == True and int(choice) > 0:
		clear_screen()
		header()
		amount = range(1, int(choice) + 1)
		for i in amount:
			result = function[0]
			print(function[1] + result)
		cont()
	else:
		fail()
	clear_screen()
	header()
	menu_2()

def menu_2():							#Menu 2
	clear_screen()
	header()
	print("1: Roll Armour & Shields.")
	print("2: Roll Miscelaneous Magic Weapons.")
	print("3: Roll Magic Swords.")
	print("4: Roll Potions.")
	print("5: Roll Scrolls.")
	print("6: Roll Rings.")
	print("7: Roll Rods, Staves & Wands.")
	print("8: Roll Miscellaneous Magic Items. (disabled)")
	print("9: Roll Ioun Stones.")
	print("0: Return to Main Menu.")
	choice = input("\nWhat would you like to do? > ")
	if choice == "1":
		choice = input("\nHow many would you like to roll? > ")
		check = int_check(choice)
		if check == True and int(choice) > 0:
			clear_screen()
			header()
			amount = range(1, int(choice) + 1)
			for i in amount:
				result = asf_r()
				print(result)
			cont()
		else:
			fail()
		clear_screen()
		header()
		menu_2()
	elif choice == "2":
		choice = input("\nHow many would you like to roll? > ")
		check = int_check(choice)
		if check == True and int(choice) > 0:
			clear_screen()
			header()
			amount = range(1, int(choice) + 1)
			for i in amount:
				result = mwf_r()
				print(result)
			cont()
		else:
			fail()
		clear_screen()
		header()
		menu_2()
	elif choice == "3":
		choice = input("\nHow many would you like to roll? > ")
		check = int_check(choice)
		if check == True and int(choice) > 0:
			clear_screen()
			header()
			amount = range(1, int(choice) + 1)
			for i in amount:
				result = sf_r()
				print(result)
			cont()
		else:
			fail()
		clear_screen()
		header()
		menu_2()
	elif choice == "4":
		choice = input("\nHow many would you like to roll? > ")
		check = int_check(choice)
		if check == True and int(choice) > 0:
			clear_screen()
			header()
			amount = range(1, int(choice) + 1)
			for i in amount:
				result = pot_r()
				print(result)
			cont()
		else:
			fail()
		clear_screen()
		header()
		menu_2()
	elif choice == "5":
		choice = input("\nHow many would you like to roll? > ")
		check = int_check(choice)
		if check == True and int(choice) > 0:
			clear_screen()
			header()
			amount = range(1, int(choice) + 1)
			for i in amount:
				result = st_r()
				print(result)
			cont()
		else:
			fail()
		clear_screen()
		header()
		menu_2()
	elif choice == "6":
		choice = input("\nHow many would you like to roll? > ")
		check = int_check(choice)
		if check == True and int(choice) > 0:
			clear_screen()
			header()
			amount = range(1, int(choice) + 1)
			for i in amount:
				result = ring_r()
				print(result)
			cont()
		else:
			fail()
		clear_screen()
		header()
		menu_2()
	elif choice == "7":
		choice = input("\nHow many would you like to roll? > ")
		check = int_check(choice)
		if check == True and int(choice) > 0:
			clear_screen()
			header()
			amount = range(1, int(choice) + 1)
			for i in amount:
				result = rsw_r()
				print(result)
			cont()
		else:
			fail()
		clear_screen()
		header()
		menu_2()
	elif choice == "8":
		menu_2()
	elif choice == "9":
		choice = input("\nHow many would you like to roll? > ")
		check = int_check(choice)
		if check == True and int(choice) > 0:
			clear_screen()
			header()
			amount = range(1, int(choice) + 1)
			for i in amount:
				result = ioun_r(100)
				print("Ioun Stone - " + result)
			cont()
		else:
			fail()
		clear_screen()
		header()
		menu_2()
	elif choice == "0":
		menu_1()
	else:
		fail()
		menu_2()

def gem_r():							#Gem Roller
	roll = randint(1, 100)
	for l in gem_l:
		if roll in l[0]:
			gold = dice(l[1]) * l[1][3]
			gem_type = l[2] + " - " + l[randint(4, len(l)) - 1]
			result = gem_type + " - " + str(gold) + "gp"
			return result, gold

def jewellery_r():						#Jewellery Roller
	roll = randint(1, 100)
	for l in jewellery_l:
		if roll in l[0]:
			gem_value = l[randint(3, 12) - 1]
			gold = dice(jewellery_dl[gem_value]) * jewellery_dl[gem_value][3]
			mats = jewellery_ml[gem_value] + " - " + l[1]
			result = mats + " - " + str(gold) + "gp"
			return result, gold

def g_j_r(g_j_str):						#Loop & Output for Gems & Jewellery
	clear_screen()
	header()
	choice = input("How " + g_j_str[1] + " would you like to roll? > ")
	print("\n")
	check = int_check(choice)
	if check == True:
		amount = int(choice)
		total_gold = 0
		while amount >= 1:
			amount = amount - 1
			result, gold = g_j_str[0]()
			total_gold = total_gold + gold
			print(result)
		print("\nYour total funds are " + str(total_gold) + "gp")
		cont()
		menu_1()
	else:
		fail()
		menu_1()

def asmp_r():							#Armour / Swords / Misc Properties
	roll_1 = randint(1, 20)
	roll_2 = randint(1, 100)
	for i in asmp_l:
		if roll_1 in i[0]:
			if roll_2 in i[1]:
				properties = i[2]
			else:
				properties = i[3]
	return properties

def asf_r():							#Armour & Shields
	roll_1 = randint(1, 20)
	roll_2 = randint(1, 100)
	for i in asf_l:
		if roll_1 in i[0]:
			if roll_2 in i[1]:
				form = i[2]
			else:
				form = i[3]
	properties = asmp_r()
	result = properties + form
	return result

def mwf_r():							#Misc Weapons
	roll_1 = randint(1, 20)
	roll_2 = randint(1, 100)
	for i in mwf_l:
		if roll_1 in i[0]:
			if roll_2 in i[1]:
				form = i[2]
			else:
				form = i[3]
		if roll_1 == 20:
			roll_3 = randint(1, 3)
			if roll_3 == 1:
				form = "Military Pick"
			elif roll_3 == 2:
				form = "Morning Star"
			elif roll_3 == 3:
				form = "Pole Arm"
	properties = asmp_r()
	result = properties + form
	return result

def sf_r():								#Swords
	roll_1 = randint(1, 20)
	roll_2 = randint(1, 100)
	for i in sf_l:
		if roll_1 in i[0]:
			if roll_2 in i[1]:
				form = i[2]
			else:
				form = i[3]
	properties = asmp_r()
	result = properties + form
	return result

def pot_r():							#Potions
	roll_1 = randint(0, 19)
	roll_2 = randint(1, 100)
	if roll_2 in pot_l[roll_1][0]:
		result = "Potion - " + pot_l[roll_1][1]
	else:
		result = "Potion - " + pot_l[roll_1][2]
	return result

def ring_r():							#Rings
	roll_1 = randint(0, 19)
	roll_2 = randint(1, 100)
	if roll_1 in range(0, 15):
		if roll_2 in ring_l[roll_1][0]:
			result = ring_l[roll_1][1]
		else:
			result = ring_l[roll_1][2]
	else:
		roll_3 = randint(1, 100)
		if roll_3 in range(1, 69):
			result = "Protection (+1)"
		elif roll_3 in range(69, 71):
			result = "Protection (+1, 5ft)"
		elif roll_3 in range(71, 93):
			result = "Protection (+2)"
		elif roll_3 in range(93, 94):
			result = "Protection (+2, 5ft)"
		elif roll_3 in range(94, 98):
			result = "Protection (+3)"
		elif roll_3 in range(98, 99):
			result = "Protection (+3, 5ft)"
		elif roll_3 in range(99, 100):
			result = "Protection (+4, +1 saves)"
		elif roll_3 in range(100, 101):
			result = "Protection (+5, +1 saves)"
	result = "Ring of " + result
	return result

def st_r():								#Scrolls
	roll_1 = randint(1, 20)
	roll_2 = randint(1, 20)
	if roll_1 in range(1, 13):
		for i in st2_l:
			if roll_2 in i[0]:
				result = i[1] + " Scroll"
	elif roll_1 in range(13, 20):
		for i in st3_l:
			if roll_2 in i[0]:
				result = "Scroll of protection from " + i[1]
	elif roll_1 in range(20, 21):
		result = "*Cursed* Scroll"
	return result

def rsw_r():							#Rods, Staves & Wands
	roll_1 = randint(1, 20)
	if roll_1 in range(1, 20):
		roll_2 = randint(1, 100)
		for i in rsw_l:
			if roll_1 in i[0]:
				if roll_2 in i[1]:
					result = i[2]
				else:
					result = i[3]
	elif roll_1 in range(20, 21):
		roll_3 = randint(1, 4)
		if roll_3 in range(1, 2):
			result = "Rod of Captivation"
		elif roll_3 in range(2, 4):
			result = "Rod of Lordly Might"
		elif roll_3 in range(4, 5):
			result = "Rod of Resurection"
	return result

def ioun_r(max_roll):					#Ioun Stones
	roll_1 = randint(1, max_roll)
	if roll_1 in range(1, 97):
		for i in ioun_l:
			if roll_1 in i[0]:
				result = i[1]
	elif roll_1 in range(97, 100):
		result_1 = ioun_r(96)
		result_2 = ioun_r(96)
		result = result_1 + ", " + result_2
	elif roll_1 in range(100, 101):
		result_1 = ioun_r(96)
		result_2 = ioun_r(96)
		result_3 = ioun_r(96)
		result = result_1 + ", " + result_2 + ", " + result_3
	return result

def ccmit_r(max_roll):
	roll_1 = randint(1, max_roll)
	for i in cmmit_l:
		if roll_1 in i[0]:
			result = i[1]
	if roll_1 == 1:
		roll_2 = randint(2, 5)
		result = str(roll_2) + " Incense of Meditation"
	elif roll_1 == 11:
		suffix = " of Pryaer Beads"
		roll_2 = randint(1, 6)
		if roll_2 in range(1, 5):
			prefix = "Strand"
		elif roll_2 == 5:
			prefix = "Lesser Strand"
		elif roll_2 == 6:
			prefix = "Greater Strand"
		result = prefix + suffix
	elif roll_1 in range(20, 22):
		suffix = " Horn of Valhalla"
		roll_2 = randint(1, 4)
		if roll_2 == 1:
			prefix = "Silver"
		elif roll_2 == 2:
			prefix = "Brass"
		elif roll_2 == 3:
			prefix = "Bronze"
		elif roll_2 == 4:
			prefix = "Iron"
		result = prefix + suffix
	elif roll_1 in range(56, 66):
		suffix = " Feather Token"
		roll_2 = randint(1, 6)
		if roll_2 == 1:
			prefix = "Anchor"
		elif roll_2 == 2:
			prefix = "Bird"
		elif roll_2 == 3:
			prefix = "Fan"
		elif roll_2 == 4:
			prefix = "Swan Boat"
		elif roll_2 == 5:
			prefix = "Tree"
		elif roll_2 == 6:
			prefix = "Whip"
		result = prefix + suffix
	elif roll_1 in range(66, 76):
		suffix = " Figurine of Wonderous Power"
		roll_2 = randint(1, 9)
		if roll_2 == 1:
			prefix = "Bronze Griffon"
		elif roll_2 == 2:
			prefix = "Ebony Fly"
		elif roll_2 == 3:
			prefix = "Golden Lion"
		elif roll_2 == 4:
			prefix = "Ivory Goats"
		elif roll_2 == 5:
			prefix = "Marble Elephant"
		elif roll_2 == 6:
			prefix = "Obsidian Steed"
		elif roll_2 == 7:
			prefix = "Onyx Dog"
		elif roll_2 == 8:
			prefix = "Serpentine Owl"
		elif roll_2 == 9:
			prefix = "Silver Raven"
		result = prefix + suffix
	elif roll_1 in range(76, 101):
		suffix = " Bracers of Armour"
		roll_2 = randint(1, 100)
		if roll_2 in range(1, 36):
			prefix = "+1"
		elif roll_2 in range(36, 61):
			prefix = "+2"
		elif roll_2 in range(61, 76):
			prefix = "+3"
		elif roll_2 in range(76, 86):
			prefix = "+4"
		elif roll_2 in range(86, 92):
			prefix = "+5"
		elif roll_2 in range(92, 97):
			prefix = "+6"
		elif roll_2 in range(97, 100):
			prefix = "+7"
		elif roll_2 == 100:
			prefix = "+8"
		result = prefix + suffix
	return result



# Gems

#Gem argument list for roller
gem_str = [gem_r, "many Gems"]

#List of gem types [chance_on_d100, [value_dice_list], gem_display_names]
gem_l = [[range(1, 31), [1, 4, 4, 1], "Ornamental Stone",
    "Banded Agate", "Eye Agate","Moss Agate", "Azurite", "Blue Quartz",
    "Hematite", "Lapis Lazuli", "Malachite", "Obsidian", "Rhodochrosite",
    "Tiger Eye", "Turquoise", "Freshwater Pearl"],
    [range(31, 56), [1, 4, 2, 10], "Semi-precious", "Bloodstone",
    "Carnelian", "Chalcedony", "Chrysoprase", "Citrine", "Iolite", "Jasper",
    "Moonstone", "Onyx", "Peridot", "Clear Quartz", "Sard", "Sardonyx",
    "Rose Quartz", "Smokey Quartz", "Star Rose Quartz", "Zircon"],
    [range(56, 76), [1, 4, 4, 10], "Fancy", "Amber", "Amethyst",
    "Chrysoberyl", "Coral", "Red Garnet", "Brown-Green Garnet", "Jade", "Jet",
    "White Pearl", "Golden Pearl", "Pink Pearl", "Silver Pearl", "Red Spinel",
    "Red-Brown Spinel", "Deep Green Spinel", "Tourmaline"],
    [range(76, 91), [1, 4, 2, 100], "Precious", "Alexandrite",
    "Aquamarine", "Violet Garnet", "Black Pearl", "Deep Blue Spinel",
    "Golden Yellow Topaz"],
    [range(91, 100), [1, 4, 4, 100], "Gem", "Emerald", "White Opal",
    "Black Opal", "Fire Opal", "Blue Sapphire", "Fiery Yellow Corundum",
    "Rich Purple Corundum", "Blue Star Sapphire", "Black Star Sapphire",
    "Star Ruby"],
    [range(100, 101), [1, 4, 2, 1000], "Jewel", "Clearest Bright Green Emerald",
    "Blue-White Diamond", "Canary Diamond", "Pink Diamond", "Brown Diamond",
    "Blue Diamond", "Jacinth"]]


#Jewellery

#jeweller argument list for roller
jewellery_str = [jewellery_r , "much Jewellery"]

#List of jewellery value dice [min_sides, max_sides, number_of_dice, multiplyer]
jewellery_dl = [[1, 10, 1, 100], [1, 6, 2, 100], [1, 6, 3, 100],
    [1, 6, 5, 100], [1, 4, 2, 1000], [1, 6, 2, 1000]]

#List of Jewellery description matterial
jewellery_ml = ["Silver", "Silver & Gold", "Gold",
	"Silver & Gems", "Gold & Gems", "Exceptional"]

#Type of jewellery list
#[chance_on_d100, name, 10_*_value_probability(dl_&_ml_list_position)]
jewellery_l = [[range(1, 4), "Amulet", 0, 0, 0, 0, 1, 1, 1, 2, 2, 3],
    [range(4, 5), "Anklet", 0, 0, 0, 1, 1, 1, 2, 2, 3, 4],
    [range(5, 8), "Arm-ring", 0, 0, 0, 0, 1, 1, 2, 2, 3, 4],
    [range(8, 11), "Belt", 0, 0, 0, 0, 1, 1, 2, 2, 3, 3],
    [range(11, 13), "Box", 0, 0, 0, 0, 1, 1, 1, 2, 2, 3],
    [range(13, 18), "Bracelet", 0, 0, 0, 1, 1, 1, 2, 2, 3, 4],
    [range(18, 21), "Broach", 0, 0, 0, 1, 1, 1, 2, 2, 3, 4],
    [range(21, 24), "Buckle", 0, 0, 0, 0, 1, 1, 1, 2, 2, 3],
    [range(24, 26), "Chain", 0, 0, 0, 0, 1, 1, 1, 2, 2, 3],
    [range(26, 28), "Chalice", 0, 0, 0, 1, 1, 1, 2, 2, 3, 4],
    [range(28, 31), "Chocker", 0, 0, 0, 0, 1, 1, 1, 2, 2, 3],
    [range(31, 33), "Clasp", 0, 0, 0, 0, 1, 1, 2, 2, 3, 3],
    [range(33, 36), "Comb", 0, 0, 0, 1, 1, 1, 2, 2, 3, 4],
    [range(36, 38), "Coronet", 0, 1, 2, 2, 3, 3, 3, 3, 4, 5],
    [range(38, 39), "Crown", 0, 1, 2, 3, 4, 4, 4, 5, 5, 5],
    [range(39, 41), "Diadem", 0, 0, 0, 1, 1, 1, 2, 2, 3, 4],
    [range(41, 47), "Earring", 0, 0, 0, 1, 1, 1, 2, 2, 3, 4],
    [range(47, 50), "Goblet", 0, 0, 0, 1, 1, 1, 2, 2, 3, 4],
    [range(50, 52), "Idol", 0, 0, 1, 1, 2, 2, 2, 3, 3, 4],
    [range(52, 55), "Knife", 0, 0, 0, 0, 1, 1, 1, 2, 2, 3],
    [range(55, 59), "Locket", 0, 0, 0, 1, 1, 2, 2, 3, 3, 4],
    [range(59, 61), "Medal", 0, 0, 0, 0, 1, 1, 1, 2, 2, 2],
    [range(61, 65), "Medallion", 0, 0, 0, 1, 1, 1, 2, 2, 2, 3],
    [range(65, 70), "Necklace", 0, 0, 0, 1, 1, 1, 2, 2, 3, 4],
    [range(70, 74), "Pendant", 0, 0, 0, 1, 1, 1, 2, 2, 3, 4],
    [range(74, 78), "Pin", 0, 0, 0, 1, 1, 1, 2, 2, 3, 4],
    [range(78, 79), "Orb", 0, 1, 2, 3, 3, 4, 4, 4, 5, 5],
    [range(79, 88), "Ring", 0, 0, 0, 1, 1, 1, 2, 2, 3, 4],
    [range(88, 89), "Sceptre", 0, 1, 2, 3, 3, 4, 4, 4, 5, 5],
    [range(89, 93), "Seal", 0, 0, 0, 0, 1, 1, 1, 2, 2, 3],
    [range(93, 95), "Statuette", 0, 0, 0, 1, 1, 1, 2, 2, 3, 4],
    [range(95, 96), "Tiara", 0, 0, 0, 1, 1, 1, 2, 2, 3, 4],
    [range(96, 98), "Toe-ring", 0, 0, 0, 1, 1, 1, 2, 2, 3, 4],
    [range(98, 101), "Weapon-hilt", 0, 0, 0, 1, 1, 1, 2, 2, 3, 4]]


#Magic items

#Master Magic Item Table d20 mmit
mmit_l = [[range(1,4), "Armour and Shields"],
    [range(4, 7), "Miscellaneous Magic"],
    [range(7, 10), "Miscellaneous Weapons"],
    [range(10, 14), "Potions"],
    [range(14, 15), "Rings"],
    [range(15, 16), "Rods, Staves and Wands"],
    [range(16, 19), "Scrolls"],
    [range(19, 21), "Swords"]]

#Armour & Shileds / Swords / Misc Weapons Properties d20 asmp
asmp_l = [[range(1, 11), range(1, 101), "+1 "],
    [range(11, 16), range(1, 101), "+2 "],
    [range(16, 17), range(1, 101), "+3 "],
    [range(17, 18), range(1, 66), "+4 ", "+5 ", "65/35"],
    [range(18, 19), range(1, 101), "*Cursed* "],
    [range(19, 21), range(1, 101), "Special "]]

#Armour & Shileds Forms d20 asf
asf_l = [[range(1, 2), range(1, 101), "Banded"],
    [range(2, 5), range(1, 91), "Chain Mail", "Elven Chain Mail", "9/1"],
    [range(5, 7), range(1, 101), "Leather"],
    [range(7, 10), range(1, 101), "Plate Mail"],
    [range(10, 11), range(1, 101), "Ring Mail"],
    [range(11, 13), range(1, 101), "Splinted"],
    [range(13, 15), range(1, 101), "Scale Mail"],
    [range(15, 16), range(1, 101), "Studded Leather"],
    [range(16, 21), range(1, 101), "Shield"]]

#Misc Weapon Forms d20 mwf
mwf_l = [[range(1, 4), range(1, 101), "Arrow"],
    [range(4, 6), range(1, 101), "Axe"],
    [range(6, 7),  range(1, 101), "Bolt"],
    [range(7, 8), range(1, 51), "Bow", "Crossbow", "50/50"],
    [range(8, 12), range(1, 101), "Dagger"],
    [range(12, 13), range(1, 101), "Flail"],
    [range(13, 14), range(1, 101), "Hammer"],
    [range(14, 15), range(1, 101), "Javelin"],
    [range(15, 17), range(1, 101), "Mace"],
    [range(17, 18), range(1, 51), "Trident", "Sling", "50/50"],
    [range(18, 19), range(1, 101), "Scimitar"],
    [range(19, 20), range(1, 101), "Spear"]]
    #[range(20, 21),  range(1, 101), "Military Pick", "Morning Star", "Pole Arm", "33/33/33"]]

#Sword Forms d20 sf
sf_l = [[range(1, 2), range(1, 81), "Bastard Sword", "Two Handed Sword", "80/20"],
    [range(2, 6), range(1, 101), "Broadsword"],
    [range(6, 20), range(1, 101), "Longsword"],
    [range(20, 21), range(1, 81), "Shortsword", "Scimitar", "80/20"]]

#Potions d20 pot_list
pot_l = [[range(1, 51), "Animal Control", "Clairaudience", "50/50"],
    [range(1, 51), "Clairvoyance", "Climbing", "50/50"],
    [range(1, 51), "Cursed", "Delusion", "50/50"],
    [range(1, 66), "Diminuation", "Dragon Control", "65/35"],
    [range(1, 101), "ESP"],
    [range(1, 36), "Extra Healing", "Fire Resistance", "35/65"],
    [range(1, 51), "Flying", "Gaseous Form", "50/50"],
    [range(1, 51), "Giant Control", "Giant Strength", "50/50"],
    [range(1, 101), "Growth"],
    [range(1, 101), "Healing"],
    [range(1, 51), "Heroism", "Human Control", "50/50"],
    [range(1, 51), "Invisibility", "Invulnerability", "50/50"],
    [range(1, 51), "Levitation", "Longevity", "50/50"],
    [range(1, 51), "Oil of Ætherealness", "Oil of Slipperiness", "50/50"],
    [range(1, 51), "Philtre of Love", "Plitre of Persuasiveness", "50/50"],
    [range(1, 66), "Plant Control", "Polymorph", "65/35"],
    [range(1, 51), "Speed", "Super-Heroism", "50/50"],
    [range(1, 101), "Sweet Water"],
    [range(1, 76), "Treasure Finding", "Undead Control", "75/25"],
    [range(1, 101), "Water Breathing"]]

#Rings d20 ring_list
ring_l =[[range(1, 101), "Charisma"],
    [range(1, 101), "Feather Falling"],
    [range(1, 101), "Feather Falling"],
    [range(1, 101), "Fire Resistance"],
    [range(1, 101), "Free Action"],
    [range(1, 101), "Genie Summoning"],
    [range(1, 101), "Invisibility"],
    [range(1, 26), "Regeneration", "Spell Storing", "25/75"],
    [range(1, 101), "Spell Turning"],
    [range(1, 101), "Swimming"],
    [range(1, 51), "Telekinesis", "Three Wishes", "50/50"],
    [range(1, 101), "Warmth"],
    [range(1, 101), "Water Walking"],
    [range(1, 101), "Water Walking"],
    [range(1, 101), "Wizardry"]]
    #[range(1, 101), "Protection"], 01-68 - +1, 69-70 - +1 5ft
    #[range(1, 101), "Protection"], 71-92 - +2, 93 - +2 5ft
    #[range(1, 101), "Protection"], 94-97 - +3, 98 - +3 5ft
    #[range(1, 101), "Protection"], 99 - +4 +1 saving throws
    #[range(1, 101), "Protection"], 00 - +5 +1 saving throws

#Scrolls Table 1 d20 type st1
st1_l = [[range(1, 13), "Spell"],
    [range(13, 20), "Protection"],
    [range(20, 21), "Cursed"]]

#Scrolls Table 2 d20 - Spells st2
st2_l = [[range(1, 4), "Cleric"],
    [range(4, 6), "Druid"],
    [range(6, 8), "Illusionist"],
    [range(8, 21), "Magic User"]]

#Scrolls Table 3 d20 - Warding st3
st3_l = [[range(1, 3), "Acid"],
    [range(3, 5), "Demons"],
    [range(5, 7), "Devils"],
    [range(7, 10), "Elementals"],
    [range(10, 12), "Lycanthropes"],
    [range(12, 15), "Magic"],
    [range(15, 17), "Petrification"],
    [range(17, 19), "Polymorph"],
    [range(19, 21), "Undead"]]

#Misc Magic Items Master Table d100 mmimt
mmimt_l = [[range(1, 51), "Common"],
    [range(51, 71), "Less Common"],
    [range(71, 91), "Uncommon"],
    [range(91, 100), "Rare"],
    [range(100, 101), "Roll Twice, ignoring this result"]]

#Common Misc Magic Items Table d100 ccmit
cmmit_l = [#[range(1, 2), "Incense of Meditation (d4+1 cones)", "1d4+1 cones"],
    [range(2, 3), "Javelin of the Raptor"],
    [range(3, 4), "Thunder Spear"],
    [range(4, 5), "Boots of Elvenkind"],
    [range(5, 6), "Candle of Invocation"],
    [range(6, 7), "Dust of Apperance"],
    [range(7, 8), "Dust of Disapperance"],
    [range(8, 9), "Rope of Climbing"],
    [range(9, 10), "Scarab of Protection"],
    [range(10, 11), "Slippers of Spider Climbing"],
    #[range(11, 12), "Strand of Prayer Beads (d6 for strand type)", "d6 1-4=Strand, 5=Lesser, 6=Greater"],
    [range(12, 14), "Amulet of Natural Armour"],
    [range(14, 16), "Blessed Book"],
    [range(16, 18), "Broach of Shielding"],
    [range(18, 20), "Hat of Disguise"],
    #[range(20, 22), "Horn of Valhalla (d4 for type)", "d4 1=Silver, 2=Brass, 3=Bronze, 4=Iron"],
    [range(22, 24), "Periapt of Proof Against Poison"],
    [range(24, 26), "Phylactery of Faithfulness"],
    [range(26, 28), "Robe of Blending"],
    [range(28, 31), "Pipes of the Sewers"],
    [range(31, 34), "Restorative Ointment"],
    [range(34, 37), "Robe of Usefull Items"],
    [range(37, 40), "Vest of Escape"],
    [range(40, 43), "Cloak of Elvenkind"],
    [range(43, 47), "Wings of Flying"],
    [range(47, 56), "Cloak of Resistance"]]
    #[range(56, 66), "Feather Token (d6 for type)", "d6 1=Anchor,2=Bird,3=Fan,4=Swan Boat,5=Tree,6=Whip"],
    #[range(66, 76), "Figurine of Wonderous Power (d10 for type)", "d9 1=Bronze Griffon, 2=Ebony Fly, 3=Golden Lion, 4=Ivory Goats, 5=Marble Elephant, 6=Obsidian Steed, 7=Onyx Dog, 8=Serpentine Owl, 9=Silver Raven"],
    #[range(76, 101), "Bracers of Armour (d100 for type)", "d100, 1-35+1, 36-60+2, 61-75+3, 76-85+4, 86-91+5, 92-96+6, 97-99+7, 100+8"]]

#Less Common Misc Magic Items Table d100 lcmmit
lcmmit_l = [[range(1, 2), "Arrow of Direction"],
    [range(2, 3), "Brazier of Commanding Fire Elementals"],
    [range(3, 4), "Cape of the Mountebank"],
    [range(4, 5), "Cloak of the Manta Ray"],
    [range(5, 6), "Decanter of Endless Water"],
    [range(6, 7), "Dust of Dryness"],
    [range(7, 8), "Elixir of Swimming"],
    [range(8, 9), "Gloves of Arrow Snaring"],
    [range(9, 10), "Gloves of Swimming & Climbing"],
    [range(10, 11), "Goggles of Night"],
    [range(11, 12), "Horseshoes of Speed"],
    [range(12, 13), "Necklace of Adaptation"],
    [range(13, 14), "Orb of Storms"],
    [range(14, 15), "Periapt of Health"],
    [range(15, 16), "Pipes of Haunting"],
    [range(16, 17), "Ring Gates"],
    [range(17, 18), "Robe of Bones"],
    [range(18, 19), "Ungent of Timelessness"],
    [range(19, 21), "Universal Solvent"],
    [range(21, 23), "Amulet of Proof Against Detection or Location"],
    [range(23, 25), "Boots of Speed"],
    [range(25, 27), "Boots of Striding & Springing"],
    [range(27, 29), "Bracers of Archery (Lesser)"],
    [range(29, 31), "Candle of Truth"],
    [range(31, 33), "Cloak of Displacement (Minor)"],
    [range(33, 35), "Cloak of the Bat"],
    [range(35, 37), "Dark Skull"],
    [range(37, 39), "Dust of Tracelessness"],
    [range(39, 41), "Elixir of Truth"],
    [range(41, 43), "Elixir of Vision"],
    [range(43, 45), "Gloves of Storing"],
    [range(45, 47), "Horn of Tritons"],
    [range(47, 49), "Necklace of Fireballs (d8 for type)", "1d8 = level, 8 reroll 2x 8 roll a new item"],
    [range(49, 51), "Periapt of Wound Closure"],
    [range(51, 53), "Phylactery of Undead Turning"],
    [range(53, 55), "Rope of Entaglement"],
    [range(55, 57), "Stone Horse"],
    [range(57, 59), "Stone of Alarm"],
    [range(59, 61), "Sustaining Spoon"],
    [range(61, 63), "Wind Fan"],
    [range(63, 66), "Bag of Holding (d4 type)", "d4 1=type1, 2=type2. 3=type3, 4=type4"],
    [range(66, 69), "Boots of Levitation"],
    [range(69, 72), "Bottle of Air"],
    [range(72, 75), "Broom of Flying"],
    [range(75, 78), "Crystal Ball"],
    [range(78, 81), "Elixir of Fire Breath"],
    [range(81, 84), "Elixir of Hiding"],
    [range(84, 87), "Handy Haversack"],
    [range(87, 90), "Harp of Charming"],
    [range(90, 93), "Helm of Comprehend Languages & Read Magic"],
    [range(93, 96), "Helm of Underwater Action"],
    [range(96, 99), "Horn of Fog"]]
    #[range(99, 100), "Roll Twice on table 1", "ccmimt"],
    #[range(100, 101), "Roll twice on table 2 (ignore results over 98)", "lccmit 98"]]

# Uncommon Misc Magic Items Table d100 ummit
ummit_l = [[range(1, 2), "Ahmek's Copious Coin Purse"],
    [range(2, 3), "Alchemy Jug"],
    [range(3, 4), "Amulet of Health"],
    [range(4, 5), "Amulet of the Planes"],
    [range(5, 6), "Apparatus of the Lobster"],
    [range(6, 7), "Stone Salve"],
    [range(7, 8), "Bead of Force"],
    [range(8, 9), "Blemish Blotter"],
    [range(9, 10), "Boots of the Winterlands"],
    [range(10, 11), "Bowl of Commanding Water Elementals"],
    [range(11, 12), "Bracelet of Friends"],
    [range(12, 13), "Bracers of Archery (Greater)"],
    [range(13, 14), "Stone of Good Luck"],
    [range(14, 15), "Censer of Controlling Air Elementals"],
    [range(15, 16), "Chime of Interruption"],
    [range(16, 17), "Chime of Opening"],
    [range(17, 18), "Circlet of Blasting (Minor)"],
    [range(18, 19), "Circlet of Persuasion"],
    [range(19, 20), "Cloak of Ætherealness"],
    [range(20, 21), "Cloak of Arachnida"],
    [range(21, 22), "Cloak of Charisma"],
    [range(22, 23), "Cloak of Displacement (Major)"],
    [range(23, 24), "Cube of Force"],
    [range(24, 25), "Cube of Frost Resistance"],
    [range(25, 26), "Cubic Gate"],
    [range(26, 27), "Deck of Illusion"],
    [range(27, 28), "Dimensional Shackles"],
    [range(28, 29), "Drums of Panic"],
    [range(29, 30), "Dust of Illusion"],
    [range(30, 31), "Efficient Quiver"],
    [range(31, 32), "Vestment, Druid’s"],
    [range(32, 33), "Eyes of the Eagle"],
    [range(33, 34), "Gauntlets of Ogre Power"],
    [range(34, 35), "Gauntlets of Rust"],
    [range(35, 36), "Gloves of Dexterity"],
    [range(36, 37), "Goggles of Minute Seeing"],
    [range(37, 38), "Headband of Intellect"],
    [range(38, 39), "Helm of Telepathy"],
    [range(39, 40), "Horn of Goodness/Evil"],
    [range(40, 41), "Horseshoes of the Zephyr"],
    [range(41, 42), "Instant Fortress"],
    [range(42, 43), "Iron Bands of Binding"],
    [range(43, 44), "Iron Flask"],
    [range(44, 45), "Lantern of Revealing"],
    [range(45, 46), "Mantle of Faith"],
    [range(46, 47), "Mantle of Magic Resistance"],
    [range(47, 48), "Well of Many Worlds"],
    [range(48, 49), "Mask of the Skull"],
    [range(49, 50), "Medallion of Thoughts"],
    [range(50, 51), "Pearl of Power"],
    [range(51, 52), "Pearl of the Sirines"],
    [range(52, 53), "Periapt of Wisdom"],
    [range(53, 54), "Pipes of Pain"],
    [range(54, 55), "Pipes of Sounding"],
    [range(55, 56), "Plentiful Vessel"],
    [range(56, 57), "Robe of Stars"],
    [range(57, 58), "Scabbard of Keen Edges"],
    [range(58, 59), "Scarab of Golem Bane"],
    [range(59, 60), "Silversheen"],
    [range(60, 61), "Sovereign Glue"],
    [range(61, 62), "Stone of Controlling Earth Elementals"]]
    #[range(62, 63), "Carpet of Flying (d6 type)", "d6 1/2=5x5, 3/4=5x10, 5/6=10x10"],
    #[range(63, 64), "Bag of Tricks", "(d6 type)", "d6 1/2=Grey, 34/Rust, 5/6=Tan"",]"]
    #[range(64, 65), "Elemental Gem", "d4 1=Clear 2=Brown 3=BrightRed 4=Turquoise"],
    #[range(65, 66), "Marvellous Pigments", "(1d4 pots)"]
    #[range(66, 76), "Roll Twice on Table I"],
    #[range(76, 86), "Roll Once on Table I & Once on Table II", "cmmit & lcmmit"],
    #[range(86, 96), "Roll Twice on Table II", "lcmmit * 2"],
    #[range(96, 100), "Reroll & Ignore Results > 65, Roll Once on Table II", "ummit<65 & lcmmit"],
    #[range(100, 101), "Roll Twice, Ignore Results > 65", "ummit<65 * 2"]]

#Rare Misc Magic Items Table d100 rmmit errors on table (4 and 13)
rmmit_l = [[range(1, 3), "Afreeti Bottle"],
    [range(3, 5), "Amulet of Life Protection"],
    [range(5, 7), "Amulet of Mighty Fists"],
    [range(7, 9), "Belt of Dwarfkind"],
    [range(9, 11), "Belt of Giant Strength"],
    [range(11, 13), "Boat Folding"],
    [range(13, 15), "Boots of Teleportation"],
    [range(15, 17), "Boots, Winged"],
    [range(17, 19), "Brooch of Instigation"],
    [range(19, 21), "Circlet of Blasting (Major)"],
    [range(21, 23), "Eversmoking Bottle"],
    [range(23, 25), "Eyes of Charming"],
    [range(25, 27), "Eyes of Doom"],
    [range(27, 29), "Eyes of Petrifaction"],
    [range(29, 31), "Gem of Brightness"],
    [range(31, 33), "Gem of Seeing"],
    [range(33, 35), "Golem Manual"],
    [range(35, 37), "Helm of Brilliance"],
    [range(37, 39), "Helm of Teleportation"],
    [range(39, 41), "Horn of Blasting"],
    [range(41, 43), "Horn of Blasting (Greater)"],
    [range(43, 45), "Tome of Understanding"],
    [range(45, 47), "Lyre of Building"],
    [range(47, 49), "Manual of Bodily Health"],
    [range(49, 51), "Manual of Gainful Exercise"],
    [range(51, 53), "Manual of Quickness of Action"],
    [range(53, 55), "Mattock of the Titans"],
    [range(55, 57), "Maul of the Titans"],
    [range(57, 59), "Mirror of Life Trapping"],
    [range(59, 61), "Mirror of Mental Prowess"],
    [range(61, 63), "Mirror of Opposition"],
    [range(63, 65), "Oil of Famishing"],
    [range(65, 67), "Portable Hole"],
    [range(67, 69), "Robe of Eyes"],
    [range(69, 71), "Robe of Scintillating Colours"],
    [range(71, 73), "Robe of the Archmagi"],
    [range(73, 75), "Sagacious Volume"],
    [range(75, 77), "Shrouds of Disintegration"],
    [range(77, 79), "Tome of Clear Thought"],
    [range(79, 81), "Tome of Leadership and Influence"]]
    #[range(81, 83), "Ioun Stone (d100 type)", "ioun stone table"]]
	#[range(83, 88), "Roll twice on table 2", "lcmmit & lcmmit"]
    #[range(88, 92), "Roll Again & Roll Misc. Magic Weapon", "rmmit & misc_wep"],
    #[range(92, 96), "Roll Again & Roll Magic Sword", "rmmit & swords"],
    #[range(96, 101), "Roll On Cursed Items Table", "cursed + mmit"]]

#Rods Staves & Wands - No table exists rsw
rsw_l = [[range(1, 2), range(1, 101), "Rod of Absorption"],
	[range(2, 4), range(1, 101), "Rod of Cancellation"],
	[range(4, 5), range(1, 51), "Wand of Summoning", "Wand of Wonder", "50/50"],
	[range(5, 6), range(1, 51), "Rod of Rulership", "Rod of Striking", "50/50"],
	[range(6, 7), range(1, 51), "Staff of Compulsion", "Staff of Healing", "50/50"],
	[range(7, 8), range(1, 26), "Staff of Power", "Staff of the Serpent", "25/75"],
	[range(8, 9), range(1, 76), "Staff of Withering", "Staff of Wizardry", "75/25"],
	[range(9, 10), range(1, 101), "Wand of Detect Magic"],
	[range(10, 11), range(1, 101), "Wand of Detecting Minerals & Metals"],
	[range(11, 12), range(1, 101), "Wand of Detecting Traps & Secret Doors"],
	[range(12, 13), range(1, 101), "Wand of Enemy Detection"],
	[range(13, 14), range(1, 51), "Wand of Fear", "Wand of Fire", "50/50"],
	[range(14, 15), range(1, 51), "Wand of Ice", "Wand of Light", "50/50"],
	[range(15, 16), range(1, 51), "Wand of Illusion", "Wand of Lightning", "50/50"],
	[range(16, 17), range(1, 101), "Wand of Magic Missiles"],
	[range(17, 18), range(1, 101), "Wand of Negation"],
	[range(18, 19), range(1, 101), "Wand of Paralysation"],
	[range(19, 20), range(1, 101), "Wand of Polymorphong"]]
	#[range(20, 21), range(1, 101), "Rod of Captivation", "Rod of Lordly Might", "Rod of Resurection", "25/50/25"]]

#Ioun Stone Table d100 ioun_roller
ioun_l = [[range(1, 7), "Clear Spindle"],
    [range(7, 13), "Dusty Rose Prism"],
    [range(13, 19), "Deep Red Sphere"],
    [range(19, 25), "Incandescent Blue Sphere"],
    [range(25, 31), "Pale Blue Rhomboid"],
    [range(31, 37), "Pink Rhomboid"],
    [range(37, 43), "Pink & Green Sphere"],
    [range(43, 49), "Scarlet & Blue Sphere"],
    [range(49, 55), "Dark Blue Rhomboid"],
    [range(55, 61), "Vibrant Purple Prism"],
    [range(61, 67), "Iridescent Spindle"],
    [range(67, 73), "Pale Lavender Ellipsoid"],
    [range(73, 78), "Pearly White Spindle"],
    [range(78, 84), "Pale Green Prism"],
    [range(84, 90), "Orange Prism"],
    [range(90, 97), "Lavender & Green Ellipsoid"]]
    #[range(97, 100), "roll twice ignoring roll over 96"]
    #[range(100, 101), "Roll Thrice ignoring roll over 96"]


#To Do - cmmit & lccmit tables need re-organising

menu_1()

#for i in range(1, 11):
#	r = ccmit_r(100)
#	print(r)
