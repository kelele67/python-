from math import sqrt

def isInCircle(n):
    count = 0
    r = sqrt(n)
    for x in range(1, int(r)+1):
        y = sqrt(n - x*x)
        if y == int(y) and y != 0:
            count = count + 1
    if r == int(r):
        return 4*count + 4
    return 4*count

n = int(raw_input())
print isInCircle(n)
