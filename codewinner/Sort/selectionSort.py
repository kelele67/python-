#!/usr/bin/python

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

arr = [0, 1, 4, 89, 5, 62, 2, 3, 88, 5]
print selection_sort(arr)