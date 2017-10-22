# -*- coding: utf-8 -*-
# 很明显纯净的字符串要少很多
# 所以我们算纯净的字符串
# def isDarkString(n):
#     all = 3 ** n
#     if n < 3:
#         return all
#     pure = 6 * ((n-3)*3 + 1)
#     return all-pure

# while True:
def isDarkString(n):
    dp = []
    dp.append(3)
    dp.append(9)
    for i in range(2, n):
        dp.append(2 * dp[i-1] + dp[i-2])
    return dp[n-1]

n = int(raw_input())
print isDarkString(n)