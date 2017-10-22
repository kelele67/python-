def minStep():
    dp = [-1 for x in range(M * 3 / 2)]
    T = [[] for x in range(M)]
    dp[M] = 0
    i = (M - 1) / 2
    while i > 1:
        j = i * 2
        while j < M:
            T[j].append(i)
            j += i
        i -= 1
    i = M - 1
    while i >= N:
        for k in T[i]:
            v = dp[i + k] + 1
            if v == 0:
                continue
            if dp[i] == -1:
                dp[i] = v
            elif v < dp[i]:
                dp[i] = v
        i -= 1
    return dp[N]
   
while True:
    try:
        N, M = map(int, raw_input().split())
        print minStep()
    except EOFError:
        break