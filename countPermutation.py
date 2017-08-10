def countPermutation(N, k):
    cur = [0]*N
    for i in range(1, N+1):
        cur[i-1] = 1
        for j in range(i-2, 0, -1):
                cur[j] = (cur[j]*(j+1) + cur[j-1]*(i-j)) % 2017
    return cur[k]

N, k = map(int, raw_input().split())
print countPermutation(N, k)