import sys
import math

def rect_intersection(rect1, rect2):	
	if rect2[0] >= rect1[0] and rect2[0] <= rect1[2]:
		if rect2[1] >= rect1[1] and rect2[1] <= rect1[3]:
			top_left = (rect2[0], rect2[1])
			if rect2[2] <= rect1[2] and rect2[3] <= rect1[3]:
				bottom_right = (rect2[2], rect2[3])
			else:
				bottom_right = (rect1[2], rect1[3])
			return list(top_left + bottom_right)
	elif rect1[0] >= rect2[0] and rect1[0] <= rect2[2]:
		if rect1[1] >= rect2[1] and rect1[1] <= rect2[3]:
			top_left = (rect1[0], rect1[1])
			if rect1[2] <= rect2[2] and rect1[3] <= rect2[3]:
				bottom_right = (rect1[2], rect1[3])
			else:
				bottom_right = (rect2[2], rect2[3])
			return list(top_left + bottom_right)

def rect_intersection2(r1, r2):
	if is_between(r1[0], r1[1], r2[0]) :
		if is_between(r1[0], r1[1], r2[1]) :
			return r2[0], r2[1]
		else:
			return r2[0], r1[1]
	elif is_between(r2[0], r2[1], r1[0]) :
		if is_between(r2[0], r2[1], r1[1]) :
			return r1[0], r1[1]
		else:
			return r1[0], r2[1]

def dist(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def is_between(a, b, c):
    return dist(a,c) + dist(c,b) == dist(a,b)
		
rect1 = (3, 3, 10, 10)
rect2 = (6, 6, 12, 12)
rect3 = (3, 3, 5, 5)
		
print rect_intersection(rect1, rect2)
print rect_intersection(rect3, rect2)
print rect_intersection(rect2, rect1)
		
rect1 = ((3, 3), (10, 10))
rect2 = ((6, 6), (12, 12))
rect3 = ((3, 3), (5, 5))
		
print rect_intersection2(rect1, rect2)
print rect_intersection2(rect3, rect2)
print rect_intersection2(rect2, rect1)