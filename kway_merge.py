import heapq

def kway_merge(*iterables):
    input_buffer = []
    iterators = [iter(iterable) for iterable in iterables]
    for index, iterable in enumerate(iterators):
        heapq.heappush(input_buffer, (iterable.next(), index))

    while input_buffer:
        value, index = heapq.heappop(input_buffer)
        yield value
        next_value = iterators[index].next()
        if next_value is not None:
            heapq.heappush(input_buffer, (next_value, index))


def main():
    a = [1, 5, 9, 13]
    b = [2, 6, 10, 14]
    c = [1, 1, 2, 3, 5, 8, 13]
    args = [a, b, c]

    print a
    print b
    print c
    print list(kway_merge(*args))


if __name__ == "__main__":
    main()
