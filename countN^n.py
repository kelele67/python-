#!/usr/bin/python

def count(N):
    res = 1;
    n = 2
    while N:
        if N & 1 == 1:
            res = res * n
        n = n * n
        N >>= 1
    return res

N = int(raw_input())
print count(N)