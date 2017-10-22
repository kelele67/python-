def sort(seq):
    L = len(seq)
    for i in range(L):
        for j in range(1, L - i):
            if seq[j] < seq[j - 1]:
                seq[j - 1], seq[j] = seq[j], seq[j - 1]
    return seq

if __name__ == '__main__':
    arr = [4, 3, 9, 6, 7, 7]
    print (sort(arr))