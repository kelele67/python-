# -*- coding:utf-8 -*-
#最小里面又要最大->尽量平均
#怎么做到平均->首先划分的时候均分-> 是3+1的倍数的时候(间隔是3的倍数)->均分
#->不是3+1的倍数的时候
#->算了，还是不要先想着归类总结，直接暴力点->
#->找出所有的分区情况->算出所有的大小->每种情况都得到一个最小值->最小值最大的那一个就是我们要的
#->发现题目说了是16份...->那这样的话横竖三刀都必须切进来->还是太粗心了。。。最关键的都没看见

def findMaxValue(n, m, list):
    sums = []
    result = []
    # 可能要计算的范围有 n/4, n/4 + 1, ... , n/4 + n%4
    for i in range(1, n/4+n%4):
        for j in range(1, m/4+m%4):
            for k in range(n/4, n/4+n%4+1):
                for l in range(m/4, m/4+m%4+1):
                    sums.append(list[i:i+k][j:j+l])
            
            result.append(min(sums))
    return max(result)

all = []
n, m = map(int, (raw_input().split()))
for i in range(0, n):
    row = map(int, list(raw_input()))
    all.append(row)
print findMaxValue(n, m, all)
