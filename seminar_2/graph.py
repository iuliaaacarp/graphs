from random import randint
import time

class Graph:
    def __init__(self, nr_vertices):
        self._nr_vertices = nr_vertices
        self.__out_neighbours = {}
        self.__in_neighbours = {}
        for i in range(self._nr_vertices):
            self.__out_neighbours[i] = []
            self.__in_neighbours[i] = []

    def add_edge(self, source, destination, weight):
        self.__out_neighbours[source].append(destination)
        self.__in_neighbours[destination].append(source)

    def parse_vertices(self):
        return self.__out_neighbours.keys()

    def parse_out(self, vertex):
        return list(self.__out_neighbours[vertex])

    def parse_in(self, vertex):
        return list(self.__in_neighbours[vertex])

    def is_edge(self, x, y):
        if y in self.__out_neighbours[x]:
            return True
        return False

def print_graph(g):
    print("Outbound")
    for x in g.parse_vertices():
        s = f"{x}:"
        for y in g.parse_out(x):
            s += f" {y}"
        print(s)

    print("Inbound")
    for x in g.parse_vertices():
        s = f"{x}:"
        for y in g.parse_in(x):
            s += f" {y}"
        print(s)

def check_performance(g):
    before = time.time()
    for x in g.parse_vertices():
        for y in g.parse_out(x):
            pass
    after = time.time()
    print(f"Outbound time: {(after - before)*1000} ms")
    before = time.time()
    for x in g.parse_vertices():
        for y in g.parse_in(x):
            pass
    after = time.time()
    print(f"Inbound time: {(after - before)*1000} ms")

def small_graph():
    g = Graph(6)
    g.add_edge(0,1,1)
    g.add_edge(0,3,4)
    g.add_edge(1,5,8)
    g.add_edge(1,1,3)
    g.add_edge(1,0,2)
    g.add_edge(1,3,2)
    g.add_edge(3,4,2)
    g.add_edge(4,5,2)
    g.add_edge(5,3,1)
    return g

def random_graph(n, m):
    g = Graph(n)
    before = time.time()
    added = 0
    while added < m:
        x = randint(0, n - 1)
        y = randint(0, n - 1)
        if g.is_edge(x, y):
            continue
        g.add_edge(x, y, 1)
        added += 1
    after = time.time()
    print(f"Generated: {(after - before)*1000} ms")
    return g

def test():
    g = small_graph()
    vertices = list(g.parse_vertices())
    print(f"vertices: type={type(vertices)}, members={dir(vertices)})")
    vertices.remove(1)
    print(f"Vertices with property X:{vertices}")

    neighbours = g.parse_out(2)
    neighbours.append(0)
    print_graph(g)

if __name__ == "__main__":
    test()
    # g = small_graph()
    #n = 10000
    #g = random_graph(n, 10*n)
    #print_graph(g)
    #check_performance(g)