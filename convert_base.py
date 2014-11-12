def convert_base(num, old_base, new_base, alphabet):
    if old_base != 10:
        alphabet_base10 = {}
        for index, char in enumerate(alphabet):
            alphabet_base10[char] = index
        base10 = 0
        for power, char in enumerate(reversed(num)):
            base10 += alphabet_base10[char] * old_base**power
        num = base10

    digits = []
    while num:
        num, rem = divmod(int(num), new_base)
        digits.append(alphabet[rem])

    return "".join(reversed(digits))


def main():
    alphabet = [str(num) for num in xrange(10)]
    alphabet.extend(list("ABCDEF"))    
    assert convert_base("FA", 16, 3, alphabet) == "100021"
    assert convert_base("100021", 3, 16, alphabet) == "FA"


if __name__ == "__main__":
    main()   
