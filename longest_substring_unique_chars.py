def longest_substring_unique_chars(s):
    """Find the longest substring of s without repeating characters."""
    if len(s) == 0:
        return ""

    end = 1
    max_len = 1
    cur_len = 1
    visited = [None for _ in xrange(256)]
    visited[ord(s[0])] = 0

    for index in xrange(1, len(s)):
        prev_index = visited[ord(s[index])]
        if prev_index is None or index - cur_len > prev_index:
            cur_len += 1
        else:
            if cur_len > max_len:
                max_len = cur_len
                end = index + 1
            cur_len = index - prev_index

        visited[ord(s[index])] = index

    if cur_len > max_len:
        max_len = cur_len
        end = len(s)

    return s[end - max_len:end]


def main():
    result = longest_substring_unique_chars("ABDEFGABEF")
    assert result == "BDEFGA" or result == "DEFGAB"
    result = longest_substring_unique_chars("GEEKSFORGEEKS")
    assert result == "EKSFORG" or result == "KSFORGE"
    assert longest_substring_unique_chars("BBBB") == "B"
    assert longest_substring_unique_chars("") == ""
    assert longest_substring_unique_chars("A") == "A"


if __name__ == "__main__":
    main()
