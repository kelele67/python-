#!/usr/bin/python

def makePalidrome(arr, n):
##    i = j = 0
##    print n
#    if n % 2 == 0:
#        print "yes"
#        i = n/2 - 1
#        j = n/2
#        res = 0
#    else:
#        i = n/2 - 1
#        j = n/2 + 1
#        res = arr[n/2]
##    print i, j
#    while i >= 0 and j <= n-1:
#        if arr[i] == arr[j]:
#            res += arr[i] + arr[j]
#            i -= 1
#            j += 1
#        elif arr[i] < arr[j]:
#            res += arr[i] * 2
#            i -= 1
#        else:
#            res += arr[j] * 2
#            j += 1
#    print i, j
#    while i >= 0:
#        res += arr[i]
#        i -= 1
#    while j <= n-1:
#        res += arr[j]
#        j += 1
#        
#    print i, j
#    return res
    res = 0
    first, last = 0, n-1
    while first < last - 1:
        if arr[first] == arr[last]:
            res += arr[first] + arr[last]
            first += 1
            last -= 1
        elif arr[first] < arr[last]:
            res += arr[first] * 2
            first += 1
        else:
            res += arr[last] * 2
            last -= 1
    if first != last:
        if arr[first] == arr[last]:
            return (res + arr[first] + arr[last])
        else:
            return (res + (arr[first] + arr[last]) * 2)
    else:
        return (res + arr[first])
    
n = int(raw_input())
arr = map(int, raw_input().split())
print makePalidrome(arr, n)