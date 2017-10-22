#!/usr/bin/python

#def count(n):
#    res = [0] * (n+1)
#    if n == 1:
#        res[1] = 2
#    elif n >= 2:
#        res[n] = count(n-1) * 9
#    return res[n]
#
#n = int(raw_input())
#print 10**n - count(n)

import re
import string


def count(s):
    p = re.compile(ur"(\w)(\1+)")
    keys = list(p.sub(ur"\1", s))
    words = list(s)
    result = []
    # print keys, words
    for k in keys:
        n = 0
        # print words
        while len(words) > n and k == words[n]:
            n = n + 1
        words = words[n:]
        result.append((k, n))
        # print result
    return result

#i = 0
#for word in string.lowercase:
#    dic(word) = c[i]
#    i += 0
#
#new_str = 

if __name__ == '__main__':
    s = "abbbcccbba"
    result = count(s)
    print result
    print ''.join(["%s%s" % x for x in result])
    
        	
        
    	