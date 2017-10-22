#!/usr/bin/python

def shell_sort(arr):
    n = len(arr)
    gap = n/2
    
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j-gap] > temp:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = temp
            print arr
        gap /= 3
    return arr

arr = [20,15, 8, 16, 10, 30, 4, 26, 25,]
print shell_sort(arr)