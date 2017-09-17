from random import randrange

def partition(seq, left, right, pivot_index):
    pivot_value = seq[pivot_index]
    seq[pivot_index], seq[right] = seq[right], seq[pivot_index]
    store_index = left
    for i in range(left, right):
        if seq[i] < pivot_value:
            seq[i], seq[store_index] = seq[store_index], seq[i]
            store_index += 1
    seq[store_index], seq[right] = seq[right], seq[store_index]
    return store_index

def sort(seq, left, right):
    if len(seq) <= 1:
        return seq
    elif left < right:
        # pivot = randrange(left, right)
        pivot = seq[0]
        pivot_new_index = partition(seq, left, right, pivot)
        sort(seq, left, pivot_new_index - 1)
        sort(seq, pivot_new_index + 1, right)
        return seq

if __name__ == '__main__':
    arr = [4, 3, 9, 6, 7, 7]
    print (sort(arr, 0, 5))