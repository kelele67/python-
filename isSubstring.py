def isSubstring():
    s = list(raw_input())
    t = list(raw_input())
    if t != '':
        for value in t:
            if value in s:
                s = s[s.index(value)+1:]
            else:
                return False
    return True

if isSubstring():
    print "Yes"
else:
    print "No"
