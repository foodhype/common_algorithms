from BinaryTreeNode import BinaryTreeNode


class BSTIterator(object):
    def __init__(self, root):
        self.stack = []
        # Process the leftmost node first, since it is the smallest,
        # and keep track of its parent, since its parent may be next.
        while root is not None:
            self.stack.append(root)
            root = root.left

    def hasNext(self):
        return len(self.stack) > 0

    def next(self):
        # node is the leftmost node that hasn't been processed.
        cur = self.stack.pop()
        val = cur.val

        # If cur has a right node, then the leftmost node in cur's right
        # subtree is next. Otherwise, the cur's parent is next.
        if cur.right is not None:
            cur = cur.right
            while cur is not None:
                self.stack.append(cur)
                cur = cur.left

        return val


def main():
    root = BinaryTreeNode(5)
    root.left = BinaryTreeNode(3)
    root.right = BinaryTreeNode(8)
    root.left.left = BinaryTreeNode(1)
    root.left.right = BinaryTreeNode(4)

    it = BSTIterator(root)
    result = []
    while it.hasNext():
        result.append(it.next())
    assert result == [1, 3, 4, 5, 8]


if __name__ == "__main__":
    main()
