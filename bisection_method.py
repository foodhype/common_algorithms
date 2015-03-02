def opposite_signs(a, b):
    return ((a < 0 and b > 0) or
            (a > 0 and b < 0) or 
            (a == 0 or b == 0)) # This last case is specific to bisection method.


def bisection_method(f, a, b, iterations):
    """Find a root of function f in the interval [a, b]."""

    mid = (a + b) / 2

    for _ in xrange(iterations - 1):
        if opposite_signs(f(a), f(mid)):
            b = mid
            mid = (a + b) / 2
        elif opposite_signs(f(mid), f(b)):
            a = mid
            mid = (a + b) / 2
        else:
            return mid

    return mid


def main():
    f = lambda x: 3.0 * (x + 1.0) * (x - 0.5) * (x - 1.0)
    print bisection_method(f, -2.0, 1.5, 3)


if __name__ == "__main__":
    main()
