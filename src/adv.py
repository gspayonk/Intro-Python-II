from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons"),

    'foyer': Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow': Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'lake': Room("Underground Lake", """The still water reminds you of a distant dream. Shiny and cold, the reflection perfect. Ahead to the north, go back to the south."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together
# attributes
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
room['lake'].n_to = room['narrow']
room['lake'].s_to = room['overlook']

# Adding items 
bow = Item('bow','A small bow used for protection.' )
arrows = Item('arrows', 'A common arrow.')
axe = Item('axe', 'Great choice for felling trees. For combat - not so much.')
sword = Item('sword', 'Common sword, fends small beasts.')
shield = Item('shield', 'Common shield, will assist in a pinch.')

#rooms that hold items
room['outside'].items = [arrows]
room['foyer'].items = [shield]
room['overlook'].items = [bow]
room['narrow'].items = [axe]
room['treasure'].items = [sword]

#
# Main
#
newplayer_name = input('Enter player name: ')

# Make a new player object that is currently in the 'outside' room.
new_player = Player(newplayer_name, room['outside'])

# Write a loop that:
#
# * Prints the current room name
print(f'Current Room: { new_player.current_room.name }')

# * Prints the current description (the textwrap module might be useful here).
print(new_player.current_room.description)




# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

#assigning user input to be a string
user_input = ''

# if the user input is not q then take a looks and see where they are. hasattr function is used to check if the object matches the attribute and returns it if true.
while user_input != 'q':

    items_found = new_player.current_room.items
    no_items = True
    if items_found is not []:
            print('Items in room: ')
    for i in items_found:
            print(i)
    no_items = False

    user_input = input(' Welcome! We hope you find our world to be full of adventures! \n You will travel the land by using cardinal directions -- n for North, s for South, e for East and w for West. \n There\'s a chance that you\'ll find items along the way. \n If you do, feel free to pick it up by entering p. You can drop the item by entering d and you can check you pack by entering k. \n  Now, where do you want to go? Please enter which cardinal direction you would like to go: ')
    if user_input == 'n':
        if hasattr(new_player.current_room, 'n_to'):
            new_player.current_room = new_player.current_room.n_to
            print(f'Location: { new_player.current_room.name }')
            print(new_player.current_room.description)
            print(f'Items in room: { items_found }')
        else:
            print('Please enter choose a different direction.')
    elif user_input == 's':
        if hasattr(new_player.current_room, 's_to'):
            new_player.current_room = new_player.current_room.s_to
            print(f'Location: { new_player.current_room.name }')
            print(new_player.current_room.description)
            print(f'Items in room: { items_found }')
        else:
            print('Please enter choose a different direction.')
    elif user_input == 'e':
        if hasattr(new_player.current_room, 'e_to'):
            new_player.current_room = new_player.current_room.e_to
            print(f'Location: { new_player.current_room.name }')
            print(new_player.current_room.description)
            print(f'Items in room: { items_found }')
        else:
            print('Please enter choose a different direction.')
    elif user_input == 'w':
        if hasattr(new_player.current_room, 'w_to'):
            new_player.current_room = new_player.current_room.w_to
            print(f'Location: { new_player.current_room.name }')
            print(new_player.current_room.description)
            print(f'Items in room: { items_found }')
        else:
            print('Please enter choose a different direction.')
    elif user_input == 'p':
        if no_items:
            print('No items found')
        else:
            item_name = input('Enter item name that you wish to add to pack: ').lower()
            for i in items_found:
                if i.name == item_name:
                    new_player.get_item(i)
                    new_player.current_room.drop_item(i)
                    print(f'{ item_name} has been added to your pack.')
    elif user_input == 'd':
        print('Which item would you like to discard? ')
        for i in new_player.items:
            print(i)
        discard = input('').lower()
        for i in new_player.items:
            if i.name == discard:
                new_player.drop_item(i)
                new_player.current_room.get_item(i)
                print(f'{ discard } dropped!')
    elif user_input == 'q':
        print('Goodbye!')
    else:
        print('Invalid Key Entered')
    
