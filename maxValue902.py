import collections

def maxValue(n, v):
    maxV = 0
    age = 1
    d = collections.deque(v)
    while d:
        if d[0] < d[-1]:
            maxV += d[0] * age
            age += 1
            d.popleft()
        elif d[0] > d[-1]:
            maxV += d[-1] * age
            age += 1
            d.pop()
        else:
    # while d:
            for i in range(0, len(d)/2):
                if d[0+i] < d[len(d)-1-i]:
                    maxV += d[0] * age
                    age += 1
                    d.popleft()
                elif d[i] > d[len(d)-1-i]:
                    maxV += d[-1] * age
                    d.pop()
                else:
                    
    return maxV

n = int(raw_input())
v = []
for i in range(n):
    v.append(int(raw_input()))
print maxValue(n, v)