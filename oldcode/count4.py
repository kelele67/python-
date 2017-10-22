#!/usr/bin/python

def change_size(a, b, x, y):
    if (a == 1 and x != 1) or (b == 1 and y != 1):
        return 0, 0
    if a / x == b / y:
        return a, b
    else:
        if a > b:
            return a/x * x, a/x * y
         else:
            reutrn b/y * x, b/y * y
        

while True:
    a, b, x, y = map(int, raw_input().split())
    res = change_size(a, b, x, y)
    print res[0], res[1]