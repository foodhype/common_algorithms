def rot13(original):
  translated = []
  for character in original:
    shifted = ord(character)
    if ord('A') <= ord(character) <= ord('Z'):
      shifted = ord(character) + 13
      if shifted > ord('Z'):
        shifted = ord('A') + (shifted - ord('Z') - 1)
    elif ord('a') <= ord(character) <= ord('z'):
      shifted = ord(character) + 13
      if shifted > ord('z'):
        shifted = ord('a') + (shifted - ord('z') - 1)
    translated.append(chr(shifted))

  return "".join(translated)

if __name__ == '__main__':
  original = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
  assert rot13(original) == "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"
