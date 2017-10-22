# def sort(seq):
#     if len(seq) <= 1:
#         return seq
#     else:
#         pivot = seq[0]
#         left, right = [], []
#         for x in seq[1:]:
#             if x < pivot:
#                 left.append(x)
#             else:
#                 right.append(x)
#         return sort(left) + [pivot] + sort(right)

def sort(seq):
    if len(seq) <= 1:
        return seq
    else:
        pivot = seq[0]
        left = sort([x for x in seq[1:] if x < pivot])
        right = sort([x for x in seq[1:] if x >= pivot])
    return left + [pivot] + right
    
if __name__ == '__main__':
    arr = [4, 3, 9, 6, 7, 7]
    print (sort(arr))