def is_palindrome(n):
    s = str(n)
    for i in xrange(len(s) // 2):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True
