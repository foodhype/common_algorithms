def valid_parentheses(s):
    count = 0
    for c in s:
        if c == "(":
            count += 1
        elif c == ")":
            if count == 0:
                return False
            else:
                count -= 1

    return count == 0


def main():
    assert valid_parentheses("()()") == True
    assert valid_parentheses("()") == True
    assert valid_parentheses("(()()))") == False
    assert valid_parentheses(")") == False
    assert valid_parentheses("()())(") == False


if __name__ == "__main__":
    main()
