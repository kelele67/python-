def isPalindrome(str):
    for i in range(0, len(str)/2):
        if str[i] == str[len(str)-1-i]:
            continue
        else:
            return False
    return True

def palindromeCount(str, insert_str):
    count = 0
    for i in range(0, len(str)+1):
        new_str = ''
        new_str = str[:i] + insert_str + str[i:]
        if isPalindrome(new_str):
            count = count + 1
    return count
    
str = raw_input()
insert_str = raw_input()
print palindromeCount(str, insert_str)