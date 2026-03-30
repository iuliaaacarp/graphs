from seminar_2.graph import *

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

    queue = [s]
    visited = set()
    visited.add(s)
    while len(queue) > 0:
        current = queue.pop(0)
        for next in g.parse_out(current):
            if next in visited:
                continue
            dist[next] = dist[current] + 1
            parent[next] = current
            visited.add(next)
            queue.append(next)

    return (dist, parent)

def shortest_path(g, s, t):
    """
    Returns a list of vertices representing the shortest (min len) path from s to t in graph g.
    Returns None if there is no path
    Precondition: s and t are vertices in graph g
    """
    dist, parent = bfs(g, s)
    if t not in parent.keys():
        return None
    current_vertex = t
    path = [current_vertex]
    while current_vertex !=s:
        current_vertex = parent[current_vertex]
        path.append(current_vertex)
    path.reverse()
    return path

def test_bfs():
    g = Graph.small_graph()
    dist, parent = bfs(g, 1)
    print(f"dist={dist}")
    print(f"parent={parent}")

if __name__ == '__main__':
    test_bfs()