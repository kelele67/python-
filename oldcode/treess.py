# N = int(raw_input())
# all = [[] for i in range(N)]

# for i in range(N):
#     row = raw_input().split()
#     if row[1] == '-1':
#         root = row[0]
#     else:
#         (all[int(row[1])]).append(row[0])

# print root
# padding = '|'
# for i in range(len(all)):
#     for j in range(len(all[i])):
#         if i == 0:
#             print padding + '-- ' + all[i][j]
#         if j == len(all[i]):
#             print '`-- ' + all[i][j]
#         else:
#             print '    ' * i + padding + '-- ' + all[i][j]
import math

def musicList(N, M, P):
    if P < N:
        return 0
    if P == N:
        sum = math.factorial(N)
    if P > N:
        res = P / N
        rest = P % N
        for i in (M, N):
            sum += res * (N * math.factorial(i)) * rest
    ret = sum % 1000000007
    return ret

N, M, P = map(int, raw_input().split())
print musicList(N, M, P)