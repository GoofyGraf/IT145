rooms = {
    'Prison Cell ': {
        'North': 'Great Hall',
        'East': 'Sewers'
    },
    'Sewers': {
        'West': 'Prison Cell',
        'North': 'Basement',
        'Item': 'Poison'
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





rooms = {
    'Prison Cell' : {
        'North' : 'Great Hall',
        'East' : 'Sewers'}, 'Sewers' : {'West' : 'Prison Cell', 'North' : 'Basement', Item : Poison}, Basement : {West : Great Hall, North : Kitchen, South : Sewers, Item : Torch}, Kitchen : {North : Living Quarters, South : Basement, Item : Food}, Living Quarters : {West : Throne Room, South : Kitchen, Item : Diary}, Great Hall : {North : Throne Room, West : Guard Tower, East : Basement, South : Prison Cell, Item : Liquid Courage}, Guard Tower : {North : Training Arena, East : Great Hall, Item : Armor}, Training Arena : {North : Wizard Tower, South : Guard Tower, Item : Sword}, Wizard Tower : { South : Training Arena, Item : Magical Trinket}}
SET player = {room = Sewers, items = []}
SET items = [‘Poison’, ‘Torch’, ‘Food’, ‘Diary’, ‘Liquid Courage’, ‘Armor’, ‘Sword’, ‘Magical Trinket’]
PRINT You are in the {player[“room”]}
PRINT You see rooms[player[“rooms”]][“item”] on the floor!
PRINT Enter Get rooms[player[“rooms”]][“item”] to add it to your inventory!
INPUT Get item name
WHILE INPUT != quit
	IF INPUT = quit
		PRINT Thanks for playing!
	ENDIF
	IF INPUT in items
		IF INPUT = [player[“rooms]][“item”]
			player[“items”].push(room.item)
			PRINT Your inventory now has player[“items”] in it!
		ELSE
			PRINT That item isn’t in this room!
	ELSE
		PRINT Invalid Item!
		ENDIF
	END
