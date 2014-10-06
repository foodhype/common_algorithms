def kmp(pattern, text):
    """Return all indexes where pattern occurs in text (Knuth-Morris-Pratt
    algorithm for O(N) substring search)."""
    shifts = [None] * (len(pattern) + 1)
    shift = 1
    for i in range(len(pattern) + 1):
        while shift < i and pattern[i - 1] != pattern[i - shift - 1]:
            shift += shifts[i - shift - 1]
        shifts[i] = shift

    start = 0
    match_len = 0
    for c in text:
        while match_len >= 0 and pattern[match_len] != c:
            start += shifts[match_len]
            match_len -= shifts[match_len]
        match_len += 1
        if match_len == len(pattern):
            yield start
            start += shifts[match_len]
            match_len -= shifts[match_len]
