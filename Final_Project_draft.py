rooms = {
    'Prison Cell ': {
        'North': 'Great Hall',
        'East': 'Sewers'
    },
    'Sewers': {
        'West': 'Prison Cell',
        'North': 'Basement'
    },
    'Basement': {
        'West': 'Great Hall',
        'North': 'Kitchen',
        'South': 'Sewers'
    },
    'Kitchen': {
        'North': 'Living Quarters',
        'South': 'Basement'
    },
    'Living Quarters': {
        'West': 'Throne Room',
        'South': 'Kitchen'
    },
    'Great Hall': {
        'North': 'Throne Room',
        'West': 'Guard Tower',
        'East': 'Basement',
        'South': 'Prison Cell'
    },
    'Guard Tower': {
        'North': 'Training Arena',
        'East': 'Great Hall'
    },
    'Training Arena': {
        'North': 'Wizard Tower',
        'South': 'Guard Tower'
    },
    'Wizard Tower': {
        'South': 'Training Arena'
    }
}
player = {'room': 'Prison Cell'}  # Declare player dict with Key:value pairs and starting room

directions = {'North', 'South', 'East', 'West', 'Exit'}  # Inputs accepted while navigating rooms
print('Welcome to the Module Six Milestone Castle, you are in the Prison Cell!')
print('Enter North, South, East, or West to move to a new room!\nEnter Exit to quit!')

while player["room"] != 'Exit':  # Code will loop while player isn't in the Exit room
    user_input = input('Enter a direction to move:\n').capitalize()  # Prompts for user input //
    # .capitalize allows for flexible input validation
    if user_input == 'Help':  # Provides user with list of valid inputs
        print('Enter North, South, East or West to move between rooms or Exit to quit the game.')
    elif user_input in directions:  # checks if input is in accepted list of inputs
        if user_input in rooms[player["room"]]:  # assigns player to new room if input is valid
            player["room"] = rooms[player["room"]][user_input]
            print(f'You are in the {player["room"]}')  # Returns updated player room
        else:
            print('You can\'t go that way from this room')  # Valid input, but invalid direction from current room
    else:
        print('Invalid Direction, Enter help for valid commands!')  # Invalid input, returns help command

if player["room"] == 'Exit':  # Ends current game
    print('Thanks for playing!')
