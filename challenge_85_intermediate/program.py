import sys

def draw_ascii_3d_box(length, height, depth):
	sys.stdout.write(''.join((' ' * (depth - i) + ':' * (length - 1) + '/' + '+' * i +'\n') for i in range(depth)))
	
	for i in range(height):
		line = ''.join('#' for _ in range(length))
		if height - i > depth:
			line += '+' * depth
		else:
			line += '+' * (height - (i + 1))
		print line

if len(sys.argv)==1:
	print 'Enter arguments'
	exit(0)
	
draw_ascii_3d_box(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]))