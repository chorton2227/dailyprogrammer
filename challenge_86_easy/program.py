import sys

if len(sys.argv)==1:
	print 'Enter arguments'
	exit(0)

text = sys.argv[1]
arr = []

for i in range(len(text)):
	if len(arr) > 0 and arr[(len(arr)-1)][0] == text[i]:
		arr[(len(arr)-1)][1] += 1
	else:
		arr.append([text[i], 1])

print arr

text = ''
for char in arr:
	text += char[0] * char[1]
print text