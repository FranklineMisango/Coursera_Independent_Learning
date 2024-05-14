import networkx as nx
import matplotlib.pyplot as plt

class Bag:
    def __init__(self):
        self.bag = []

    def add(self, item):
        self.bag.append(item)

    def __iter__(self):
        return iter(self.bag)

class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = [Bag() for _ in range(V)]

    def add_edge(self, v, w):
        self.adj[v].add(w)
        self.adj[w].add(v)

    def adj(self, v):
        return self.adj[v]

def visualize_graph(graph):
    nx_graph = nx.Graph()
    for v in range(graph.V):
        for w in graph.adj(v):
            nx_graph.add_edge(v, w)

    pos = nx.spring_layout(nx_graph)
    nx.draw(nx_graph, pos, with_labels=True, node_size=500, node_color='skyblue', font_size=12, font_weight='bold')
    plt.title('Graph Visualization')
    plt.show()


def read_graph_from_input():
    V = int(input("Enter the number of vertices: "))
    graph = Graph(V)

    E = int(input("Enter the number of edges: "))
    print("Enter the edges (vertex pairs separated by space, indices starting from 0):")
    for _ in range(E):
        v, w = map(int, input().split())
        if v >= V or w >= V:
            print("Invalid vertex indices. Please enter indices within the range [0, V-1].")
            return None
        graph.add_edge(v, w)

    return graph


if __name__ == "__main__":
    try:
        # Read the graph from user input
        graph = read_graph_from_input()

        # Visualize the graph
        visualize_graph(graph)
    except ValueError:
        print("Invalid input. Please enter integers for number of vertices, edges, and edge pairs.")
