def rebuild_tree(pre, inorder):
    if not pre:
        return
    cur = Node(pre[0])
    index = inorder.index(pre[0])
    cur.left = rebuild_tree(pre[1:index+1], inorder[:index])
    cur.right = rebuild_tree(pre[index+1:], inorder[index+1:])
    return cur