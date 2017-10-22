#!/usr/bin/python

import re
import string

s = raw_input()
def count(s):
    p = re.compile(ur"(\w)(\1+)")
    keys = list(p.sub(ur"\1", s))
    words = list(s)
    result = []
    for k in keys:
        n = 0
        while len(words) > n and k == words[n]:
            n = n + 1
        words = words[n:]
        result.append((k, n))
    return result

result = count(s)
old_s = ''.join(["%s%s" % x for x in result])

c = map(int, raw_input().split())
dic = {}
i = 0
for word in string.lowercase:
    dic[word] = c[i]
    i += 1

#new_s = ""
#for (k, v) in dic.items():
#    new_s += k + str(v)

for i in range(len(old_s)):
    if 
    