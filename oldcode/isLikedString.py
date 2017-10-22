def isLikedString(str):
    for s in str:
        if not s.isupper():
            return False
    for i in range(len(str)-1):
        if str[i] == str[i+1]:
            return False
    if isXyxy(str):
        return False
    return True
    
def isXyxy(str):
    for i in range(1, len(str)+1):
        for s in str:
            if str[:i].count(s) != 0:
                for s in str[i:str.index(s)]:
                    if str[:str.index(s)].count(s) != 0:
                        return True
    return False
    
str = raw_input()
if isLikedString(str):
    print "Likes"
else:
    print "Dislikes"