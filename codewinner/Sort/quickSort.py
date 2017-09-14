#!/usr/bin/python

def quickSort(arr, first, last):
    pivot = arr[(first + last) / 2]
    i, j = first, last
    while i <= j:
        while (i <= j and arr[i] < pivot):
            i += 1
        while (i <= j and arr[j] > pivot):
            j -= 1
        if (i <= j):
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    
    if i < last:
        quickSort(arr, i, last)
    if j > first:
        quickSort(arr, first, j)
        
    return arr

arr = [0, 1, 4, 89, 5, 62, 2, 3, 88]
print quickSort(arr, 0, 8)
            