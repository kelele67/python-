# -*- coding: utf-8 -*-
## 只是2的倍数，4的倍数，其他的倍数
## 当4的倍数  >= 其他 ： 成立
## 当4的倍数  < 其他 ： 不成立
## 当4的倍数    = 0 ：有其他： GG， 没有其他：数组个数为偶数（2的个数）
def isGood(arr, N):
    count_four = count_two = count_else = 0
    if N == 0:
        return "No"
    if N == 1:
        if arr[0] % 4 == 0:
            return "Yes"
        else:
            return "No"
    for i in range(N):
        if arr[i] % 4 == 0:
            count_four += 1
        elif arr[i] % 4 != 0 and arr[i] % 2 == 0:
            count_two += 1
        else:
            count_else += 1
    if count_four == 0:
        if count_else != 0:
            return "No"
        else:
            if N % 2 == 0:
                return "Yes"
            else:
                return "No"
    elif count_four >= count_else:
        return "Yes"
    elif count_four < count_else:
        return "No"
    else:
        return "No"

t = int(raw_input())
for i in range(t):
    N = int(raw_input())
    arr = map(int, raw_input().split())
    print isGood(arr, N)