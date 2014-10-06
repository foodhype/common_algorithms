import random


def getbit(num, index):
    return (num >> index) & 1


def msd(arr):
    return max(num.bit_length() for num in arr)


def radixsort(arr, algorithm):
    if algorithm == "msd":
        msd_radixsort(arr, 0, len(arr), msd(arr) - 1)
    elif algorithm == "lsd":
        lsd_radixsort(arr)
    else:
        print "invalid algorithm"


def msd_radixsort(arr, lo, hi, bit_index):
    left_bound = lo
    right_bound = hi
    while left_bound < right_bound:
        bit = getbit(arr[left_bound], bit_index)
        if bit == 0:
            left_bound += 1
        else:
            arr[left_bound], arr[right_bound - 1] = arr[right_bound - 1], arr[left_bound]
            right_bound -= 1

    if bit_index > 0:
        msd_radixsort(arr, lo, left_bound, bit_index - 1)
        msd_radixsort(arr, left_bound, hi, bit_index - 1)


def lsd_radixsort(arr):
    for bit_index in xrange(msd(arr)):
        arr = [number for number in merge(arr, bit_index)]


def merge(iterable, bit_index):
    for bucket in (0, 1):
        for number in iterable:
            bit = getbit(number, bit_index)
            if bit == bucket:
                yield number


def main():
    random.seed(12345)
    arr = random.sample(xrange(100), 21)
    radixsort(arr, "lsd")


if __name__ == "__main__":
    main()
