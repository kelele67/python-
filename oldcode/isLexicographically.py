def isLexicographically(str_list, n):
    for i in range(0, n-1):
        if str_list[i] < str_list[i+1]:
             continue
        else:
            return False
    return True

def isLength(str_list, n):
    for i in range(0, n-1):
        if len(str_list[i]) < len(str_list[i+1]):
            continue
        else:
            return False
    return True
    
def judge(str_list, n):
    if isLexicographically(str_list, n) and isLength(str_list, n):
        return "both"
    if isLexicographically(str_list, n) and not isLength(str_list, n):
        return "lexicographically"
    if not isLexicographically(str_list, n) and isLength(str_list, n):
        return "lengths"
    if not isLexicographically(str_list, n) and not isLength(str_list, n):
        return "none"
    
str_list = []
n = int(raw_input())
for i in range(n):
    str = raw_input()
    str_list.append(str)
print judge(str_list, n)