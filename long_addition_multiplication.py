#TODO: handle negative numbers
def multiply(x, y):
  """Perform long multiplication of strings representing integers."""
  sums = []
  product = "0"
  carry = 0
  for (y_decimal_place, y_digit) in enumerate(y[::-1]):
    sum = "0"
    for (x_decimal_place, x_digit) in enumerate(x[::-1]):
      digit_product = int(x_digit) * int(y_digit) + carry
      carry = int(digit_product) // 10
      addend = str(digit_product % 10).ljust(
          x_decimal_place + y_decimal_place + 1, "0")
      sum = add(sum, addend)
    if carry != 0:
      sum = str(carry) + sum
    sums.append(sum)
  for sum in sums:
    product = add(product, sum)

  return product

# TODO: handle negative numbers
def add(x, y):
  """Perform long addition of strings representing integers."""
  max_length = max(len(x), len(y))
  x = x.zfill(max_length)
  y = y.zfill(max_length)

  carry = 0
  digits = []
  for (x_digit, y_digit) in zip(x[::-1], y[::-1]):
    digit_sum = int(x_digit) + int(y_digit) + carry
    carry = digit_sum // 10
    digits.insert(0, str(digit_sum % 10))
  if carry != 0:
    digits.insert(0, str(carry))

  return "".join(digits)

def main():
  a = "1546546547546"
  b = "5365654762352342352"
  print multiply(a, b)
  

if __name__ == "__main__":
  main()
