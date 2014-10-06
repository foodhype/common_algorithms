import random


def partition(arr, left, right, pivot_index):
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
