def factors(n):
  result = []
  factor_pairs = ([i, n//i] for i in xrange(
      1, int(n**0.5) + 1) if n % i == 0)
  for factor_pair in factor_pairs:
    result += factor_pair
  return result

def isprime(n):
  if n == 2:
    return True
  elif n % 2 == 0:
    return False
  i = 3
  while i <= int(n**0.5) + 1:
    if n % i == 0:
      return False
    i += 2
  return True

def primefactors(n):
  return [p for p in factors(n) if isprime(p)]
