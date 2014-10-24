import re


def build_trie(words):
    trie = {}
    for word in words:
        current = trie
        for c in word:
            if c not in current:
                current[c] = {}
            current = current[c]

    return trie


def main():
    with open("/usr/share/dict/words") as word_file:
        words = [word.lower().rstrip() for word
            in word_file.readlines()
            if re.match("^[A-Za-z]+$", word)]

        print build_trie(words)


if __name__ == "__main__":
    main() 
