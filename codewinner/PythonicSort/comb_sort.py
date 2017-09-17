"""
Improves on bubble sort by using a gap sequence to remove turtles.
http://en.wikipedia.org/wiki/Comb_sort
"""

def sort(seq):
    gap = len(seq)
    swap = True

    while gap > 1 or swap:
        gap = max(1, int(gap / 1.25))
        swap = False
        for i in range(len(seq) - gap):
            if seq[i] > seq[i + gap]:
                seq[i], seq[i + gap] = seq[i + gap], seq[i]
                swap = True
    return seq

if __name__ == '__main__':
    arr = [4, 3, 9, 6, 7, 7]
    print (sort(arr))
