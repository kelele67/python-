import random

def sort(seq):
    if len(seq) == 1:
        return seq
    random.seed()
    while not is_sorted(seq):
        if len(seq) == 2:
            i = 0
            j = 1
        else:
            i = random.randint(0, len(seq) - 2)
            j = random.randint(i, len(seq) - 1)
        seq[i], seq[j] = seq[j], seq[i]
    return seq

def is_sorted(seq):
    return all(seq[i - 1] <= seq[i] for i in range(1, len(seq)))

if __name__ == '__main__':
    arr = [4, 3, 9, 6, 7, 7]
    print (sort(arr))