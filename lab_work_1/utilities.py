import random

from directed_graph import DirectedGraph
from operations import GraphOperations


class Utilities:
    @staticmethod
    def read_from_file(filename):
        with open(filename, 'r') as f:
            line = f.readline().split()
            if not line: return None
            n, m = map(int, line)
            graph = GraphOperations(n)
            for i in range(m):
                u, v, c = map(int, f.readline().split())
                graph.add_edge(u, v, c)
        return graph

    @staticmethod
    def write_to_file(filename, graph):
        with open(filename, 'w') as f:
            edge_list = []
            for u in graph.iterate_vertices():
                for v in graph.iterate_neighbours(u):
                    edge_list.append((u, v, graph.get_edge_cost(u, v)))

            f.write(f"{graph.get_vertices()} {len(edge_list)}\n")
            for u, v, c in edge_list:
                f.write(f"{u} {v} {c}\n")

    @staticmethod
    def generate_random_graph(n, m):
        if m > n * n: raise ValueError("Too many edges")
        g = GraphOperations(n)
        count = 0
        while count < m:
            u, v = random.randint(0, n - 1), random.randint(0, n - 1)
            if g.add_edge(u, v, random.randint(1, 100)):
                count += 1
        return g

    @staticmethod
    def small_graph():
        g = GraphOperations(6)
        g.add_edge(0, 1, 1)
        g.add_edge(0, 3, 4)
        g.add_edge(1, 5, 8)
        g.add_edge(1, 1, 3)
        g.add_edge(1, 0, 2)
        g.add_edge(1, 3, 2)
        g.add_edge(3, 4, 2)
        g.add_edge(4, 5, 2)
        g.add_edge(5, 3, 1)
        return g
