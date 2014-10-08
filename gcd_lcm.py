def gcd(a, b):
    """Greatest common denominator (Euclid's algorithm, iterative)."""
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Lowest common multiple."""
    return (a * b) / gcd(a, b)

def gcd_all(integers):
    """Greatest common denominator of more than two integers."""
    result = 0
    for i in integers:
        result = gcd(i, result)
    return result

def lcm_all(integers):
    """Lowest common multiple of more than two integers."""
    result = 1
    for i in integers:
        result = lcm(result, i)
    return result
