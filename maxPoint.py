def maxPoint(N, P):
    result = []
    for i in range(N):
        count = 0
        for v in (P[:i] + P[i+1:]):
            if P[i][0] < v[0] and P[i][1] < v[1]:
                break;
            count = count + 1
            if count == (N - 1):
                result.append(P[i])
    return result


P = []
N = int(raw_input())
for i in range(N):
    point = map(int, raw_input().split())
    P.append(point)
for value in maxPoint(N, P):
    print " ".join(str(i) for i in value)