import random
import copy

class DirectedGraph:
    """
    A class used to represent a Directed Graph using adjacency maps.

    Attributes:
        _vertices (set): A set containing all vertex identifiers.
        _in_neighbors (dict): Maps a vertex to a dictionary of its incoming neighbors and edge costs.
        _out_neighbors (dict): Maps a vertex to a dictionary of its outgoing neighbors and edge costs.
    """

    def __init__(self, vertices=0):
        """
        Initializes a directed graph with a fixed number of vertices (0 to n-1).
        Complexity: O(V)
        """
        self._vertices = set(range(vertices))
        self._in_neighbors = {v: {} for v in self._vertices}
        self._out_neighbors = {v: {} for v in self._vertices}

    def get_number_of_vertices(self):
        """
        Returns the total number of vertices in the graph.
        Complexity: O(1)
        """
        return len(self._vertices)

    def get_in_degree(self, vertex):
        """
        Returns the number of inbound edges for a given vertex.
        Complexity: O(1)
        """
        return len(self._in_neighbors[vertex])

    def get_out_degree(self, vertex):
        """
        Returns the number of outbound edges for a given vertex.
        Complexity: O(1)
        """
        return len(self._out_neighbors[vertex])

    def get_edge_cost(self, u, v):
        """
        Returns the cost of the edge from vertex u to vertex v.
        Complexity: O(1)
        """
        return self._out_neighbors[u][v]

    def set_edge_cost(self, u, v, cost):
        """
        Updates the cost of an existing edge (u, v).
        Complexity: O(1)
        Raises Exception if the edge does not exist.
        """
        if v in self._out_neighbors[u]:
            self._out_neighbors[u][v] = cost
            self._in_neighbors[v][u] = cost
            return
        raise Exception("Edge cost cannot be set: Edge does not exist")

    def iterate_vertices(self):
        """
        Returns an iterator for the set of vertices.
        Complexity: O(1)
        """
        return iter(self._vertices)

    def iterate_out_neighbours(self, u):
        """
        Returns an iterator over the keys (neighbors) of the outbound edges of u.
        Complexity: O(1)
        """
        return iter(self._out_neighbors[u].keys())

    def iterate_in_neighbours(self, u):
        """
        Returns an iterator over the keys (neighbors) of the inbound edges of u.
        Complexity: O(1)
        """
        return iter(self._in_neighbors[u].keys())

    def is_edge(self, u, v):
        """
        Checks if a directed edge exists from u to v.
        Complexity: O(1)
        """
        return u in self._out_neighbors and v in self._out_neighbors[u]

    def iterate_vertices(self):
        """
        Returns an iterator for all vertices in the graph.
        Usage: for v in graph.iterate_vertices():
        """
        return iter(self._vertices)

    def iterate_out_neighbors(self, u):
        """
        Returns an iterator for the vertices v such that there is an edge (u, v).
        Usage: for v in graph.iterate_out_neighbors(u):
        """
        if u not in self._out_neighbors:
            raise ValueError("Vertex not in graph")
        return iter(self._out_neighbors[u].keys())

    def iterate_in_neighbors(self, v):
        """
        Returns an iterator for the vertices u such that there is an edge (u, v).
        Usage: for u in graph.iterate_in_neighbors(v):
        """
        if v not in self._in_neighbors:
            raise ValueError("Vertex not in graph")
        return iter(self._in_neighbors[v].keys())