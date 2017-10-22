# def evaluate():
#     N = int(raw_input())
#     count = 0
#     for i in range(N):
#         x, y = raw_input().split()
#         if x == y:
#             count = count + 1
#     print ("%.2f%%") %(100* float(count)/N)

# evaluate()

# while True:
#     try:
#         count = 0
#         N = int(raw_input())
#         for i in range(N):
#             x, y = raw_input().split()
#             if x == y:
#                 count = count + 1
#         print ("%.2f%%") %(100* count/float(N))
#     except EOFError:
#         break

def evaluate():
    N = int(raw_input())
    count = 0
    for i in range(N):
        x, y = raw_input().split()
        if x == y:
            count = count + 1
    p = (count/float(N)) * 100
    return ("%.2f%%") %(p)
while True:
    try:
        print evaluate()
    except EOFError:
        break
