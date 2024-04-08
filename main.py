# Starting text that welcomes and explains game to player
print('Welcome!')

print('\nYou are on a camping trip with 3 of your friends in the middle of the forest and while sitting around a campfire,\n'
      'you feel as though something has been watching you all. You dismiss it and guess that it is just due to sleepiness.\n'
      'Everyone then decides to put out the fire and call it a night when suddenly an abnormally tall man with a creepily \n'
      'distorted face steps out of the shadows from behind a tree. He is covered from head to toe in blood and is holding an axe.\n'
      'One of your friends’ yells and asks the man “What do you want?”, He does not answer. The man all of a sudden starts running\n'
      'full speed towards you all. You and each of your friends start running away but the man is too fast. While running,\n'
      'one by one, your friends are caught and murdered You manage to find a small ditch behind a tree to hide in. On your way,\n'
      'you spotted a car in the distance, but it would not start due to some missing items. You must navigate your way around\n'
      'the forest and collect components for the car so that you can escape.')

print('\nYou need to find car keys, a car battery, spark plug wires, tires, a steering wheel, a toolbox, a gas can, and\n'
      'a first aid kit to treat your wounds. You will also need to find some food in order to have enough energy to escape\n'
      'all the while avoiding running into the serial killer. Enter "north, east, south, or west, to move around the forest')

# Dictionary of rooms linked to each-other
rooms = {
    'Your Hiding Place': {'west': 'Area Number 1'},
    'Area Number 1': {'north': 'Area Number 2', 'east': 'Your Hiding Place'},
    'Area Number 2': {'north': 'Area Number 5', 'east': 'Area Number 3', 'west': 'Area Number 4', 'south': 'Area Number 1'},
    'Area Number 3': {'west': 'Area Number 2'},
    'Area Number 4': {'east': 'Area Number 2'},
    'Area Number 5': {'north': 'Area Number 9', 'south': 'Area Number 2', 'east': 'Area Number 6', 'west': 'Area Number 8'},
    'Area Number 6': {'north': 'Area Number 7', 'west': 'Area Number 5'},
    'Area Number 7': {'south': 'Area Number 6'},
    'Area Number 8': {'east': 'Area Number 5', 'north': 'Villain Area'},
    'Area Number 9': {'south': 'Area Number 5', 'east': 'Escape Car', 'West': 'Villain Area'},
    'Villain Area': {'east': 'Area Number 9', 'south': 'Area Number 8'},
    'Escape Car': {'west': 'Area Number 9'},
}

# Items the players need to collect in the rooms in order to escape
items_in_rooms = {
    'Area Number 1': 'First aid kit',
    'Area Number 2': 'Tool box',
    'Area Number 3': 'Steering wheel',
    'Area Number 4': 'Spark plug wires',
    'Area Number 5': 'Food',
    'Area Number 6': 'Gas can',
    'Area Number 7': 'Car battery',
    'Area Number 8': 'Car keys',
    'Area Number 9': 'Tires'
}

# Inputs that allow player to move throughout the game
moves = ['north', 'south', 'east', 'west']
# Items the players need to collect in order to escape
items = ['Gas can', 'First aid kit', 'Spark plug wires', 'Tires', 'Car keys', 'Food', 'Steering wheel', 'Tool box', 'Car battery']
# Starting position of the player
location = 'Your Hiding Place'
# The players inventory containing collected items
inventory = []


# Loop for movement and item collection around the game
while True:
    print('\nYou are now in', location)
    print('Items in your inventory:', inventory)
    choice = input('Enter "search" to search around the area for an item or enter your next direction:\n')
    exits = rooms[location]
    if choice in exits:
        if exits[choice] == 'Escape Car' and not all(item in inventory for item in items):
            print(inventory)
            print('\nYou can not escape yet, you need to find more items to repair the car first!')
        else:
            location = exits[choice]
            if location == 'Villain Area':
                print("\nOH NO, YOU'VE BEEN CAUGHT BY THE SERIAL KILLER!!! Game Over:(!")
                break
            if location == 'Escape Car' and all(item in inventory for item in items):
                print("\nYou manage to find all of the parts and fix the car. You see the Serial killer fading away in the rear view mirror\n"
                      "as you drive further and further away from his cursed soul that has changed your life forever. About 15 miles away\n"
                      "you stumble upon a small town nearby and pull up their police station. You pull yourself together and step out of the\n"
                      "vehicle into the building. Inside, there are no lights on and it is dead silent. You call out for someone, anyone, but\n"
                      "there is no answer. It's a ghost town. It's 3 in the morning, you decide to just drive home and contact someone for help\n"
                      "in the morning. You make it home and decide to take a shower to wash all of the blood off of you when suddenly, you\n"
                      "feel a hot breath of air on your neck. You freeze, hesitant to turn around and then you feel his axe softly glide across\n"
                      "your neck. He cocks the axe back full force, and then he swings. You hit the ground and everything fades to black...\n")

                print("\nTHANKS FOR PLAYING!!! :)")
                break
    elif choice == "search":
        if location in items_in_rooms:
            item = items_in_rooms[location]
            print("\nYou search around the area and find the", item)
            YN = input('Do you want to pick it up? ')
            if YN == 'yes':
                inventory.append(item)
                del items_in_rooms[location]
            elif YN == 'no':
                print ('\nYou do not collect the item.')
            else:
                print('\nPlease enter "Yes" or "No".')
        else:
            print('\nYou do not find anything...:(')
    else:
        print("\nPlease enter a valid move.")