from trees.utility.tree_node import Node


def construct_binary_tree(arr: list) -> Node:
    root = Node(arr[0])
    for x in arr[0:]:
        root.insert(x)
    return root
