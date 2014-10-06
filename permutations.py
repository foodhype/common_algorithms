
def permutations(elements):
  if len(elements) <= 1:
    yield elements
  else:
    for i in xrange(len(elements)):
      for p in permutations(elements[:i] + elements[i + 1:]):
        yield (elements[i:i + 1] + p)

for p in permutations([1, 2, 3, 4, 5]):
  print p
