def getIndex(s):
    v=[]
    for i in range(3,-1,-1):
        v.append(25**i)
    index=0
    for i in range(len(s)):
        temp=ord(s[i])-97
        index=index+(temp)*(sum(v[i:4]))
    index+=i
    return index

s=raw_input()
print getIndex(s)