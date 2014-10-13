class ArrayQueue(object):
    """Array implementation of FIFO queue."""

    # Still buggy; don't use.

    def __init__(self):
        self.capacity = 8
        self.queue = [None for _ in xrange(self.capacity)]
        self.front = 0
        self.back = 0
        self.size = 0

    def inorder(self):
        index = self.front
        if self.front <= self.back:
            while index < self.back:
                yield self.queue[index]
                index = (index + 1) % self.capacity
        else:
            while index < self.size:
                yield self.queue[index]
                index = (index + 1) % self.capacity
            index = 0
            while index < self.back:
                yield self.queue[index]
                index = (index + 1) % self.capacity

    def push(self, val):
        if self.size >= 3 * self.capacity // 4:
            temp = [None for _ in xrange(self.capacity * 2)]

            index = 0
            for elem in self.inorder():
                temp[index] = elem
                index += 1
            temp[index] = val

            self.queue = temp
            self.capacity *= 2
            self.front = 0
            self.back = self.size
        else:
            self.queue[self.back] = val
            self.back = (self.back + 1) % self.capacity

        self.size += 1

    def pop(self):
        if self.size == 0:
            raise Exception("Empty: Cannot pop.")
        elif self.size <= self.capacity // 4:
            print self.queue
            temp = [None for _ in xrange(self.capacity // 2)]

            for index, elem in enumerate(self.inorder()):
                temp[index] = elem

            self.queue = temp
            self.capacity //= 2
            self.front = 0
            self.back = self.size
            self.size -= 1
            return self.queue[self.front]
        else:
            popped = self.queue[self.front]
            self.front = (self.front + 1) % self.capacity
            self.size -= 1
            return popped


def main():
    queue = ArrayQueue()
    for i in xrange(32):
        queue.push(i)

    for i in xrange(32):
        queue.pop()

    for i, elem in enumerate(queue.inorder()):
        print elem

main()            
