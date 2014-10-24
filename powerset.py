import itertools

def powerset(arr):
    """Generate power set of set."""
    sets = []
    for bitmask in xrange(pow(2, len(arr))):
        binstr = bin(bitmask)[2:].zfill(len(arr))
        newset = [arr[index] for (index, bit) in enumerate(binstr) if bit == "1"]
        sets.append(newset)
    return sets

def powerset_simple(s):
    return itertools.chain.from_iterable(
            itertools.combinations(s, r) for r in xrange(len(s) + 1))

print list(powerset_simple([1, 2, 3]))
