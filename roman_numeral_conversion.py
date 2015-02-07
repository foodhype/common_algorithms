def roman_to_dec(s):
    result = 0
    roman_hash = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    for index, roman_digit in enumerate(s):
        if index == len(s) - 1:
            result += roman_hash[roman_digit]
        elif roman_hash[s[index]] < roman_hash[s[index + 1]]:
            result -= roman_hash[s[index]]
        else:
            result += roman_hash[roman_digit]
    return result


def dec_to_roman(s):
    result = 0
    for index, dec_digit in enumerate(reversed(s)):
        if dec_digit % 10 == 0:


print roman_to_dec("MCMXCVII")
