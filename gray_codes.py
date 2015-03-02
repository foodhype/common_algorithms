def gray_codes(n):
    """Return a sequence of n-bit gray codes starting with 0."""
    if n == 0:
        return [0]
    else:
        gray_codes = [0, 1]
        for i in xrange(1, n):
            # Reversing all i-bit gray codes will produce another sequence
            # where successive terms differ by one bit. If we prepend a '1' bit
            # to all terms in the reversed gray codes, they will maintain this
            # property; additionally, the first term in the reversed gray codes
            # will differ from the last code in the original gray codes by one 
            # bit. Thus, appending the new sequence to end of the original
            # sequence will produce a valid gray code sequence. Since the
            # resulting sequence will be twice as large, it must cover all gray 
            # codes with i + 1 bits.
            reversed_gray_codes = [code for code in reversed(gray_codes)]
            for code in reversed_gray_codes:
                gray_codes.append(code + (1 << i))

        return gray_codes


def main():
    assert gray_codes(0) == [0]
    assert gray_codes(1) == [0, 1]
    assert gray_codes(2) == [0, 1, 3, 2]
    assert gray_codes(3) == [0, 1, 3, 2, 6, 7, 5, 4]


if __name__ == "__main__":
    main()
