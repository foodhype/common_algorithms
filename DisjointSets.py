class DisjointSets(object):
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def makeset(self, v):
        """Create a set containing v."""
        self.parent[v] = v
        self.rank[v] = 0

    def union(self, u, v):
        """Join the subsets containing u and v into a single subset.

        Implementation notes: uses union by rank.
        """
        uroot = self.find(u)
        vroot = self.find(v)
        if uroot != vroot:
            if self.rank[uroot] < self.rank[vroot]:
                self.parent[uroot] = vroot
            elif self.rank[vroot] < self.rank[uroot]:
                self.parent[vroot] = uroot
            else:
                self.parent[vroot] = uroot
                self.rank[uroot] += 1

    def find(self, v):
        """Determine which subset v is in.
        
        By comparing the result of two find operations, one can determine if
        two elements are in the same subset. Implementation notes: uses path
        compression.

        Returns:
            An item from the set containing v that serves as its
            representative.
        """
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])

        return self.parent[v]
