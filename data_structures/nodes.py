import copy


class PlainNode:
    def __init__(self, data):
        self.data = data


class BinaryNode(PlainNode):
    def __init__(self, data):
        super().__init__(data)
        self.left = None
        self.right = None


class GraphNode(PlainNode):
    def __init__(self, data, v=[]):
        super().__init__(copy.deepcopy(data))
        self.vertices = copy.deepcopy(v)

    def __str__(self) -> str:
        return f"{self.data}\t{[x.data for x in self.vertices]}"
