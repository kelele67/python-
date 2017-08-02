def reverse(str):
    str = str[::-1]
    for s in str:
        if s == '0':
            str = str.replace(s, '')
        else:
            break
    return str

def revCount(x, y):
    return reverse(str(int(reverse(x)) + int(reverse(y))))

x, y = raw_input().split()
print revCount(x, y)
