def minOperator(str1, str2):
    count = 0
    while str1 != str2:
        if len(str1) == len(str2):
            for i in range(len(str1)):
                if str1[i] != str2[i]:
                    count = count + 1
        elif len(str1) < len(str2):
            for i in range(len(str1)):
                if str1[i] != str2[i]:
                    str1 = str1[:i] + str2[i] + str1[i:]
                    count = count + 1
        elif len(str1) > len(str2):
            for i in range(len(str2)):
                if str1[i] != str2[i]:
                    str1.replace(str1[i], '')
                    count = count + 1
    return count

str1, str2 = raw_input().split()
print minOperator(str1, str2)

