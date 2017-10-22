# from itertools import combinations
# def mul(x):
#     mul = 1
#     for value in x:
#         mul *= value
#     return mul
# def luckyBag(balls):
#     count = 0
#     f = lambda s: reduce(list.__add__, (list(map(list, combinations(s, l))) for l in range(1, len(s))),[])
#     for x in f(balls): 
#         if sum(x) > mul(x):
#             count = count + 1
#     return count

# n = int(raw_input())
# balls = map(int, raw_input().split())
# print luckyBag(balls)

raw_input()
arr=map(int,raw_input().strip().split())
 
arr.sort()
n1=len(filter(lambda x:x==1,arr))
arr=filter(lambda x:x>1,arr)
n2=len(arr)
 
cnt=0
cnt+=max(n1-1,0)
 
def dfs(arr2,mul,add,pos,n1):
    mul=mul*arr2[pos]
    add=add+arr2[pos]
    if mul-add>=n1:
        return 0
    cnt=1
    visited=set()
    for i in range(pos+1,len(arr2)):
        if arr2[i] in visited:
            continue
        visited.add(arr2[i])
        ocnt=dfs(arr2,mul,add,i,n1)
        cnt+=ocnt
        if not ocnt:
            return cnt
    return cnt
 
for j in range(1,n1+1):
    visited=set()
    for i in range(len(arr)):
        if arr[i] in visited:
            continue
        visited.add(arr[i])
        ocnt=dfs(arr,1,0,i,j)
        if not ocnt:
            break
        cnt+=ocnt
print cnt