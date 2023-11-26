import heapq

import graphviz

from data_structures.nodes import PlainNode


class Node(PlainNode):
    def __init__(
        self,
        freq,
        symbol,
        left=None,
        right=None,
        huff=-1,
    ):
        # frequency of symbol
        self.freq = freq
        # symbol name (character)
        self.symbol = symbol
        # node left of current node
        self.left = left

        # node right of current node
        self.right = right
        # tree direction (0/1)
        self.huff = str(huff)

    def __lt__(self, nxt):
        return self.freq < nxt.freq

    def print_tree(self, string, dir="default"):
        return super().print_tree(string, dir, key=lambda x: x.symbol)

    def insert(self, freq, symbol, huff=-1):
        if not self.symbol:
            self.symbol = symbol
            self.freq = freq
            self.huff = huff
            return
        if self.symbol == symbol and self.freq:
            return
        if freq < self.freq:
            if self.left:
                self.left.insert(freq, symbol, 0)
                return
            self.left = Node(freq, symbol, huff=0)
            return
        if self.right:
            self.right.insert(freq, symbol, 1)
            return
        self.right = Node(freq, symbol, huff=1)
        self.print_tree(f"{symbol}/after_insert")

    def print_tree(self, string, dir="default", key=lambda x: x.symbol):
        dot = graphviz.Digraph(comment=string)

        dot.node(str(key(self)))
        accessed_node: Node = self

        def add_nodes_edges(accessed_node):
            if accessed_node.left:
                dot.node(str(key(accessed_node.left)))
                dot.edge(
                    str(key(accessed_node)),
                    str(key(accessed_node.left)),
                    label=str(accessed_node.huff),
                )
                add_nodes_edges(accessed_node.left)
            if accessed_node.right:
                dot.node(str(key(accessed_node.right)))
                dot.edge(
                    str(key(accessed_node)),
                    str(key(accessed_node.right)),
                    label=str(accessed_node.huff),
                )
                add_nodes_edges(accessed_node.right)

        add_nodes_edges(accessed_node)
        dot.render(string, format="png", directory=f"./graph_images/{dir}", view=False)


def construct_huffman_coding_tree(unsorted_arr: list) -> Node:
    frequencies = {}
    for item in unsorted_arr:
        if frequencies.get(item):
            frequencies[item] += 1
        else:
            frequencies[item] = 1
    tup_list = [(s, f) for s, f in zip(frequencies.values(), frequencies.keys())]
    nodes: list[Node] = []
    for item in tup_list:
        heapq.heappush(nodes, Node(item[0], item[1]))

    while len(nodes) > 1:
        # sort all the nodes in ascending order
        # based on their frequency
        left = heapq.heappop(nodes)
        right = heapq.heappop(nodes)

        # assign directional value to these nodes
        left.huff = 0
        right.huff = 1

        # combine the 2 smallest nodes to create
        # new node as their parent
        newNode = Node(left.freq + right.freq, left.symbol + right.symbol, left, right)

        heapq.heappush(nodes, newNode)
    return nodes[0]
