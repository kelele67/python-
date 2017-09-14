#!/usr/bin/python

#def insert_sort(arr, n):
#    for i in range(1, n):
#        j = i
#        while j > 0 and arr[j] < arr[j-1]:
#            arr[j], arr[j-1] = arr[j-1], arr[j]
#            j -= 1
#    return arr

#def insert_sort2(arr, n):
#    for i in range(1, n):
#        for j in range(i)[::-1]:
#            if arr[j] > arr[j+1]:
#                arr[j], arr[j+1] = arr[j+1], arr[j]
#    return arr

def insert_sort_guard(arr, n):
    for i in range(1, n):
        key = arr[i]
        for j in range(i)[::-1]:
            if arr[j] > key:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            else:
                break
        arr[j+1] = key
    return arr

arr = [0, 1, 4, 89, 5, 62, 2, 3, 88]
n = 9
print insert_sort_guard(arr, n)
    