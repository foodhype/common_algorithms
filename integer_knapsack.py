def integer_knapsack(values, weights, capacity):
    dp = [[0 for _ in xrange(capacity + 1)] for _ in xrange(len(values) + 1)]

    for i in xrange(len(values) + 1):
        for weight in xrange(capacity + 1):
            if i == 0 or weight == 0:
                dp[i][weight] = 0
            elif weights[i - 1] <= weight:
                dp[i][weight] = max(dp[i - 1][weight], values[i - 1] + dp[i - 1][weight - weights[i - 1]])
            else:
                dp[i][weight] = dp[i - 1][weight]

    return dp[len(values)][capacity]


def main():
    values = [60, 100, 120]
    weights = [10, 20, 30]
    capacity = 50
    print integer_knapsack(values, weights, capacity)


if __name__ == "__main__":
    main()
