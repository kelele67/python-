def sort(seq):
    for i in range(1, len(seq)):
        item = seq[i]
        hole = i
        while hole > 0 and seq[hole - 1] > item:
            seq[hole] = seq[hole - 1]
            hole = hole - 1
        seq[hole] = item
        print seq
    return seq

if __name__ == '__main__':
    arr = [23, 14, 50, 67, 41, 86, 60, 77, 21]
    print sort(arr)

def insert_sort(seq):
    n = len(seq)
    for i in range(1, n):
        temp = seq[i]
        j = i
        while j > 0 and seq[j-1] > temp:
            arr[j] = arr[j-1]
            j -= 1
        seq[j] = temp
    return seq