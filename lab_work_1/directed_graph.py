class DirectedGraph:
    def __init__(self, vertices = 0):
        self._vertices = set(range(vertices))
        self._no_vertices = vertices
        self._in_neighbors = {}
        self._out_neighbors = {}
        for vertex in range(self._no_vertices):
            self._in_neighbors[vertex] = {}
            self._out_neighbors[vertex] = {}

    def get_vertices(self):
        return self._no_vertices

    def get_in_neighbors(self, vertex):
        return len(self._in_neighbors[vertex])

    def get_out_neighbors(self, vertex):
        return len(self._out_neighbors[vertex])

    def get_edge_cost(self, u, v):
        return self._out_neighbors[u][v]

    def set_edge_cost(self, u, v, cost):
        if v in self._out_neighbors[u]:
            self._out_neighbors[u][v] = cost
            self._in_neighbors[v][u] = cost
        raise Exception("Edge cost cannot be set")

    def iterate_vertices(self):
        return iter(range(self._no_vertices))

    def iterate_neighbours(self, u):
        return iter(self._out_neighbors[u].keys())

    def is_edge(self, u, v):
        if u in self._in_neighbors[v] or v in self._out_neighbors[u]:
            return u, v
        return None

    def inbound_edges(self, u):
        return list(self._in_neighbors[u])