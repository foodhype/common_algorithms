def combinations(elements, length):
    for index in xrange(len(elements)):
        if length == 1:
            yield (elements[index],)
        else:
            for sub_combination in combinations(elements[index + 1:], length - 1):
                yield (elements[index],) + sub_combination


def main():
    arr = [1, 2, 3, 4]
    print list(combinations(arr, 3))


if __name__ == "__main__":
    main()
