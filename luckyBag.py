from itertools import combinations
def mul(x):
    mul = 1
    for value in x:
        mul *= value
    return mul
def luckyBag(balls):
    count = 0
    f = lambda s: reduce(list.__add__, (list(map(list, combinations(s, l))) for l in range(1, len(s))),[])
    for x in f(balls): 
        if sum(x) > mul(x):
            count = count + 1
    return count

n = int(raw_input())
balls = map(int, raw_input().split())
print luckyBag(balls)