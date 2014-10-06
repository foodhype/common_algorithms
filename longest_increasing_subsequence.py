import bisect


def len_longest_increasing_subsequence(arr):
    """Get the length of the longest increasing subsequence in O(N^2)."""
    lis_ending_here = [1 for _ in xrange(len(arr))]
    for i in xrange(len(arr)):
        max_so_far = 0
        for j in xrange(i):
            if arr[j] < arr[i]:
                max_so_far = max(max_so_far, lis_ending_here[j] + 1)
            lis_ending_here[i] = max_so_far

    return max(lis_ending_here)


def longest_increasing_subsequence(arr):
    """Get the longest increasing subsequence in O(N^2)."""
    lis_ending_here = [1 for _ in xrange(len(arr))]
    prev = [-1 for i in xrange(len(arr))]
    for i in xrange(len(arr)):
        max_so_far = 0
        best_end = -1
        for j in xrange(i):
            if arr[j] < arr[i] and lis_ending_here[j] + 1 > max_so_far:
                max_so_far = lis_ending_here[j] + 1
                best_end = j
            lis_ending_here[i] = max_so_far
            prev[i] = best_end

    max_len = max(lis_ending_here)
    max_len_index = lis_ending_here.index(max_len)
    lis = [arr[max_len_index]]

    for _ in xrange(max_len - 1):
        prev_index = prev[max_len_index]
        lis.append(arr[prev_index])
        max_len_index = prev_index

    lis.reverse()

    return lis


def fast_len_longest_increasing_subsequence(arr):
    """Get length of the longest increasing subsequence in O(N*log(N))."""
    lis_ending_here = [1 for _ in xrange(len(arr))]
    min_end_of_lis_with_length = [float("inf") for _ in xrange(len(arr) + 1)]
    min_end_of_lis_with_length[1] = arr[0]
    max_len = 1

    for i in xrange(1, len(arr)):
        if arr[i] < min_end_of_lis_with_length[1]:
            min_end_of_lis_with_length[1] = arr[i]
            lis_ending_here[i] = 1
        elif arr[i] > min_end_of_lis_with_length[max_len]:
            min_end_of_lis_with_length[max_len + 1] = arr[i]
            lis_ending_here[i] = max_len + 1
            max_len += 1
        else:
            best_end = bisect.bisect_left(min_end_of_lis_with_length, arr[i], hi=max_len)
            min_end_of_lis_with_length[best_end] = arr[i]
            lis_ending_here[i] = best_end

    return max(lis_ending_here)


def main():
    arr = [1, 3, 1, 2, 99, 3, 5, 8, 13]
    print fast_len_longest_increasing_subsequence(arr)


if __name__ == "__main__":
    main()
