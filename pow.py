import math


def float_pow(base, exp, prec=53):
    if exp < 0:
        return 1.0 / float_pow(base, -exp)
    elif exp == 0:
        return 1.0
    elif 0 < exp < 1:
        lo = 0.0
        hi = 1.0
        mid = (lo + hi) / 2.0

        sqrt = math.sqrt(base)
        result = sqrt

        while abs(mid - exp) > 1.0 / 2**prec:
            sqrt = math.sqrt(sqrt)

            if mid <= exp:
                lo = mid
                result *= sqrt
            else:
                hi = mid
                result /= sqrt

            mid = (lo + hi) / 2.0

        return result
    else:
        temp = float_pow(base, exp / 2)
        return temp * temp

def int_pow(base, exp):
    if exp < 0:
        return 1.0 / int_pow(base, -exp)
    elif exp == 0:
        return 1
    else:
        temp = 1
        while exp > 1:
            if exp & 1:
                temp *= base
            base *= base
            exp /= 2
        return temp * base


print float_pow(10000, 0.25)
print 10000**0.25
