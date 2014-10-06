class lru_cache:
    def __init__(self, capacity):
        """LRU cache constructor."""
        self.capacity = capacity
        self.node_map = {}
        self.head = None
        self.tail = None

    def __push(self, key, value):
        """Push entry to the front of the queue."""
        # Push node onto queue.
        node = Node(key, value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
        self.head = node
        # Map key to node to allow constant access.
        self.node_map[key] = node

    def __pop(self):
        """Pop entry from the back of the queue."""
        if self.head is None:
            raise Exception("Cannot pop empty list!")
        # Make copy of tail node contents.
        node = Node(self.tail.key, self.tail.value)
        # Delete tail node in-place.
        if self.tail.prev is None:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

        return node

    def __getitem__(self, key):
        """Get value associated with key if the key exists in the cache."""
        if key in self.node_map.keys():
            node = self.node_map[key]
            if node == self.head:
                return node.value
            # Delete node in-place.
            if node == self.tail:
                node = self.__pop()
            else:
                node.prev.next = node.next
                node.next.prev = node.prev
            # Push node to the front of the queue.
            self.__push(node.key, node.value)
            return node.value
        else:
            raise KeyError()

    def __setitem__(self, key, value):
        """Map key to value in cache."""
        if key in self.node_map.keys():
            self[key]
            self.head.value = value
        else:
            self.__push(key, value)
            # If we have exceeded capacity, then we need to evict the entry.
            if len(self.node_map.keys()) > self.capacity:
                # Evict the least recently used.
                evicted = self.__pop()
                # Remove the entry from our node map.
                del self.node_map[evicted.key]

    def __contains__(self, item):
        return item in self.node_map.keys()

    def __len__(self):
        return len(self.node_map.keys())


class Node(object):
    """Doubly linked list node class for LRU Cache."""
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None       

    def __eq__(self, other):
        return (isinstance(other, self.__class__)
                and self.__dict__ == other.__dict__)
