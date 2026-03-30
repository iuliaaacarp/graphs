from seminar_2.graph import Graph

def bfs(g, s):
    """
    Perform BF search in graph g starting from vertex s
    Returns a tuple (dist, parent) where:
        > dist is a dictionary with keys all vertices accessible from s and
        dist[x] = length of shortest path from s to x
        > parent is a dictionary with keys all vertices accessible from s and
        parent[x] = parent of x in the BFS tree; parent[s] = None
    Precondition: s is a vertex of graph g
    """
    dist = {}
    parent = {}

    dist[s] = 0
    parent[s] = None

    queue = []
    queue.append(s)
    visited = set()
    visited.add(s)
    while len(queue) > 0:
        current = queue.pop(0)
        for next in g.parse_out(current):
            if next in visited:
                continue
            dist[next] = dist[current] + 1
            visited.add(next)
            queue.append(next)

    return (dist, parent)

def test_bfs():
    g = Graph.small_graph()
    dist, parent = bfs(g, 1)
    print(f"dist={dist}")
    print(f"parent={parent}")

if __name__ == '__main__':
    test_bfs()