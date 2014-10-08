def coin_change(denominations, total):
    """Get list of all possible combinations of coins from denominations that
    sum to total."""
    memo = [0 for _ in xrange(total + 1)]
    coins = [None for _ in xrange(total + 1)]
    memo[0] = 1
    coins[0] = [[]]
    for denomination in denominations:
        for index in xrange(denomination, total + 1):
            if memo[index - denomination] > 0:
                if coins[index] is None:
                    coins[index] = []
                for combination in coins[index - denomination]:
                    coins[index].append(combination + [denomination])
                memo[index] += memo[index - denomination]

    return coins[total]


def main():
    print coin_change([1, 5, 10, 25, 50, 100], 100)


if __name__ == "__main__":
    main()
