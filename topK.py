# import heapq

# def topK(arr, k):
#     heap=arr[:k]
#     heapq._heapify_max(heap)
#     for i in range(k, len(arr)):
#         if arr[i] < heap[0]:
#             heap[0] = arr[i]
#             heapq._heapify_max(heap)
#     return heap[0]


# arr = map(int, raw_input().split())
# k = int(raw_input())
# arr.sort()
# print arr[k-1]

def partition(alist, start, end):
    if end <= start:
        return
    base = alist[start]
    index1, index2 = start, end
    while start < end:
        while start < end and alist[end] >= base:
            end -= 1
        alist[start] = alist[end]
        while start < end and alist[start] <= base:
            start += 1
        alist[end] = alist[start]
    alist[start] = base
    partition(alist, index1, start - 1)
    partition(alist, start + 1, index2)

def find_least_k_nums(alist, k):
    length = len(alist)
    if not alist or k <= 0 or k > length:
        return None
    start = 0
    end = length - 1
    partition(alist, start, end)
    return alist[:k]


def partition(alist, start, end):
    if end <= start:
        return
    base = alist[start]
    index1, index2 = start, end
    while start < end:
        while start < end and alist[end] >= base:
            end -= 1
        while start < end and alist[start] <= base:
            start += 1
        alist[end] = alist[start]
    alist[start] = base
    return start

def find_least_k_nums(alist, k):
    length = len(alist)
    if not alist or k <= 0 or k > length:
        return None
    start = 0
    end = length - 1
    index = partition(alist, start, end)
    while index != k:
        if index > k:
            index = partition(alist, start, index - 1)
        elif index < k:
            index = partition(alist, index + 1, end)
    return alist[:k]

# 至于容器的选择，很多人第一反应便是最大堆，但是python中最大堆如何实现呢？我们可以借助实现了最小堆的heapq库，因为在一个数组中，每个数取反，
# 则最大数变成了最小数，整个数字的顺序发生了变化，所以可以给数组的每个数字取反，然后借助最小堆，最后返回结果的时候再取反就可以了

import heapq
def get_least_numbers_big_data(self, alist, k):
    max_heap = []
    length = len(alist)
    if not alist or k <= 0 or k < length:
        return
    k = k - 1
    for ele in alist:
        ele = -ele
        if len(max_heap) <= k:
            heapq.heapqush(max_heap, ele)
        else:
            heapq.headppushpop(max_heap, ele)

    return map(lambda x: -x, max_heap)

