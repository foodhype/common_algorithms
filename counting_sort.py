def counting_sort(arr):
    count = [0 for _ in xrange(max(arr) + 1)]
    for num in arr:
        count[num] += 1

    total = 0
    for index, num in enumerate(count):
        count[index] = total
        total += num

    output = [0 for _ in xrange(len(arr))]
    for num in arr:
        output[count[num]] = num
        count[num] += 1

    return output


def main():
    arr = [6, 4, 5, 1, 2, 1, 6, 6, 8, 10]
    print arr
    print counting_sort(arr)


if __name__ == "__main__":
    main()
