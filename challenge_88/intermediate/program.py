import sys
import calendar

if len(sys.argv)==1:
	print 'Enter arguments'
	exit(0)

year = int(sys.argv[1])
month = int(sys.argv[2])

print '\n'.join(calendar.month(year, month).split('\n'))