def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) / gcd(a, b)

def gcd_all(integers):
    result = 0
    for i in integers:
        result = gcd(i, result)
    return result

def lcm_all(integers):
    result = 1
    for i in integers:
        result = lcm(result, i)
    return result
