from room import Room
from player import Player

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

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

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

user_input = ''

while user_input != 'q':
    user_input = input('Where do you want to go? Please enter which cardinal direction wou would like to go (n for North, s for South, e for East and w for West: ')
    if user_input == 'n':
        if hasattr(new_player.current_room, 'n_to'):
            new_player.current_room = new_player.current_room.n_to
            print(f'Location: { new_player.current_room.name }')
            print(new_player.current_room.description)
        else:
            print('Please enter choose a different direction.')
    elif user_input == 's':
        if hasattr(new_player.current_room, 's_to'):
            new_player.current_room = new_player.current_room.s_to
            print(f'Location: { new_player.current_room.name }')
            print(new_player.current_room.description)
        else:
            print('Please enter choose a different direction.')
    elif user_input == 'e':
        if hasattr(new_player.current_room, 'e_to'):
            new_player.current_room = new_player.current_room.e_to
            print(f'Location: { new_player.current_room.name }')
            print(new_player.current_room.description)
        else:
            print('Please enter choose a different direction.')
    elif user_input == 'w':
        if hasattr(new_player.current_room, 'w_to'):
            new_player.current_room = new_player.current_room.w_to
            print(f'Location: { new_player.current_room.name }')
            print(new_player.current_room.description)
        else:
            print('Please enter choose a different direction.')
    elif user_input == 'q':
        print('Goodbye!')
    else:
        print('Invalid Key Entered')
    
