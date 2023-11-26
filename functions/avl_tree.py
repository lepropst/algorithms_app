from data_structures.avl_tree import AVLTree
from data_structures.keys import keys


def avl_tree(data):
    t = AVLTree()
    if data:
        for datum in data.get(keys[0]):
            t.insert(datum)
    t.print_tree("example.png")
