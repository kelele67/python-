def longestA(arr, K, N):
    start, end = [-1] * K, [-1] * K
    start[0] = end[0] = s = e = n = m = 0

    for i in range(N):
        m = (m + arr[i]) % K
        end[m] = i+1
        if start[m] < 0:
            start[m] = i+1
        if end[m] - start[m] > e - s:
            s, e, n = start[m], end[m], m
    return e-s

N = int(raw_input())
arr = map(int, raw_input().split())
K = int(raw_input())
print longestA(arr, K, N)