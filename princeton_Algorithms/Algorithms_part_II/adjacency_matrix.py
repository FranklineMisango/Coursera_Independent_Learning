
import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self, V):
        #Initializing the vertices, Edges and the adjacent matrix to store connections between vertices
        self.V = V
        self.adj_list = [[] for _ in range(V)]
        self.E = 0

    def add_edge(self, v, w):
        self.adj_list[v].append(w)
        self.adj_list[w].append(v)
        self.E += 1

    def adj(self, v):
        return self.adj_list[v]

    def num_vertices(self):
        return self.V

    def num_edges(self):
        return self.E

    def __str__(self):
        graph_str = ""
        for v in range(self.V):
            graph_str += f"{v}: "
            for w in self.adj_list[v]:
                graph_str += f"{w} "
            graph_str += "\n"
        return graph_str

# Example Usage:
# Create a graph with 5 vertices
graph = Graph(5)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 4)

# Convert the adjacency list representation to NetworkX Graph
nx_graph = nx.Graph()
for v in range(graph.num_vertices()):
    for w in graph.adj(v):
        nx_graph.add_edge(v, w)

# Draw the graph
nx.draw(nx_graph, with_labels=True, node_size=500, node_color='skyblue', font_size=12, font_weight='bold')
plt.title('Graph Visualization')
plt.show()
