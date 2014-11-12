from collections import deque


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


def levelorder_traversal(root):
    """Generate values in binary tree in level-order."""

    # Note: count is only used if you need to do something special at each
    # level (e.g. yield a new line, etc).
    count = 0
    queue = deque()

    queue.append(root)
    count += 1
    while queue:
        current = queue.popleft()
        yield current.val
        count -= 1

        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)

        if count == 0:
            # We are at next level
            # Do somethiing useful
            count = len(queue)
