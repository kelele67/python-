
def binary_search_1(arr, l, r, v):
    while (l <= r):
        mid = l + (r - l) / 2
        if arr[mid] == v:
            return mid
        elif arr[mid] > v:
            r = mid - 1
        else:
            l = mid + 1
    return -1

def binary_search_2(arr, l, r, v):
    if (l <= r):
        mid = l + (r - l) / 2
        if arr[mid] == v:
            return mid
        elif arr[mid] > v:
            return binary_search_2(arr, l, mid - 1, v)
        else:
            return binary_search_2(arr, mid + 1, r, v)
    return -1
    