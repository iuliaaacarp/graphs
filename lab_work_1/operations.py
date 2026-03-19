import copy
from directed_graph import DirectedGraph

class GraphOperations(DirectedGraph):
    def __init__(self, edges = 0):
        super().__init__(edges)
        self._edges = edges

    def add_edge(self, u, v, cost):
        if u in self._vertices and v in self._vertices:
            if v not in self._out_neighbors[u]:
                self._in_neighbors[v][u] = cost
                self._out_neighbors[u][v] = cost
                return True
        return False

    def remove_edge(self, u, v):
        if v not in self._out_neighbors[u]:
            return False
        del self._in_neighbors[v][u]
        del self._in_neighbors[u][v]
        return True

    def add_vertex(self, vertex):
        if vertex not in self._vertices:
            self._vertices.add(vertex)
            self._out_neighbors[vertex] = {}
            self._in_neighbors[vertex] = {}
            return True
        return False

    def remove_vertex(self, vertex):
        if vertex not in self._vertices:
            return False
        for source in list(self._in_neighbors[vertex].keys()):
            self.remove_edge(source, vertex)
        for target in list(self._out_neighbors[vertex].keys()):
            self.remove_edge(vertex, target)

        del self._in_neighbors[vertex]
        del self._out_neighbors[vertex]
        self._vertices.remove(vertex)
        return True

    def copy_graph(self):
        return copy.deepcopy(self)

