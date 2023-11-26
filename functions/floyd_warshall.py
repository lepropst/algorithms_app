from data_structures.nodes import GraphNode
from graph_operations.bellman_ford import Graph


class Vertex:
    def __init__(self, vertex):
        self.name = vertex
        self.neighbors = []

    def add_neighbor(self, neighbor):
        if isinstance(neighbor, Vertex):
            if neighbor.name not in self.neighbors:
                self.neighbors.append(neighbor.name)
                neighbor.neighbors.append(self.name)
                print(self.neighbors)
                self.neighbors = sorted(self.neighbors)
                neighbor.neighbors = sorted(neighbor.neighbors)
        else:
            return False

    def add_neighbors(self, neighbors):
        for neighbor in neighbors:
            if isinstance(neighbor, Vertex):
                if neighbor.name not in self.neighbors:
                    self.neighbors.append(neighbor.name)
                    neighbor.neighbors.append(self.name)
                    self.neighbors = sorted(self.neighbors)
                    neighbor.neighbors = sorted(neighbor.neighbors)
            else:
                return False

    def __repr__(self):
        return str(self.neighbors)


# def bf(data):
#     g = Graph(len(data.get("undirected_graph_nodes")))
#     for item in data.get("undirected_graph_nodes"):
#         for verticeSet in item.get("vertices"):
# g.addEdge(item.get("data"), verticeSet, item.get("weight"))


def floyd_warshall(data):
    g = Graph(len(data.get("undirected_graph_nodes")))
    for item in data.get("undirected_graph_nodes"):
        for verticeSet in item.get("vertices"):
            g.addEdge(item.get("data"), verticeSet, item.get("weight"))
    print(g.graph)

    [print(x) for x in g.adjacencyArray()]
