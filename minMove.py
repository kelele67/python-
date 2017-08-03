# def minMove(n, L):
#     count = 0
#     X = sorted(L)
#     while L != X:
#         tmp = min(L)
#         L.remove(tmp)
#         L = [tmp] + L
#         count = count + 1
#     return count

# def minMove_max(n, L):
#     count = 0
#     X = sorted(L)
#     while L != X:
#         tmp = max(L)
#         L.remove(tmp)
#         L.append(tmp)
#         count = count + 1
#     return count

# # # 超时->太暴力了
## 修改后，勉强
def minMove(n, L):
    count = 0
    while L != sorted(L):
        if max(L) != L[-1:]:
            count = count + 1
        L.remove(max(L))
    return count

n = int(raw_input())
L = map(int, raw_input().split())
print minMove(n, L)