import random


def partition(arr, lo, hi, pivot_index):
    pivot = arr[pivot_index]
    arr[pivot_index], arr[hi] = arr[hi], arr[pivot_index]
    store_index = lo

    for index in xrange(lo, hi):
        if arr[index] < pivot:
            arr[index], arr[store_index] = arr[store_index], arr[index]
            store_index += 1
            
    arr[store_index], arr[hi] = arr[hi], arr[store_index]

    return store_index


def quicksort(arr, lo, hi):
    if lo < hi:
        pivot_index = random.randint(lo, hi)
        pivot_index = partition(arr, lo, hi, pivot_index)
        quicksort(arr, lo, pivot_index)
        quicksort(arr, pivot_index + 1, hi)


def main():
    random.seed(12345)
    numbers = random.sample(xrange(1, 500), 20)
    print numbers
    quicksort(numbers, 0, len(numbers) - 1)
    print numbers


if __name__ == "__main__":
    main()
