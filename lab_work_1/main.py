from utilities import Utilities


def main():
    utility = Utilities()
    graph = utility.read_from_file("graph1m.txt")
    utility.write_to_file("graph.txt", graph)
    print("Okey! :)")

if __name__ == '__main__':
    main()