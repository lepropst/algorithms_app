from data_structures.nodes import BinaryNode
import graphviz


class AVLTree:
    def __init__(self, *args):
        self.node = None

        self.height = -1
        self.balance = 0

        if len(args) == 1:
            self.root = self.insert(args[0][0])

    def height(self):
        if self.node:
            return self.node.height
        else:
            return 0

    def is_leaf(self):
        return self.height == 0

    def insert(self, data: str):
        tree = self.node
        newnode = BinaryNode(data)
        if tree == None:
            self.node = newnode
            self.node.left = AVLTree()
            self.node.right = AVLTree()
            print("Inserted data [" + str(data) + "]")

        elif data < tree.data:
            self.node.left.insert(data)

        elif data > tree.data:
            self.node.right.insert(data)

        else:
            print("Key [" + str(data) + "] already in tree.")

        self.rebalance(self.node.data)

    def rebalance(self, name):
        """
        Rebalance a particular (sub)tree
        """
        # data inserted. Let's check if we're balanced
        self.update_heights(False)
        self.update_balances(False)
        while self.balance < -1 or self.balance > 1:
            if self.balance > 1:
                if self.node.left.balance < 0:
                    self.node.left.lrotate(name)  # we're in case II
                    self.update_heights()
                    self.update_balances()

                self.rrotate(name)
                self.update_heights()
                self.update_balances()

            if self.balance < -1:
                if self.node.right.balance > 0:
                    self.node.right.rrotate(name)  # we're in case III
                    self.update_heights()
                    self.update_balances()

                self.lrotate(name)
                self.update_heights()
                self.update_balances()

    def rrotate(self, name):
        # Rotate left pivoting on self
        print("Rotating " + str(self.node.data) + " right")
        self.print_tree("before_rotating_" + str(self.node.data) + "_right", name)
        A = self.node
        B = self.node.left.node
        T = B.right.node
        self.node = B
        B.right.node = A
        A.left.node = T
        self.print_tree("after_rotating_" + str(self.node.data) + "_right", name)

    def lrotate(self, name):
        # Rotate left pivoting on self
        print("Rotating " + str(self.node.data) + " left")
        self.print_tree(f"before_lrotate {self.node.data}", name)
        A = self.node
        B = self.node.right.node
        T = B.left.node

        self.node = B
        B.left.node = A
        A.right.node = T
        self.print_tree(f"after_lrotate {self.node.data}", name)

    def update_heights(self, recurse=True):
        if not self.node == None:
            if recurse:
                if self.node.left != None:
                    self.node.left.update_heights()
                if self.node.right != None:
                    self.node.right.update_heights()

            self.height = max(self.node.left.height, self.node.right.height) + 1
        else:
            self.height = -1

    def update_balances(self, recurse=True):
        if not self.node == None:
            if recurse:
                if self.node.left != None:
                    self.node.left.update_balances()
                if self.node.right != None:
                    self.node.right.update_balances()

            self.balance = self.node.left.height - self.node.right.height
        else:
            self.balance = 0

    def delete(self, data, name):
        # print("Trying to delete at node: " + str(self.node.data))
        if self.node != None:
            if self.node.data == data:
                print("Deleting ... " + str(data))
                if self.node.left.node == None and self.node.right.node == None:
                    self.node = None  # leaves can be killed at will
                # if only one subtree, take that
                elif self.node.left.node == None:
                    self.node = self.node.right.node
                elif self.node.right.node == None:
                    self.node = self.node.left.node

                # worst-case: both children present. Find logical successor
                else:
                    replacement = self.logical_successor(self.node)
                    if replacement != None:  # sanity check
                        print(
                            "Found replacement for "
                            + str(data)
                            + " -> "
                            + str(replacement.data)
                        )
                        self.node.data = replacement.data

                        # replaced. Now delete the data from right child
                        self.node.right.delete(replacement.data, name=name)

                self.rebalance(name)
                return
            elif data < self.node.data:
                self.node.left.delete(data, name)
            elif data > self.node.data:
                self.node.right.delete(data, name)

            self.rebalance(name=name)
        else:
            return

    def logical_predecessor(self, node):
        """
        Find the biggest dataued node in LEFT child
        """
        node = node.left.node
        if node != None:
            while node.right != None:
                if node.right.node == None:
                    return node
                else:
                    node = node.right.node
        return node

    def logical_successor(self, node):
        """
        Find the smallese dataued node in RIGHT child
        """
        node = node.right.node
        if node != None:  # just a sanity check
            while node.left != None:
                print("LS: traversing: " + str(node.data))
                if node.left.node == None:
                    return node
                else:
                    node = node.left.node
        return node

    def check_balanced(self):
        if self == None or self.node == None:
            return True

        # We always need to make sure we are balanced
        self.update_heights()
        self.update_balances()
        return (
            (abs(self.balance) < 2)
            and self.node.left.check_balanced()
            and self.node.right.check_balanced()
        )

    def _inorder_traverse(self, datas):
        if self.node is None:
            return datas

        if self.node.left is not None:
            self.node.left._inorder_traverse(datas)
        if self.node is not None:
            datas.append(self.node.data)
        if self.node.right is not None:
            self.node.right._inorder_traverse(datas)
        return datas

    def _preorder_traverse(self, datas):
        if self.node is None:
            return datas
        if self.node is not None:
            datas.append(self.node.data)
        if self.node.left is not None:
            self.node.left._preorder_traverse(datas)
        if self.node.right is not None:
            self.node.right._preorder_traverse(datas)
        return datas

    def _postorder_traverse(self, datas):
        if self.node is None:
            return datas
        if self.node.left is not None:
            self.node.left._postorder_traverse(datas)
        if self.node.right is not None:
            self.node.right._postorder_traverse(datas)
        if self.node is not None:
            datas.append(self.node.data)
        return datas

    def print_tree(self, string, dir="default"):
        self.update_heights()  # Must update heights before balances
        self.update_balances()
        dot = graphviz.Digraph(comment=string)
        if self.node:
            dot.node(str(self.node.data))
            accessed_node = self.node

            def add_nodes_edges(accessed_node):
                if accessed_node.left.node:
                    dot.node(str(accessed_node.left.node.data))
                    dot.edge(str(accessed_node.data), str(accessed_node.left.node.data))
                    add_nodes_edges(accessed_node.left.node)
                if accessed_node.right.node:
                    dot.node(str(accessed_node.right.node.data))
                    dot.edge(
                        str(accessed_node.data), str(accessed_node.right.node.data)
                    )
                    add_nodes_edges(accessed_node.right.node)

            add_nodes_edges(accessed_node)
            dot.render(
                string, format="png", directory=f"./graph_images/avl/{dir}", view=False
            )
