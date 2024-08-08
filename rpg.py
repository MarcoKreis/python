import random

# Player stats
player = {
    "name": "Hero",
    "hp": 100,
    "max_hp": 100,
    "attack": 10,
    "gold": 0
}

# Enemy data
enemies = [
    {"name": "Rat", "hp": 20, "attack": 5, "gold": 10},
    {"name": "Goblin", "hp": 30, "attack": 8, "gold": 20},
    {"name": "Orc", "hp": 50, "attack": 12, "gold": 30},
    {"name": "Dragon", "hp": 100, "attack": 20, "gold": 100}
]

# Functions to handle game mechanics
def display_stats():
    print(f"\n{player['name']}'s Stats:")
    print(f"Health: {player['hp']}/{player['max_hp']}")
    print(f"Attack: {player['attack']}")
    print(f"Gold: {player['gold']}\n")

def battle(enemy):
    print(f"A wild {enemy['name']} appears!")
    while enemy['hp'] > 0 and player['hp'] > 0:
        action = input("Do you want to (A)ttack or (R)un? ").strip().lower()
        if action == 'a':
            # Player attacks enemy
            damage = random.randint(1, player['attack'])
            enemy['hp'] -= damage
            print(f"You attack the {enemy['name']} for {damage} damage.")

            if enemy['hp'] <= 0:
                print(f"The {enemy['name']} has been defeated!")
                player['gold'] += enemy['gold']
                print(f"You gained {enemy['gold']} gold!")
                break

            # Enemy attacks player
            enemy_damage = random.randint(1, enemy['attack'])
            player['hp'] -= enemy_damage
            print(f"The {enemy['name']} attacks you for {enemy_damage} damage.")

            if player['hp'] <= 0:
                print("You have been defeated... Game Over!")
                quit()
        elif action == 'r':
            print("You run away safely!")
            break
        else:
            print("Invalid action. Please choose (A)ttack or (R)un.")

def visit_shop():
    print("\nWelcome to the shop!")
    print("1. Heal (10 Gold) - Restores 20 HP")
    print("2. Leave shop")
    choice = input("Choose an option: ").strip()
    
    if choice == '1':
        if player['gold'] >= 10:
            heal_amount = min(20, player['max_hp'] - player['hp'])
            player['hp'] += heal_amount
            player['gold'] -= 10
            print(f"You have been healed by {heal_amount} HP.")
        else:
            print("You don't have enough gold to heal.")
    elif choice == '2':
        print("You leave the shop.")
    else:
        print("Invalid choice. Please choose again.")

def random_encounter():
    enemy = random.choice(enemies)
    battle(enemy)

# Main game loop
def main():
    print("Welcome to the RPG Game!")
    
    while True:
        display_stats()
        print("1. Explore")
        print("2. Visit Shop")
        print("3. Quit")
        choice = input("What would you like to do? ").strip()

        if choice == '1':
            random_encounter()
        elif choice == '2':
            visit_shop()
        elif choice == '3':
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
