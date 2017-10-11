def is_same_tree(p, q):
    if p == None and q == None:
        return True
    elif p and q:
        return p.val == q.val and is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)
    else:
        return False