def longest_palindrome_substring(s):
    if len(s) == 0:
        return ""

    start = 0
    max_len = 1

    index = 1
    while index < len(s):
        left = index - 1
        right = index + 1

        while left >= 0 and right < len(s) and s[left] == s[right]:
            if right - left + 1 > max_len:
                start = left
                max_len = right - left + 1
            left -= 1
            right += 1

        index = right + 1

    index = 0
    while index + 1 < len(s):
        left = index
        right = index + 1

        while left >= 0 and right < len(s) and s[left] == s[right]:
            if right - left + 1 > max_len:
                start = left
                max_len = right - left + 1
            left -= 1
            right += 1

        index = right + 1

    return s[start:start + max_len]

assert longest_palindrome_substring("alcatrazracecarmaxipad") == "racecar"
assert longest_palindrome_substring("") == ""
assert longest_palindrome_substring("racecar") == "racecar"
assert longest_palindrome_substring("abbbbabba") == "abbbba"
