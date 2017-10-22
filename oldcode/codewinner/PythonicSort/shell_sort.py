def sort(seq):
    # get gaps
    gaps = [x for x in range(len(seq)//2, 0, -1)]

    for gap in gaps:
        for i in range(gap, len(seq)):
            temp = seq[i]
            j = i
            while j >= gap and seq[j - gap] > temp:
                seq[j] = seq[j - gap]
                j -= gap
            seq[j] = temp

    return seq

if __name__ == '__main__':
    arr = [4, 3, 9, 6, 7, 7]
    print (sort(arr))