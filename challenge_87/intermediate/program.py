import sys

if len(sys.argv)==1:
	print 'Enter arguments'
	exit(0)

note = sys.argv[1][:1]
symbol = sys.argv[1][1:]
notes = ('C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#' 'B')
chords = {'major':     [0, 4, 7],
			  'm':     [0, 3, 7],
			  '7': [0, 4, 7, 10],
			 'm7': [0, 3, 7, 10],
		   'maj7': [0, 4, 7, 11]}

if note not in notes or symbol not in chords:
	print 'Invalid input'
	exit(0)

output = []
for i in chords[symbol]:
	output.append(notes[(notes.index(note) + i) % (len(notes) + 1)])
print output