import math


def newtons_method(n, prec=1e-8):
    prev, mid = 0, float(n)
    while abs(mid - prev) > prec:
        prev, mid = mid, (mid + (n / mid)) / 2
    return mid


def main():
    assert abs(newtons_method(0) - math.sqrt(0)) < 1e-8
    assert abs(newtons_method(1) - math.sqrt(1)) < 1e-8
    assert abs(newtons_method(49) - math.sqrt(49)) < 1e-8
    assert abs(newtons_method(0.49) - math.sqrt(0.49)) < 1e-8
    assert abs(newtons_method(0.81) - math.sqrt(0.81)) < 1e-8
    assert abs(newtons_method(2) - math.sqrt(2)) < 1e-8


if __name__ == "__main__":
    main()
