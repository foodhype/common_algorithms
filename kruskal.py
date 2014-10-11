from DisjointSets import DisjointSets


def kruskal(graph):
    """Find the minimum spanning tree of a graph."""
    msf = set()

    forest = DisjointSets()
    for v in graph.keys():
        forest.makeset(v)

    edges = []
    for u, adjlist in graph.items():
        for (v, weight) in adjlist.items():
            edges.append((u, v, weight))
    edges.sort(key=lambda edge: edge[2])

    for u, v, w in edges:
        if forest.find(u) != forest.find(v):
            msf.add((u, v, w))
            forest.union(u, v)
    
    return msf


def main():
    graph = {'A': {'D': 5, 'B': 7},
            'B': {'A': 7, 'C': 8, 'D': 9, 'E': 7},
            'C': {'B': 8, 'E': 5},
            'D': {'A': 5, 'B': 9, 'E': 15, 'F': 6},
            'E': {'B': 7, 'C': 5, 'D': 15, 'F': 8, 'G': 9},
            'F': {'D': 6, 'E': 8, 'G': 11},
            'G': {'E': 9, 'F': 11}}

    expected = set([('A', 'B', 7),
            ('A', 'D', 5),
            ('B', 'E', 7),
            ('C', 'E', 5),
            ('D', 'F', 6),
            ('E', 'G', 9)])

    msf = kruskal(graph)
    assert msf.issubset(expected) and expected.issubset(msf)


if __name__ == "__main__":
    main()
