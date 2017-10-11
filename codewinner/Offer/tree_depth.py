def tree_depth(root):
    if not root:
        return 0
    return max(tree_depth(root.left), tree_depth(root.right)) + 1
    