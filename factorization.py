def factors(n):
    yield (n, 1)
    for factorization in set(factors_helper(n)):
        yield factorization


def factors_helper(n, visited=None):
    for i in xrange(2, int(n**0.5) + 1):
        if n % i == 0:
            factor1, factor2 = i, n // i
            factorization = tuple(sorted((factor1, factor2)))
            yield factorization
            for f1_tree, f2_tree in zip(
                    factors_helper(factor1), factors_helper(factor2)):
                factorization = tuple(sorted(f1_tree + f2_tree))
                yield factorization


for factorization in factors(36):
    print factorization
