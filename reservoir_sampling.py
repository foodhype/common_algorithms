import random

def sample(a, k):
  """Get k random elements from a with uniform probability."""
  reservoir = [a[i] for i in xrange(k)]
  for i in xrange(k + 1, len(a)):
    random_index = int(i * random.random())
    if random_index < k:
      reservoir[random_index] = a[i]

  return reservoir

def main():
  li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  print li
  print sample(li, 3)

if __name__ == "__main__":
  main()
