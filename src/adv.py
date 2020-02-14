import textwrap

from room import Room
from player import Player
from item import Item

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


sword = Item('sword', 'a rusty sword')
torch = Item('torch', 'a torch')
key = Item('key', 'a skeleton key')
gold = Item('gold', 'a handful of gold coins')

def add_item_to_room(which_room, item_name):
    room[which_room].items.append(item_name)

def add_to_inventory(item_name):
    if item_name in player.current_room.items:
        player.inventory.append(item_name)
        player.current_room.items.remove(item_name)
        item_name.on_take()
    else:
        print('Can\'t find item by that name')

def drop_from_inventory(item_name):
    if item_name in player.inventory:
        player.current_room.items.append(item_name)
        player.inventory.remove(item_name)
        item_name.on_drop()
    else:
        print('Can\'t find item by that name')

add_item_to_room('foyer', sword)
add_item_to_room('foyer', torch)
add_item_to_room('overlook', key)
add_item_to_room('treasure', gold)



def visible_items(items):
    items_str = ""
    for item in items:
        if len(items_str) < 1:
            items_str += item.name
        else: items_str += f', {item.name}'
    
    return items_str

commands = ['"n", "s", "e", or "w" to move', '"i" or "inventory" to open inventory', '"get <item>" or "take <item>" to pick up an item', '"drop <item>" to drop an item', '"q" to quit']

def help():
    for cmd in commands:
        print(cmd)

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player(input('What is your name? '), room['outside'])
print(f'\nGood luck, {player.name}!')

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
    current_room = player.current_room
    room_name = current_room.name
    print(f'\n\n{current_room}\n')
    if len(current_room.items) < 1:
        print(f'\nLooking around the area, you see nothing of interest.\n')
    else:
        print(f'\nLooking around the area, you see these items: {visible_items(current_room.items)}\n')

    action = input('What do you want to do? (Type "help" for list of commands. Type "q" to quit) ').lower()
    split_action = action.split(' ')

    if len(split_action) > 1 and split_action[0] == 'get' or split_action[0] == 'take':
        if split_action[1] == 'sword' and sword in current_room.items:
            add_to_inventory(sword)
        elif split_action[1] == 'torch' and torch in current_room.items:
            add_to_inventory(torch)
        elif split_action[1] == 'key' and key in current_room.items:
            add_to_inventory(key)
        elif split_action[1] == 'gold' and gold in current_room.items:
            add_to_inventory(gold)
        else:
            print('Can\'t find item by that name')

    elif len(split_action) > 1 and split_action[0] == 'drop':
        if split_action[1] == 'sword' and sword in player.inventory:
            drop_from_inventory(sword)
        elif split_action[1] == 'torch' and torch in player.inventory:
            drop_from_inventory(torch)
        elif split_action[1] == 'key' and key in player.inventory:
            drop_from_inventory(key)
        elif split_action[1] == 'gold' and gold in player.inventory:
            drop_from_inventory(gold)
        else:
            print('Item not in inventory')

    elif action == 'q':
        print(f'\nGoodbye, {player.name}!\n')
        exit()
    elif action == 'help':
        print('\nCommands:')
        help()
    elif room_name == 'Outside Cave Entrance' and action == 'n':
        player.current_room = player.current_room.n_to
    elif room_name == 'Foyer' and action == 's':
        player.current_room = player.current_room.s_to
    elif room_name == 'Foyer' and action == 'n':
        player.current_room = player.current_room.n_to
    elif room_name == 'Foyer' and action == 'e':
        player.current_room = player.current_room.e_to
    elif room_name == 'Grand Overlook' and action == 's':
        player.current_room = player.current_room.s_to
    elif room_name == 'Narrow Passage' and action == 'n':
        player.current_room = player.current_room.n_to
    elif room_name == 'Narrow Passage' and action == 'w':
        player.current_room = player.current_room.w_to
    elif room_name == 'Treasure Chamber' and action == 's':
        player.current_room = player.current_room.s_to
    else:
        print('\n-------------------------------------------\n You are unable to move in that direction!\n-------------------------------------------')
