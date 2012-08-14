import sys
import string
import time

def solve(msg, key):
	alphabet = list(string.ascii_uppercase)
	output = ""

	for i in range(len(msg)):
		output += alphabet[(alphabet.index(msg[i]) + alphabet.index(key[i%len(key)]))%len(alphabet)]
	return output

if len(sys.argv)==1:
	print 'Enter arguments'
	exit(0)

msg = sys.argv[1]
key = sys.argv[2]

print solve(msg, key)