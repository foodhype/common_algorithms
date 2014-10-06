def primes(limit):
    sieve = [True] * limit
    sieve[0] = False
    sieve[1] = False

    current = 2
    while current < limit:
        while current < limit and not sieve[current]:
            current += 1
        for index in xrange(2 * current, limit, current):
            sieve[index] = False
        current += 1

    return [number for number, is_prime in enumerate(sieve) if is_prime]


def main():
    print primes(100)


if __name__ == "__main__":
    main()
