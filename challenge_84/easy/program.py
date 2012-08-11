import sys
from random import randint

treasure = {'X':randint(-100, 100), 'Y':randint(-100,100)}
location = {'X':0, 'Y':0}

while treasure["X"] != location["X"] or treasure["Y"] != location["Y"]:
	direction = raw_input('Which direction? ')
	
	if direction == 'N' or direction == 'NORTH':
		location["X"] += 1
	elif direction == 'S' or direction == 'SOUTH':
		location["X"] -= 1
	elif direction == 'E' or direction == 'EAST':
		location["Y"] += 1
	elif direction == 'W' or direction == 'WEST':
		location["Y"] -= 1
	elif direction == 'Q' or direction == 'QUIT':
		exit(0);
	else:
		print 'Invalid input'
		continue
	
	distance = (((location["X"] - treasure["X"]) ** 2) + ((location["Y"] - treasure["Y"]) ** 2)) ** 0.5
	print 'The treasure is ' + str(distance) + ' miles away'

print 'You found the treasure'
