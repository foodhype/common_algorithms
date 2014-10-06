def inorder_traversal(root):
    """Generate values in binary tree in-order."""
    if root is not None:
        for val in inorder_traversal(root.left):
            yield val
        yield root.val
        for val in inorder_traversal(root.right):
            yield val


def preorder_traversal(root):
    """Generate values in binary tree pre-order."""
    if root is not None:
        yield root.val
        for val in preorder_traversal(root.left):
            yield val
        for val in preorder_traversal(root.right):
            yield val


def postorder_traversal(root):
    """Generate values in binary tree post-order."""
    if root is not None:
        for val in postorder_traversal(root.left):
            yield val
        for val in postorder_traversal(root.right):
            yield val
        yield root.val
