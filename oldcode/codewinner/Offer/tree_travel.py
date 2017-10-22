class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

tree = Node(1, Node(3, Node(7, Node(0)), Node(6)), Node(2, Node(5), Node(4)))

def travel_by_level(root):
    stack = [root]
    while stack:
        current = stack.pop(0)
        print current.data
        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)

def travel_by_depth(root):
    if not root:
        return
    print root.data
    travel_by_depth(root.left)
    travel_by_depth(root.right)

if __name__ == '__main__':
    travel_by_level(tree)
    travel_by_depth(tree)