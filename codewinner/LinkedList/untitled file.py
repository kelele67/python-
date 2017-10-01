# -*- coding: utf-8 -*-

# 剔除最大数-> 找子数组有没有等于 t - 1, t-2...的 然后+最大的数

def find_sum(arr, n, target):
    temp = arr[:]
    sums = 0
    for i in range(n):
        for j in range(i, n):
            sums = sums + arr[j]
            temp.remove(arr[j])
            if (sums == target):
                return temp
    return -1

def max_time(arr, n, t):
    m = max(arr)
    arr.remove(m)
    for i in range(t-1, 0, -1):
        if find_sum(arr, n-1, i):
            res = i + m
            return res
    else:
        return max(arr)
        
n, t = map(int, raw_input().split())
arr = map(int, raw_input().split())
print max_time(arr, n, t)           
            