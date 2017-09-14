#!/usr/bin/python

#def bubble_sort(arr):
#	n = len(arr)
#	for i in range(n):
#		for j in range(0, n-i-1):
#			if arr[j] > arr[j+1]:
#				arr[j], arr[j+1] = arr[j+1], arr[j]
#	return arr

#def better_bubble_sort(n, arr):
#	for i in range(n)[::-1]:
#		swaped = False
#		for j in range(i):
#			if arr[j] > arr[j+1]:
#				arr[j], arr[j+1] = arr[j+1], arr[j]
#				swaped = True
#		if not swaped:
#		    return arr
#	return arr

#def better_bubble_sort(arr):
#	n = len(arr)
#	for i in range(n):
#		swapped = False
#		for j in range(0, n-1-i):
#			if arr[j] > arr[j+1]:
#				arr[j], arr[j+1] = arr[j+1], arr[j]
#				swapped = True
#		if not swapped:
#			print "yes"
#			return arr
#	return arr

def sharker_sort(arr):
	n = len(arr)
	left, right = 0, n-1
	while left < right:
		for i in range(left, right):
			if arr[i] > arr[i+1]:
				arr[i], arr[i+1] = arr[i+1], arr[i]
		right -= 1
		for j in range(left+1, right)[::-1]:
			if arr[j] < arr[j-1]:
				arr[j], arr[j-1] = arr[j-1], arr[j]
		left += 1
	
	return arr

arr = [0, 1, 4, 89, 5, 62, 2, 3, 88, 5]
#print bubble_sort(arr)
#print better_bubble_sort(arr)
print sharker_sort(arr)