import heapq

def running_median(arr):
    """Generate median for each element encountered so far in arr iterating
    from left to right."""
    max_heap = []
    min_heap = []
    median_upto = []
    for index, number in enumerate(arr):
        if len(max_heap) == 0 or number < max_heap[0][1]:
            heapq.heappush(max_heap, ((1.0 / number), number))
        else:
            heapq.heappush(min_heap, number)
        while len(max_heap) - len(min_heap) > 1:
            temp = heapq.heappop(max_heap)[1]
            heapq.heappush(min_heap, temp)
        while len(min_heap) - len(max_heap) >= 1:
            temp = heapq.heappop(min_heap)
            heapq.heappush(max_heap, ((1.0 / temp), temp))

        median_upto.append(max_heap[0][1])

    return median_upto

def main():
    arr = [2, 1, 4, 1, 3, 9, 5, 10, 4, 10]
    print arr
    print running_median(arr)


if __name__ == "__main__":
    main()
