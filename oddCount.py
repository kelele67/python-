# -*- coding: utf-8 -*-
# def oddCount(n):
#     sum = 0
#     for i in range(1, n+1):
#         if i % 2 == 0:
#             while (i != 1 and i % 2 ==0):
#                 i /= 2
#             sum += i
#         else:
#             sum += i
#     return sum

# n = int(raw_input())
# print oddCount(n)

# import sys   
# sys.setrecursionlimit(1000000)
def oddCount(n):
    if n == 1:
        return 1
    if n % 2 != 0:
        return oddCount(n-1) + n
    else:
        return oddCount(n/2) + n*n / 4

n = int(raw_input())
print oddCount(n)

# -*- coding: utf-8 -*-
# 数字很大递归失败
# 建立一个list保存每个数字的最大公约数
# def oddCount(n):
#     odds = []
#     for i in range(1, n+1):
#         if i == 1:
#             odds.append(1)
#         elif i % 2 != 0:
#             odds.append(i)
#         else:
#             while (i % 2 == 0):
#                 i /= 2
#             odds.append(i)
#     return sum(odds)

# n = int(raw_input())
# print oddCount(n)