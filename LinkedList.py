class SinglyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, val):
        """Append a node storing val to the tail of the list."""
        node = Node(val)
        if self.head is None:
            self.head = node
            self.tail = self.head
        else:
            self.tail.next = node
            self.tail = node


class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
