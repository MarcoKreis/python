#Text-Based-RPG in Python 07.08.2024

global playerhp, playermaxhp, playerdmg, enemyhp, enemymaxhp, enemydmg
playerhp = 100
playermaxhp = 100
playerdmg = 20
enemyhp = 100
enemymaxhp = 100
enemydmg = 30

def Attack():
	print("You started attacking the enemy...")
	global enemyhp, enemymaxhp, enemydmg, playerdmg, playerhp, playermaxhp
	enemyhp = enemyhp - playerdmg
	print("You did ",playerdmg, " damage to the enemy.")
	print("The Enemy has ", enemyhp, " HP left.")
	if enemyhp > 0:
		playerhp = playerhp - enemydmg
		print("The enemy attacks you for ",enemydmg, " HP.")
		print("You have ", playerhp, " HP left.")
		if playerhp <= 0:
			print("You have no more HP. You faint.")
			input()


print("Hello there, this is an RPG-Game! Press any button to start...")
input()
while playerhp > 0:
	print("Your HP: ",playerhp)
	print("Enemy HP: ",enemyhp)
	print("Select from the following options:")
	print("(1) Attack")
	selection = int(input())
	print("You selected: ", selection)
	if selection == 1:
		Attack()