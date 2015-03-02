class lru_cache:
    def __init__(self, capacity):
        """LRU cache constructor."""
        self.capacity = capacity
        self.node_map = {}
        self.head = None
        self.tail = None

    def __getitem__(self, key):
        """Get value associated with key if the key exists in the cache."""
        if key in self.node_map.keys():
            if key == self.head.key:
                return self.head.value
            node = self.node_map[key]

            # Delete node in-place.
            if node.key == self.tail.key:
                node = self.pop()
            else:
                node.prev.next = node.next
                node.next.prev = node.prev

            # Push node to the front of the queue.
            self.push(node)
            return node.value
        else:
            raise KeyError("Key not found: %s" % (str(key)))

    def __setitem__(self, key, value):
        """Map key to value in cache."""
        if key in self.node_map.keys():
            self[key]
            self.head.value = value
        else:
            self.push(Node(key, value))

            # If we have exceeded capacity, then we need to evict the entry.
            if len(self.node_map.keys()) > self.capacity:
                # Remove the entry from our node map.
                del self.node_map[self.tail.key]
                # Evict the least recently used.
                self.pop()

    def push(self, node):
        """Push entry to the front of the queue."""
        if self.head is None:
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
        self.head = node

        # Map key to node to allow constant access.
        self.node_map[node.key] = node

    def pop(self):
        """Pop entry from the back of the queue."""
        if self.head is None:
            raise Exception("Cannot pop empty list!")

        popped = self.tail

        # Delete tail node in-place.
        if self.tail.prev is None:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

        return popped

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
