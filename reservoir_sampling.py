import random

def sample(a, k):
    """Get k random elements from a with uniform probability."""
    reservoir = [a[i] for i in xrange(k)]
    for index in xrange(k, len(a)):
        random_index = random.randint(0, index)
        if random_index < k:
            reservoir[random_index] = a[index]

    return reservoir

def main():
    li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print li
    print sample(li, 3)

if __name__ == "__main__":
  main()
