def rod_cut(n, p):
    dp = [-1 for _ in xrange(n + 1)]
    dp[0] = 0
    for i in xrange(1, n + 1):
        q = -1
        for j in xrange(1, i + 1):
            q = max(q, p[j] + dp[i - j])
        dp[i] = q

    return dp[n]
