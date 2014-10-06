"""Heap Sort implentation."""

def heapsort(arr):
    for start in reversed(xrange(len(arr) // 2)):
        sift_down(arr, start, len(arr) - 1)
    for end in reversed(xrange(1, len(arr))):
        arr[0], arr[end] = arr[end], arr[0]
        sift_down(arr, 0, end - 1)

    return arr


def sift_down(arr, start, end):
    root = start

    while True:
        # Get index of the left child.
        child = root * 2 + 1
        # If root has no children, we are done.
        if child > end:
            break
        # Get index of the greater child.
        if child + 1 <= end and arr[child] < arr[child + 1]:
            child += 1
        # If root is less than its greater child, swap them and move root down.
        # Otherwise, we are done.
        if arr[root] < arr[child]:
            arr[root], arr[child] = arr[child], arr[root]
            root = child
        else:
            break


def main():
    arr = [5, 1, 3, 4, 10, -1, -6, 3, 9]
    print arr
    print heapsort(arr)


if __name__ == "__main__":
    main()
