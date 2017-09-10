# -*- coding: utf-8 -*-

# 考虑两种情况：桌子上的试卷不够－＞ 剩下的试卷小与下一组+　学生改到自己的试卷－＞最后一组小与第一组

def isGood(arr, N):
    if N == 0:
        return "Yes"
    rest = 0
    for i in range(N):
        for v in arr[:i] + arr[i+1:]:
            flag = 0
            rest += arr[i]
            if v <= rest:
                rest -= v
                break
            else:
                flag += 1
            if flag == i:
                return "No"
    if rest < arr[0]:
        return "Yes"
    return "No"

N = int(raw_input())
arr = map(int, raw_input().split())
print isGood(arr, N)