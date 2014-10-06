from collections import OrderedDict


class lru_cache(object):
    def __init__(self, capacity):
        """LRU cache constructor."""
        self.capacity = capacity
        self.cache = OrderedDict()

    def __getitem__(self, key):
        """Get value associated with key if the key exists in the cache."""
        value = self.cache[key]
        del self.cache[key]
        self.cache[key] = value

        return value

    def __setitem__(self, key, value):
        """Map key to value in cache."""
        if key in self.cache:
            self[key]
            self.cache[key] = value
        else:
            self.cache[key] = value
            if len(self.cache.keys()) > self.capacity:
                self.cache.popitem(False)

    def __contains__(self, item):
        return item in self.cache.keys()
