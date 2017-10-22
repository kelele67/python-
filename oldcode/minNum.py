# from itertools import combinations
# def minNum(num_list):
#     sums = []
#     # f = lambda s: reduce(list.__add__, (
#     # list(map(list, combinations(s, l)))
#     #     for l in range(1, len(s))),
#     # [])
#     f = lambda s: reduce(list.__add__, (list(map(list, combinations(s, l))) for l in range(1, len(s))),[])
#     for x in f(num_list):
#         sums.append(sum(x))
#     # sums = sorted(sums)
#     # for i in range(1, len(sums)):
#     #     if sums[i]-sums[i-1] > 1:
#     #         return sums[i-1]+1
#     for i in range(1, sum(num_list)+1):
#         if i not in sums:
#             if i != sum(num_list):
#                 return i
#     return sum(num_list)+1

# n = int(raw_input())
# num_list = map(int, raw_input().split())
# print minNum(num_list)

# from itertools import combinations
# def minNum(num_list):
#     sums = []
#     f = lambda s: reduce(list.__add__, (list(map(list, combinations(s, l))) for l in range(1, len(s))),[])
#     for x in f(num_list):
#         sums.append(sum(x))
#     for i in range(1, sum(num_list)+1):
#         if i not in sums:
#             if i != sum(num_list):
#                 return i
#     return sum(num_list)+1

# n = int(raw_input())
# num_list = map(int, raw_input().split())
# print minNum(num_list)

def minNum(n, num_list):
    miss = 0
    sort(num_list)
    for i in range(n):
        if num_list[i] > miss+1:
            break
        miss += num_list[i]
    return miss+1

n = int(raw_input())
num_list = map(int, raw_input().split())
print minNum(n, num_list)