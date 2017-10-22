def isTree(N, all):
    for i in range(N):
        if i not in all:
            return False

M, N = map(int, raw_input().split())
all = []
for i in range(M):
    all.append(map(int, raw_input().split()))

if isTree(N, all):
    print "YES"
else:
    print "NO"

# while True:
#     try:
#         (x, y) = (int(x) for x in raw_input().split())
#         print x + y
#     except EOFError:
#         break