import sys
import random

def throw_result(playey_throw, computer_throw):	
	if playey_throw == 'rock':	
		if computer_throw == 'paper':
			return 0
		elif computer_throw == 'scissors':
			return 1
		else:
			return 2
	elif playey_throw == 'paper':
		if computer_throw == 'rock':
			return 1
		elif computer_throw == 'scissors':
			return 0
		else:
			return 2
	elif playey_throw == 'scissors':
		if computer_throw == 'rock':
			return 0
		elif computer_throw == 'paper':
			return 1
		else:
			return 2
	else:
		return -1

games_played = 0
player_score = 0
computer_score = 0
throw_options = ['rock', 'paper', 'scissors']

while games_played < 11:
	player_throw = raw_input('Rock, Paper, Scissors: ')
	computer_throw = throw_options[random.randint(0,2)]
	score = throw_result(player_throw, computer_throw)
	
	if score > -1:
		if score == 0:
			computer_score += 1
			print 'You lost this round'
		elif score == 1:
			player_score += 1
			print 'You won this round'
		else:
			print 'You tied this round'
		games_played += 1
	else:
		print 'Invalid input'
		continue

if player_score > computer_score:
	print 'You won the game'
elif computer_score > player_score:
	print 'You lost the game'
else:
	print 'You tied'

print 'You won ',str(player_score/float(games_played)* 100),'% of the rounds'