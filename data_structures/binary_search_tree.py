from data_structures.nodes import BinaryNode


class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None
        self.count = 0

    def insert(self, data):
        new_node = BinaryNode(data)
        if self.root == None:
            self.root = new_node
            self.number_of_nodes += 1
            return
        else:
            current_node = self.root
            while (current_node.left != new_node) and (current_node.right != new_node):
                if new_node.data > current_node.data:
                    if current_node.right == None:
                        current_node.right = new_node
                    else:
                        current_node = current_node.right
                elif new_node.data < current_node.data:
                    if current_node.left == None:
                        current_node.left = new_node
                    else:
                        current_node = current_node.left
            self.number_of_nodes += 1
            return

    # Now we will implement the lookup method.
    # It will follow similar logic as to the insert method to reach the correct position.
    # Only instead of inserting a new node we will return "Found" if the node pointed by the temporary node contains the same value we are looking for
    def search(self, data):
        if self.root == None:
            return "Tree Is Empty"
        else:
            current_node = self.root
            while True:
                if current_node == None:
                    return "Not Found"
                if current_node.data == data:
                    return "Found"
                elif current_node.data > data:
                    current_node = current_node.left
                elif current_node.data < data:
                    current_node = current_node.right

    # Finally comes the very complicated remove method.
    # This one is too complicated for me to explain while writing. So I'll just write the code down with some comments
    # explaining which conditions are being checked
    def remove(self, data):
        if self.root == None:  # Tree is empty
            return "Tree Is Empty"
        current_node = self.root
        parent_node = None
        while (
            current_node != None
        ):  # Traversing the tree to reach the desired node or the end of the tree
            if current_node.data > data:
                parent_node = current_node
                current_node = current_node.left
            elif current_node.data < data:
                parent_node = current_node
                current_node = current_node.right
            else:  # Match is found. Different cases to be checked
                # Node has left child only
                if current_node.right == None:
                    if parent_node == None:
                        self.root = current_node.left
                        return
                    else:
                        if parent_node.data > current_node.data:
                            parent_node.left = current_node.left
                            return
                        else:
                            parent_node.right = current_node.left
                            return

                # Node has right child only
                elif current_node.left == None:
                    if parent_node == None:
                        self.root = current_node.right
                        return
                    else:
                        if parent_node.data > current_node.data:
                            parent_node.left = current_node.right
                            return
                        else:
                            parent_node.right = current_node.right
                            return

                # Node has neither left nor right child
                elif current_node.left == None and current_node.right == None:
                    if parent_node == None:  # Node to be deleted is root
                        current_node = None
                        return
                    if parent_node.data > current_node.data:
                        parent_node.left = None
                        return
                    else:
                        parent_node.right = None
                        return

                # Node has both left and right child
                elif current_node.left != None and current_node.right != None:
                    del_node = current_node.right
                    del_node_parent = current_node.right
                    while (
                        del_node.left != None
                    ):  # Loop to reach the leftmost node of the right subtree of the current node
                        del_node_parent = del_node
                        del_node = del_node.left
                    current_node.data = (
                        del_node.data
                    )  # The value to be replaced is copied
                    if (
                        del_node == del_node_parent
                    ):  # If the node to be deleted is the exact right child of the current node
                        current_node.right = del_node.right
                        return
                    if (
                        del_node.right == None
                    ):  # If the leftmost node of the right subtree of the current node has no right subtree
                        del_node_parent.left = None
                        return
                    else:  # If it has a right subtree, we simply link it to the parent of the del_node
                        del_node_parent.left = del_node.right
                        return
        return "Not Found"
