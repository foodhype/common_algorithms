# Note: fails two edge cases: dynamic resizing and capacity bounds checking.
# Do not use.

class ArrayQueue(object):
    """Array implementation of FIFO queue."""

    def __init__(self, capacity):
        self.queue = [None for _ in xrange(capacity)]
        self.front = 0
        self.back = 0
        self.capacity = capacity
        self.size = 0

    def push(self, val):
        self.queue[self.back] = val
        self.back = (self.back + 1) % self.capacity
        self.size += 1

    def pop(self):
        if self.size == 0:
            raise Exception("Empty: Cannot pop.")
        else:
            popped = self.queue[self.front]
            self.front = (self.front + 1) % self.capacity
            self.size -= 1
            return popped


def main():
    queue = ArrayQueue(5)
    for i in xrange(5):
        queue.push(i)

    assert queue.pop() == 0
    assert queue.pop() == 1

    queue.push(10)
    queue.push(11)

    assert queue.pop() == 2
    assert queue.pop() == 3
    assert queue.pop() == 4
    assert queue.pop() == 10
    assert queue.pop() == 11


main()            
