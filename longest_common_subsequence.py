def lcs(a, b):
    """Find the length of the longest common subsequence of strings a and b."""
    dp = [[0 for j in xrange(len(b) + 1)] for i in xrange(len(a) + 1)]
    for i in xrange(1, len(a) + 1):
        for j in xrange(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[len(a)][len(b)]


def lcsk(a, b, k):
    """Find the length of the longest common subsequence of strings a and b,
       where each subsequence is made up of segments with a length of at least k."""
    common_segments = [[0 for j in xrange(len(b) + 1)] for i in xrange(len(a) + 1)]
    dp = [[0 for j in xrange(len(b) + 1)] for i in xrange(len(a) + 1)]
    for i in xrange(1, len(a) + 1):
        for j in xrange(1, len(b) + 1):
        if a[i - 1] == b[j - 1]:
            common_segments[i][j] = common_segments[i - 1][j - 1] + 1
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        if common_segments[i][j] >= k:
            for x in xrange(k, common_segments[i][j] + 1):
        dp[i][j] = max(dp[i][j], dp[i - x][j - x] + x)

    return dp[len(a)][len(b)]
