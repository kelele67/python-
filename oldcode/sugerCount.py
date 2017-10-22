def sugerCount(a, b, c, d):
    if a+b == c-d:
        A = (a + c) / 2
        B = (c + d) / 2
        C = A - (a + b)
        print "%d %d %d" %(A, B, C)
    else:
        print "No"

a, b, c, d = map(int, raw_input().split())
sugerCount(a, b, c, d)