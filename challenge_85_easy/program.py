import sys

def max_length(matrix):
	maxlength = 0
	for row in matrix:
		for val in row:
			length = len(str(val))
			if length > maxlength:
				maxlength = length
	return maxlength

def draw_border(space, length):
	print "-" * (((space + 1) * length) + 1)

def print_matrix(matrix):
	max_space = max_length(matrix)
	for row in matrix:
		line = "|"
		for col in row:
			line += (' ' * (max_space - len(str(col)))) + str(col) + "|"
		draw_border(max_space, len(row))
		print line
	draw_border(max_space, len(row))

if len(sys.argv)==1:
	print 'Enter file as argument'
	exit(0)

file = open(sys.argv[1], 'r')

rowmatrix = [[int(word) for word in line.split(' ')] for line in file.readlines()]
colmatrix = zip(*rowmatrix)
rowmatrixsum = [(sum(n), n) for n in rowmatrix]
colmatrixsum = [(sum(n), n) for n in colmatrix]
rowmatrixsum = sorted(rowmatrixsum)
colmatrixsum = sorted(colmatrixsum)

rowsum = [row[0] for row in rowmatrixsum]
colsum =  [col[0] for col in colmatrixsum]
rowmatrixsorted = [row[1] for row in rowmatrixsum]
colmatrixsorted =  [col[1] for col in colmatrixsum]

print 'Rows: ' + str(rowsum)
print 'Columns: ' + str(colsum)
print 'Row Matrix Sorted:'
print_matrix(rowmatrixsorted)
print 'Column Matrix Sorted:'
print_matrix(colmatrixsorted)