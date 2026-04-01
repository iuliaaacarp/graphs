import random

from operations import GraphOperations

class Utilities:
    """
    Utility class for file I/O and random graph generation.
    """

    @staticmethod
    def read_from_file(filename):
        """
        Reads graph data from a file and returns a GraphOperations object.

            * :param filename: The name of the file to read.
        Complexity: O(E)
        """
        with open(filename, 'r') as f:
            line = f.readline().split()
            if not line: return None
            n, m = map(int, line)
            graph = GraphOperations(n)
            for _ in range(m):
                u, v, c = map(int, f.readline().split())
                graph.add_edge(u, v, c)
        return graph

    @staticmethod
    def write_to_file(filename, graph):
        """
        Writes the vertex count and all edges of the graph to a file.

            * :param filename: The name of the file to write.
            * :param graph: The graph to write.
        Complexity: O(V + E)
        """
        with open(filename, 'w') as f:
            edge_list = []
            for u in graph.iterate_vertices():
                for v in graph.iterate_out_neighbours(u):
                    edge_list.append((u, v, graph.get_edge_cost(u, v)))
            f.write(f"{graph.get_number_of_vertices()} {len(edge_list)}\n")
            for u, v, c in edge_list:
                f.write(f"{u} {v} {c}\n")

    @staticmethod
    def generate_random_graph(n, m):
        """
        Generates a random directed graph with n vertices and m edges.

            * :param n: The number of vertices.
            * :param m: The number of edges.
        Complexity: O(m) average case.
        """
        if m > n * n:
            raise ValueError("Too many edges for the number of vertices.")

        g = GraphOperations(n)

        edges_added = 0
        while edges_added < m:
            u = random.randint(0, n - 1)
            v = random.randint(0, n - 1)
            cost = random.randint(1, 100)

            if g.add_edge(u, v, cost):
                edges_added += 1

        return g