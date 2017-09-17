def sort(seq):
    for i in range(0, len(seq)):
        iMin = i
        for j in range(i+1, len(seq)):
            if seq[iMin] > seq[j]:
                iMin = j
        if i != iMin:
            seq[i], seq[iMin] = seq[iMin], seq[i]

    return seq

if __name__ == '__main__':
    arr = [4, 3, 9, 6, 7, 7]
    print (sort(arr))