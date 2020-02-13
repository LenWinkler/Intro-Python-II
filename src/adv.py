import textwrap

from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
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

# Make a new player object that is currently in the 'outside' room.

player = Player('Hero', room['outside'])
# current_room = player.current_room
room_name = player.current_room.name
room_description = textwrap.fill(player.current_room.description)


# current_room = room[player.current_room].n_to
# print('current room', player.current_room)
# print('current name', room_name)
print('1', room['outside'])
print('2', room['foyer'])
print('3', room['overlook'])
print('4', room['narrow'])
print('5', room['treasure'])
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

while True:
    print(f'\n{room_name}\n')
    print(f'\n{room_description}\n')
    print(f'\nEnter the first letter of the direction you wish go (eg. "n", "s", "e", "w"). Type "q" to quit\n')
    action = input("What do you want to do? ").lower()

    if action == 'q':
        print('\nGoodbye!\n')
        exit()
    elif room_name == 'Outside Cave Entrance' and action == 'n':
        print('before', player.current_room)
        setattr(player, 'current_room', player.current_room.n_to)
        print('after', player.current_room)
    elif room_name == 'foyer' and action == 'n':
        player.current_room = room[player.current_room].n_to
    elif room_name == 'foyer' and action == 'e':
        player.current_room = room[player.current_room].e_to
    elif room_name == 'narrow' and action == 'n':
        player.current_room = room[player.current_room].n_to
    elif room_name == 'narrow' and action == 'w':
        player.current_room = room[player.current_room].w_to
    elif room_name == 'treasure' and action == 's':
        player.current_room = room[player.current_room].s_to
    else:
        print('\n-------------------------------------------\n You are unable to move in that direction!\n-------------------------------------------\n')
