def sort(seq):
    for i in range(1, len(seq)):
        item = seq[i]
        hole = i
        while hole > 0 and seq[hole - 1] > item:
            seq[hole] = seq[hole - 1]
            hole = hole - 1
        seq[hole] = item
    return seq

if __name__ == '__main__':
    arr = [4, 3, 9, 6, 7, 7]
    print (sort(arr))