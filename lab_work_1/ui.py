from utilities import Utilities

class UI:
    def __init__(self):
        self._graph = None
        self._utilities = Utilities()

    def _print_menu(self):
        print("====================================")
        print("---- Graph Operations Menu ---------")
        print("====================================")
        print("  1. Read graph from file")
        print("  2. Write graph to file")
        print("  3. Generate random graph")
        print("  4. Add vertex")
        print("  5. Remove vertex")
        print("  6. Add edge")
        print("  7. Remove edge")
        print("  8. Update edge cost")
        print("  9. Show graph stats (Vertices, Edges, Degrees)")
        print(" 10. Check if edge exists")
        print(" 11. List all vertices")
        print(" 12. List neighbors of a vertex")
        print(" 13. Iterate through all vertices")
        print(" 14. List all outbound neighbors of a vertex")
        print(" 15. List all inbound neighbors of a vertex")
        print(" 16. Show the whole graph")
        print("  0. Exit")
        print("====================================")

    def run(self):
        self._graph = self._utilities.read_from_file("graph1k.txt")
        while True:
            self._print_menu()
            choice = input(">> Select an option: ")
            try:
                if choice == "1":
                    filename = input(">> Enter filename: ")
                    self._graph = self._utilities.read_from_file(filename)
                    print("====================================")
                    print("--> Graph loaded successfully.")
                elif choice == "2":
                    filename = input(">> Enter output filename: ")
                    self._utilities.write_to_file(filename, self._graph)
                    print("====================================")
                    print("--> Graph saved successfully.")
                elif choice == "3":
                    n = int(input(">> Number of vertices: "))
                    m = int(input(">> Number of edges: "))
                    print("====================================")
                    self._graph = self._utilities.generate_random_graph(n, m)
                    print("--> Random graph generated.")
                elif choice == "4":
                    v = int(input(">> Enter vertex ID to add: "))
                    print("====================================")
                    if self._graph.add_vertex(v):
                        print("--> Vertex added.")
                    else:
                        print("--> Vertex already exists.")
                elif choice == "5":
                    v = int(input(">> Enter vertex ID to remove: "))
                    print("====================================")
                    if self._graph.remove_vertex(v):
                        print("--> Vertex removed.")
                    else:
                        print("--> Vertex does not exist.")
                elif choice == "6":
                    u = int(input(">> Source vertex: "))
                    v = int(input(">> Target vertex: "))
                    c = int(input(">> Cost: "))
                    print("====================================")
                    if self._graph.add_edge(u, v, c):
                        print("--> Edge added.")
                    else:
                        print("--> Failed to add edge (check if vertices exist or edge already exists).")
                elif choice == "7":
                    u = int(input(">> Source vertex: "))
                    v = int(input(">> Target vertex: "))
                    print("====================================")
                    if self._graph.remove_edge(u, v):
                        print("--> Edge removed.")
                    else:
                        print("--> Edge does not exist.")
                elif choice == "8":
                    u = int(input(">> Source vertex: "))
                    v = int(input(">> Target vertex: "))
                    c = int(input(">> New cost: "))
                    print("====================================")
                    self._graph.set_edge_cost(u, v, c)
                    print("--> Cost updated.")
                elif choice == "9":
                    print(f"Vertices: {self._graph.get_number_of_vertices()}")
                    print("====================================")
                    for v in self._graph.iterate_vertices():
                        print(f">> Vertex {v}:")
                        print(f"In-degree: {self._graph.get_in_degree(v)} | Out-degree: {self._graph.get_out_degree(v)}")
                        print("------------------------------------")
                elif choice == "10":
                    u = int(input(">> Source vertex: "))
                    v = int(input(">> Target vertex: "))
                    print("====================================")
                    if self._graph.is_edge(u, v):
                        print(f"--> Edge exists with cost {self._graph.get_edge_cost(u, v)}.")
                    else:
                        print("--> Edge does not exist.")

                elif choice == "11":
                    print("--> Vertices as list:")
                    print(list(self._graph.iterate_vertices()))

                elif choice == "12":
                    u = int(input(">> Vertex ID: "))
                    print("====================================")
                    print(f"> Outbound neighbors: {list(self._graph.iterate_out_neighbours(u))}")
                    print(f"> Inbound neighbors: {list(self._graph.iterate_in_neighbours(u))}")

                elif choice == "13":
                    print("--> Iterating through all vertices:")
                    print("====================================")
                    for v in self._graph.iterate_vertices():
                        print(f"Found vertex: {v}")

                elif choice == "14":
                    u = int(input(">> Enter source vertex: "))
                    print("====================================")
                    print(f"--> Iterating through outbound neighbors of {u}:")
                    for v in self._graph.iterate_out_neighbors(u):
                        cost = self._graph.get_edge_cost(u, v)
                        print(f" -> Target: {v} | Cost: {cost}")
                        print("------------------------------------")

                elif choice == "15":
                    v = int(input(">> Enter target vertex: "))
                    print("====================================")
                    print(f"Iterating through inbound neighbors of {v}:")
                    for u in self._graph.iterate_in_neighbors(v):
                        cost = self._graph.get_edge_cost(u, v)
                        print(f" -> Source: {u} (Cost: {cost})")
                        print("------------------------------------")

                elif choice == "16":
                    print("====================================")
                    print("Displaying the whole graph:")
                    print("====================================")
                    for u in range(0, self._graph.get_number_of_vertices()):
                        print("------------------------------------")
                        print(f"--- Vertex {u}:")
                        print(f"> Outbound neighbors: {list(self._graph.iterate_out_neighbours(u))}")
                        print(f"> Inbound neighbors: {list(self._graph.iterate_in_neighbours(u))}")

                elif choice == "0":
                    print("--> Goodbye!")
                    break
                else:
                    print("-->Invalid choice.")
            except Exception as e:
                print(f"Error: {e}")
