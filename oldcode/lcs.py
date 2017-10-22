from collections import Counter

def lcs(xstr, ystr):
    if not xstr or not ystr:
        return ""
    x, xs, y, ys = xstr[0], xstr[1:], ystr[0], ystr[1:]
    if x == y:
        return x + lcs(xs, ys)
    else:
        return max(lcs(xstr, ys), lcs(xs, ystr), key=len)
def getY(str):
    

xtr = raw_input()    
ystrs = getY(xtr)
for ystr in lcs:
    res.append(lcs(xstr, ystr))
print Counter(res).most_common(1)[0][1]
