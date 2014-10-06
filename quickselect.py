import random


def partition(arr, left, right, pivot_index):
    """Partition arr around element at pivot index so that all elements less
    than the pivot are left of the pivot and all elements greater than the
    pivot are right of the pivot."""
    pivot = arr[pivot_index]
    arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
    store_index = left

    for index in xrange(left, right):
        if arr[index] < pivot:
            arr[store_index], arr[index] = arr[index], arr[store_index]
            store_index += 1
    arr[store_index], arr[right] = arr[right], arr[store_index]

    return store_index


def quickselect(arr, k):
    """Find the kth smallest item in an unsorted array arr."""
    left = 0
    right = len(arr) - 1

    while True:
        pivot_index = random.randint(left, right)
        pivot_index = partition(arr, left, right, pivot_index)

        if k == pivot_index:
            return arr[k]
        elif k < pivot_index:
            right = pivot_index - 1
        else:
            left = pivot_index + 1


def main():
    arr = [8, 9, 7, 6, 5, 4, 2, 3, 1]
    print quickselect(arr, 3)


if __name__ == "__main__":
    main()
