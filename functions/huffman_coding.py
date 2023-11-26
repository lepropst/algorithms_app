from data_structures.huffman_coding import construct_huffman_coding_tree


def huffman_coding(data):
    node_one = construct_huffman_coding_tree(data.get("string_one"))
    node_one.print_tree("sample")
