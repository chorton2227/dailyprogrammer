import sys
import math
from datetime import date

if len(sys.argv)==1:
	print 'Enter arguments'
	exit(0)

days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

day = int(sys.argv[1])
month = int(sys.argv[2])
year = sys.argv[3]

T = int(year[2:])
if T & 1:
	T += 11
T /= 2
if T & 1:
	T += 11
T = 7 - (T % 7)

cent = int(year[:-2]) + 1
anchor = ((5 * cent + ((cent - 1) / 4)) % 7 + 4) % 7
doomsday = (anchor + T) % 7

year = int(year)

search_date = date(year, month, day)
doomsday_date = date(year, 4, 4)

print days[(doomsday + (search_date - doomsday_date).days) % 7]