import random

def shuffle(a):
  for i in reversed(xrange(1, len(a))):
    random_index = int(random.random() * i)
    temp = a[i]
    a[i] = a[random_index]
    a[random_index] = temp

  return a

def main():
  li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  print li
  print shuffle(li)

if __name__ == "__main__":
  main()
