#!/usr/bin/python

# merge two subarrays of arr
# arr[l...m]
# arr[m+1, r]
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    # temp arrays
    L = [0] * n1
    R = [0] * n2
    for i in range(0, n1):
        L[i] = arr[l + i]
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
    # merge temp arrays into arr[l...k]
    i = 0
    j = 0
    k = l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
        
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

    return arr

def merge_sort(arr, l, r):
    if l < r:
        m = l + (r - l) / 2
        merge_sort(arr, l, m)
        merge_sort(arr, m+1, r)
        merge(arr, l, m, r)
    return arr

arr = [0, 1, 4, 89, 5, 62, 2, 3, 88]
print merge_sort(arr, 0, 8)