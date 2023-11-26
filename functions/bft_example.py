import json
from data_structures.nodes import GraphNode
from graph_operations.dft import dft

from sorts.insertion_sort import insertionSort


def bst_example(data):
    result = []
    if type(data.get("undirected_graph_nodes")) is list:
        for x in data.get("undirected_graph_nodes"):
            if x.get("data") in [x.data for x in result]:
                current = result[[x.data for x in result].index(x.get("data"))]
                print(f"current: {current}")
                continue
            else:
                result.append(GraphNode(x.get("data")))
        for item in result:
            print(f"data.get aat item :{item} {data.get("undirected_graph_nodes")[[x.get("data") for x in data.get("undirected_graph_nodes")].index(item.data)]}")
            current= data.get("undirected_graph_nodes")[[x.get("data") for x in data.get("undirected_graph_nodes")].index(item.data)]
            for vertice in current.get("vertices"):
                if vertice in [x.data for x in result]:
                    item.vertices.append(result[[x.data for x in result].index(vertice)])

            print(f"data.get aat item :{item} {data.get("undirected_graph_nodes")[[x.get("data") for x in data.get("undirected_graph_nodes")].index(item.data)]}")
                
    for item in result:
        print(str(item))
    return result

