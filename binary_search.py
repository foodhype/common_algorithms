from bisect import bisect_left

def binary_search(li, target, lo=0, hi=None):
    hi = hi if hi is not None else len(li)
    pos = bisect_left(li, target, lo, hi)
    return pos if pos != len(li) and li[pos] == target else -1

def main():
    li = [1, 1, 2, 3, 5, 8]
    print li
    print binary_search(li, 3)

if __name__ == "__main__":
  main()
