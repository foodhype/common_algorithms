
def powerset(set):
  sets = []
  for bitmask in xrange(pow(2, len(set))):
    binstr = bin(bitmask)[2:].zfill(len(set))
    newset = [set[index] for (index, bit) in enumerate(binstr) if bit == "1"]
    sets.append(newset)
  print sets


print powerset([1, 2, 3])
