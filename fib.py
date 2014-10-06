import decimal


"""module for generating fibonacci numbers"""

def fib(count):
    """Return nth fibonacci number using Binet's formula."""
    with decimal.localcontext() as context:
        context.prec = count
        sqrt_five = decimal.Decimal(5).sqrt()
        golden_ratio = (1 + sqrt_five) / 2

        return int((golden_ratio**count - (-golden_ratio**(-count))) / sqrt_five)


def fibs(count):
    """Generator for first n fibonacci numbers"""
    current_fib, next_fib = 0, 1
    for _ in xrange(count):
        yield current_fib
        current_fib, next_fib = next_fib, current_fib + next_fib


def fibs_xrange(stop):
    """Generator for fibonacci numbers up to stop"""
    current_fib, next_fib = 0, 1
    while current_fib < stop:
        yield current_fib
        current_fib, next_fib = next_fib, current_fib + next_fib
