class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        # string representation
        return self.val


def deepest(node):
    # Fill this in
    if node and not node.left and not node.right:
        return node, 1  # if there is no leafs return node itself and it depths which is 1
    if not node.left:
        return increment_depth(deepest(node.right))
    elif not node.right:
        return increment_depth(deepest(node.left))
    return increment_depth(max(deepest(node.left), deepest(node.right), key=lambda x: x[1]))


def increment_depth(node_depths_tuple):
    node, depth = node_depths_tuple
    return node, depth + 1


if __name__ == "__main__":
    root = Node('a')
    root.left = Node('b')
    root.left.left = Node('d')
    root.right = Node('c')

    print(deepest(root))
