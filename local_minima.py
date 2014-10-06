def local_minima(arr, lo=0, hi=None):
    """Find the local minima in an array of numbers.
    
    Note: assumes elements are distinct.
    """
    if hi is None:
        hi = len(arr) - 1

    if lo == hi:
        return arr[lo]
    elif hi - lo == 1:
        if arr[lo] < arr[hi]:
            return arr[lo]
        else:
            return arr[hi]
    else:
        mid = (hi - lo) // 2
        if ((mid - 1 < 0 or arr[mid] < arr[mid - 1]) and
                (mid + 1 >= len(arr) or arr[mid] < arr[mid + 1])):
            return arr[mid]
        if mid - 1 >= 0 and arr[mid - 1] < arr[mid]:
            hi = mid - 1
            return local_minima(arr, lo, hi)
        if mid + 1 < len(arr) and arr[mid + 1] < arr[mid]:
            lo = mid + 1
            return local_minima(arr, lo, hi)


def main():
    arr = [9, 2, 3, 4, 5]
    print local_minima(arr)


if __name__ == "__main__":
    main()
