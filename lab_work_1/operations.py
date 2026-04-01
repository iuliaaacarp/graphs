import copy
from directed_graph import DirectedGraph


class GraphOperations(DirectedGraph):
    """
    Subclass of DirectedGraph providing modification operations like adding/removing
    vertices and edges, as well as copying.
    """

    def add_edge(self, u, v, cost):
        """
        Adds a directed edge from u to v with the specified cost.
        Complexity: O(1)
        Returns True if added, False if vertices don't exist or edge already exists.
        """
        if u in self._vertices and v in self._vertices:
            if v not in self._out_neighbors[u]:
                self._in_neighbors[v][u] = cost
                self._out_neighbors[u][v] = cost
                return True
        return False

    def remove_edge(self, u, v):
        """
        Removes the directed edge from u to v.
        Complexity: O(1)
        Returns True if removed, False if edge did not exist.
        """
        if not self.is_edge(u, v):
            return False
        del self._in_neighbors[v][u]
        del self._out_neighbors[u][v]
        return True

    def add_vertex(self, vertex):
        """
        Adds a new vertex to the graph.
        Complexity: O(1)
        Returns True if successful, False if vertex already exists.
        """
        if vertex not in self._vertices:
            self._vertices.add(vertex)
            self._out_neighbors[vertex] = {}
            self._in_neighbors[vertex] = {}
            return True
        return False

    def remove_vertex(self, vertex):
        """
        Removes a vertex and all its associated edges from the graph.
        Complexity: O(deg_in + deg_out)
        Returns True if successful, False if vertex does not exist.
        """
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
        """
        Returns a deep copy of the current graph.
        Complexity: O(V + E)
        """
        return copy.deepcopy(self)