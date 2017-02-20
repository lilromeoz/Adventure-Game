import random
import time

ice_cream = False
wizard = False
staff = False
sword = False
armour = False
gold = 0
exp = 0

def intro():
	print("***************\n"
		"   Adventure\n"
		"     The\n"
		"       Game\n"
		"***************\n")
	town()
	time.sleep(4)
def town():
	time.sleep(2)
	print("***************")
	print("You're in Adventure Town!\n"
		"Things you can do: \n"
		"(S)hop\n"
		"(Explore)\n"
		"(C)heck for Jobs\n"
		"(E)valuate Status\n"
		"(S)lay Dragon\n\n"
		"***************")
	print("You have %d gold" % gold)
	print("You have %d experience" % exp)
	print("***************\n")

	do = raw_input("What do you want to do? \n")

	if do == "C":
		print("You look around town for jobs...")
		time.sleep(2)
		jobs()
	elif do == "shop":
		shop()
	elif do == "E":
		evaluate()
	elif do == "S":
		print("You travel to the Dragons Den")
		time.sleep(2)
		print("...")
		time.sleep(2)
		slay()
	elif do == "explore":
		print("You go exploring")
		time.sleep(2)
		print("...")
		time.sleep(2)
		explore()
	elif do == "quit":
		quit()
	else:
		town()

def shop():
	global sword, ice_cream, armour, gold, exp
	print("***************")
	print("Welcome to the towns shop")
	print("We currently have these items in stock: \n")
	print("1) Chainmail Armour - 80 gold \n"
		"2) Steel Swords - 30 gold \n"
		"3) Ice Cream - 15 gold \n")
	print("***************")

	do = raw_input("What would you like to buy? \n")

	if do == "quit":
		town()
	elif do == "1":
		if gold <80:
			print("You dont have enough gold, come back later...\n")
			time.sleep(3)
			town()
		elif gold >=80:
			print("You have bought the armour for 80 gold\n")
			price_s = 80
			price = 25
			armour = True
			gold -= price_s
			exp += price
			time.sleep(3)
			shop()
	elif do == "2":
		if gold <30:
			print("You dont have enough gold, come back later...\n")
			time.sleep(3)
			town()
		elif gold >=30:
			print("You have bought the sword for 30 gold\n")
			price_s = 30
			price = 15
			sword = True
			gold -= price_s
			exp += price
			time.sleep(3)
			shop()
	elif do == "3":
		if gold <15:
			print("You dont have enough gold, come back later...\n")
			time.sleep(3)
			town()
		elif gold >=15:
			print("You have bought the ice cream for 15 gold\n")
			price_s = 15
			price = 5
			ice_cream = True
			gold -= price_s
			exp += price
			time.sleep(3)
			shop()
	else:
		shop()


def jobs():
	print("***************\n")
	print("Job List: \n")
	print("1) Help plantation owner...\n")
	print("2) Destroy nearby Giants...\n")
	print("3) Help King with rebels...\n")
	print("4) Help find hybrid plant for King...\n")
	print("5) Talk to Hobo")
	print("***************")

	do = raw_input("What would you like to do? \n")

	if do == "quit":
		quit()
	elif do == "1":
		plantation()
	elif do == "2":
		goblin()
	elif do == "3":
		rebel()
	elif do == "4":
		hybrid()
	elif do == "5":
		cream()
	elif do == "dev":
		global sword, gold, armour, exp, ice_cream, wizard, staff
		price = 1000
		gold += price
		exp += price
		armour = True
		sword = True
		ice_cream = True
		staff = True
		wizard = True
		town()
	else:
		town()


def evaluate():
	if staff == True:
		print("*You have a staff")
	elif staff == False:
		print("*You do not have a staff")
	if ice_cream == False:
		print("*You dont have ice cream...")
	elif ice_cream == True:
		print("*You have ice cream...")
	if sword == False:
		print("*You dont have a sword. Fighting the Dragon now would end your life...")
	elif sword == True:
		print("*You have a sword. This will help you alot in your fight against the Dragon...")	
	if armour == False:
		print("*You dont have armour. The dragon will bite you up...")
	elif armour == True:
		print("*You have armour. This will help when the dragon pounces on you...")
	if exp < 100:
		print("*You dont have enough experience. This will be fatal in battle..\n")
	elif exp >= 100:
		print("*You have alot of experience. This will help you greatly in your battle...\n")
	time.sleep(5)
	town()


def slay():
	if sword == False:
		print("You try to attack the Dragon but without a sword, you die quickly...")
		time.sleep(3)
		print("...GAME OVER...")
		time.sleep(3)
		quit()

	if sword == True:
		print("You try and attack the dragon and slash it a bit...")
		time.sleep(3)
	if armour == False:
		print("The dragon swipes at your bare chest and you die...")
		time.sleep(3)
		print("...GAME OVER...")
		time.sleep(3)
		quit()

	if sword == True:
		print("You try and attack the dragon and slash it a bit...")
		time.sleep(3)
	if armour == True:
		print("The dragon tries to slash at you chest but with your armour, it has no affect on you...")
		time.sleep(3)
	if exp < 100:
		print("The dragon traps you into a corner put as he slashes at you, your lack of experience affected your reaction time that could of saved you... ")
		time.sleep(3)
		print("...GAME OVER...")
		time.sleep(3)
		quit()

	if sword == True:
		print("You try and attack the dragon and slash it a bit...")
		time.sleep(3)
	if armour == True:
		print("The dragon tries to slash at you chest but with your armour, it has no affect on you...")
		time.sleep(3)
	if exp >= 100:
		print("The dragon tries to catch you in a corner but your experience led you to find a way out and slay the dragon...")
		time.sleep(3)
		print("...YOU WIN...")
		time.sleep(3)
		credits()

def explore():
	print("You see a tower and go investigate...")
	time.sleep(2)
	do = raw_input("You can:\n"
		"1) Go into tower\n"
		"2) Go back to village\n")

	if do == "1":
		wizard == True
		if staff == False:
			time.sleep(2)
			print("A Dark Wizard suprises you and with his spells casts you into oblivian...\n")
			print("...GAME OVER...")
			quit()
		elif staff == True:
			time.sleep(3)
			print("With your staff and spell in hand you sneak into the tower and turn the mage into ash.\n")
			time.sleep(2)
			i = input("Would you like to:\n"
				"1) Continue\n"
				"2) Retire\n")
			if i == "1":
				town()
			elif i == "2":
				print("You have faught many things, but now its time to settle down...")
				time.sleep(2)
				credits()
	elif do == "2":
		town()


def plantation():
	global gold, exp
	print("You do back breaking work all day and it pays off...\n")
	reward_g = random.randint(10, 20)
	reward_e = random.randint(1, 5)
	print("You receive %d gold and %d experience...\n" % (reward_g, reward_e))
	gold += reward_g
	exp += reward_e
	time.sleep(2)
	town()
def goblin():
	global gold, exp
	if sword == False:
		death = random.randint(2,5)
		if death == 2:
			print("You die trying to kill the giants...\n")
			print("...GAME OVER...\n")
			quit()
		else:
			print("You defeat and kill the giants")
			reward_g = random.randint(15, 30)
			reward_e = random.randint(10, 20)
			print("You got %d gold and %d experience...\n" % (reward_g, reward_e))
			gold += reward_g
			exp += reward_e
			time.sleep(3)
			town()
	if sword == True:
		print("You defeat and kill the giants")
		reward_g = random.randint(15, 30)
		reward_e = random.randint(10, 20)
		print("You got %d gold and %d experience...\n" % (reward_g, reward_e))
		gold += reward_g
		exp += reward_e
		time.sleep(3)
		town()
def rebel():
	global gold, exp
	if sword == False:
		death = random.randint(2,5)
		if death == 2:
			print("You die trying to put down the rebels...\n")
			print("...GAME OVER...\n")
			quit()
		else:
			print("You defeat and turn in the rebels")
			reward_g = random.randint(20, 30)
			reward_e = random.randint(20, 30)
			print("You got %d gold and %d experience...\n" % (reward_g, reward_e))
			gold += reward_g
			exp += reward_e
			time.sleep(3)
			town()
	if sword == True:
		print("You defeat and turn in the rebels\n")
		reward_g = random.randint(20, 35)
		reward_e = random.randint(20, 38)
		print("You got %d gold and %d experience...\n" % (reward_g, reward_e))
		gold += reward_g
		exp += reward_e
		time.sleep(3)
		town()
def hybrid():
	global gold, exp
	print("You roam the forest gathering plants to graft...months pass...and your work...\n")
	time.sleep(4)
	no = random.randint(2, 5)
	if no == 2:
		print("does not pay off...")
		print("You get 0 gold and 0 experience for your failed mission...")
		town()
	else:
		print("PAYS OFF!")
		reward_g = random.randint(23, 40)
		reward_e = random.randint(15, 20)
		print("You receive %d gold and %d experience for your effort...\n" % (reward_g, reward_e))
		gold += reward_g
		exp += reward_e
		time.sleep(2)
		town()
def cream():
	print("The hobo comes and asks you for some food")
	it = raw_input("You can:\n"
		"1) Give Food\n"
		"2) Not Give Food\n")
	if it == "1":
		global ice_cream, wizard, staff
		print("You look around for food...\n")
		if ice_cream == False:
			print("You dont have any food...")
			town()
		elif ice_cream == True:
			staff = True
			wizard = True
			ice_cream = False
			print("You give him some ice cream.")
			print("He tells you about his time adventuring and how there is a Dark Wizard in the forest.")
			print("He gives you his mage staff which is the only thing that can defeat the wizard...")
			time.sleep(5)
			town()
	elif it == "2":
		print("You dont give the Hobo food...")
		time.sleep(3)
		town()

def credits():
	print("'Adventure The Game' Made by Jordan Moore")
	time.sleep(2)
	quit()
intro()

# Made By Jordan Moore 