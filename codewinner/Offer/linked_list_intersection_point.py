class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def node(l1, l2):
    len1, len2 = 0, 0
    # get len1, len2
    while l1.next:
        l1 = l1.next
        len1 += 1
    while l2.next:
        l2 = l2.next
        len2 += 1
    # long linkedlist first go
    if len1 > len2:
        for _ in range(len1 - len2):
            l1 = l1.next
    else:
        for _ in range(len2 - len1):
            l2 = l2.next
    while l1 and l2:
        if l1.next == l2.next:
            return l1.next
        else:
            l1 = l1.next
            l2 = l2.next

            