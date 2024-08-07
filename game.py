#Text-Based-RPG in Python 07.08.2024

import random

global playerhp, playermaxhp, playerdmg, enemyhp, enemymaxhp, enemydmg
playerhp = 100
playermaxhp = 100
playerdmg = 20
enemyhp = 100
enemymaxhp = 100
enemydmg = 20

#random_integer = random.randint(dmg - 10, dmg + 10)
#print(random_integer)

def Attack():
	global enemyhp, enemymaxhp, enemydmg, playerdmg, playerhp, playermaxhp
	if enemyhp < 1:
		print("The enemy is already dead..............")
	else:
		print("You started attacking the enemy...")
		playerdmg_range = random.randint(playerdmg - 10, playerdmg + 10)
		enemyhp = enemyhp - playerdmg_range
		print("You did ",playerdmg_range, " damage to the enemy.")
		print("The Enemy has ", enemyhp, " HP left.")
		if enemyhp > 0:
			enemydmg_range = random.randint(enemydmg - 10, enemydmg + 10)
			playerhp = playerhp - enemydmg_range
			print("The enemy attacks you for ",enemydmg_range, " HP.")
			print("You have ", playerhp, " HP left.")
			if playerhp <= 0:
				print("You have no more HP. You faint.")
				input()

def CommitSuicide():
	global playerhp
	print("Live has lost all meaning...")
	print("You kill yourself for all your remaining HP.")
	playerhp = 0

print("Hello there, this is an RPG-Game! Press any button to start...")
input()
while playerhp > 0:
	print("Your HP: ",playerhp)
	print("Enemy HP: ",enemyhp)
	print("Select from the following options:")
	print("(1) Attack")
	print("(2) Commit suicide")
	selection = int(input())
	if selection == 1:
		Attack()
	elif selection == 2:
		CommitSuicide()

if playerhp <= 0:
	print("You have no more HP. You faint.")
	input()