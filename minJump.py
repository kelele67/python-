def dp(start, end):
    divs=[[] for _ in range(end+1)]  # 求因数
    for i in range(2,end+1):
        for j in range(i+i,end+1,i):
            divs[j].append(i)
 
    l = end-start+1
    res = [float("inf")] * l
    res[0] = 0
 
    for i, x in enumerate(res):
        if i==l-1:
            break
        if x != float("inf"):
            steps = divs[i+start]
 
            for step in steps:
                if step+i < l:
                    res[step+i] = min(res[step+i], x+1)
                else:
                    break
    return res[l-1] if res[l-1]!=float("inf") else -1
n, m = map(int, raw_input().strip().split())
print dp(n, m)