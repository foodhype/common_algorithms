from collections import deque


def bfs(graph, start, target):
    """Breadth-first search for target in graph from start."""
    if start == target:
        return start

    visited = set()
    visited.add(start)
    queue = deque()
    queue.appendleft(start)
  
    while len(queue) > 0:
        node = queue.pop()
        for neighbor in graph[node]:
            if neighbor not in visited:
                if neighbor == target:
                    return neighbor
                visited.add(neighbor)
                queue.appendleft(neighbor)
              
    return None


def main():
    graph = {1: [1, 2, 3], 2: [8], 3: [4, 5], 4: [], 5: [8], 8: []}
    print graph
    print bfs(graph, 1, 5) 


if __name__ == "__main__":
    main()
