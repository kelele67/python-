def maxValue(N, arr):
    MAX = []
    for i in range(N):
        MAX[i] = max(count(arr[i]), count(arr[i+1]))

def count(i):
    for 
    ret = min(a) * sum(a)
    return ret

def maxProduct(N, arr):
    max = 1
    min = 1
    maxP = 1
    for i in range(N):
        if arr[i] > 0:
            max = max * arr[i]
            min = min(min *arr[i], 1)
        elif arr[i] == 0:
            max = 1
            min = 1
        else:
            tmp = max
            max = max(min * arr[i], 1)
            min = tmp * arr[i]
        if (maxP / min(arr[:i+1])) < (max / min(arr[:i+1])):
            maxP = max
            result = maxP / min(arr[:i+1])
    return m

N = int(raw_input())
arr = map(int, raw_input().split())
print maxProduct(N, arr)

from itertools import combinations

def count(arr):
    MAX = float("-inf")
    f = lambda s: reduce(list.__add__, (list(map(list, combinations(s, l))) for l in range(1, len(s))),[])
    for x in f(arr): 
        if sum(x) * min(x) > MAX:
            MAX = mul(x) * min(x)
    return MAX

n = int(raw_input())
arr = map(int, raw_input().split())
print count(arr)