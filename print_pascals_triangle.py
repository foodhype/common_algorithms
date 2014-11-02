import sys


"""
n choose i =
n! / (i! * (n - i)!)

x * coeff(n,  i - 1) = coeff(n, i)
x * n! / ((i - 1)! * (n - (i - 1))!) = n! / (i! * (n - i)!)
x / ((i - 1)! * (n - (i - 1))!) = 1 / (i! * (n - i)!)
x * i / (n - i + 1)! = 1 / (n - i)!
x * i = n - i + 1
x = (n - i + 1) / i
"""


def print_pascals_triangle(row_count):
    for n in xrange(row_count + 1):
        coeff = 1
        for i in xrange(1, n + 1):
            sys.stdout.write(str(coeff) + " ")
            coeff = (coeff * (n - i)) // i # still don't understand why it's (n - i) and not (n - i + 1)
        sys.stdout.write("\n")

print_pascals_triangle(5)
