# Date: 2020/1/28.
# Implementing an AVL Tree data structure based on
# UOFT notes by Vassos Hadzilacos with some help from
# the algorithm textbook.

from typing import Union

class AvlTree:
    """A balanced AVL Tree implmentation.

    Representation Invariant:
        The root of the tree is the only node where 'self.parent' is None.
    """
    def __init__(self, key: int) -> None:
        self.key = key
        self.parent = None
        self.right = None
        self.left = None

    def insert(self, key: int) -> None:
        if self.key >= key and self.left != None:
            self.left.insert(key)
        else:
            new_node = AvlTree(key)
            new_node.parent = self.parent
            self.left = new_node

        if self.key <= key and self.right != None:
            self.right.insert(key)
        else:
            new_node = AvlTree(key)
            new_node.parent = self.parent
            self.right = new_node

    def search(self, key: int) -> AvlTree:
        # Base Cases.
        if self.key != key and self.left == None and self.right == None:
            return None

        if self.key == key:
            return self

        # Recursive Cases.
        if self.key >=  key and self.left != None:
            return self.left.search(key)

        if self.key <= key and self.right != None:
            return self.right.search(key)


    def inorder_tree_walk(self):
        if self.key != None:
            if self.left != None:
                self.left.inorder_tree_walk()
            print(self.key)
            if self.right != None:
                self.right.inorder_tree_walk()

    def preorder_tree_walk(self):
        if self.key != None:
            print(self.key)
            if self.left != None:
                self.left.inorder_tree_walk()
            if self.right != None:
                self.right.inorder_tree_walk()

    def postorder_tree_walk(self):
        if self.key != None:
            if self.left != None:
                self.left.inorder_tree_walk()
            if self.right != None:
                self.right.inorder_tree_walk()
            print(self.key)




if __name__ == "__main__":
    print("Testing AVL Trees ... \n\n")

    avl = AvlTree(3)
    avl.insert(10)
    avl.insert(20)
    avl.insert(1)
    avl.insert(2)
    avl.insert(100)
    avl.insert(5)
    avl.insert(4)
    avl.insert(3)
    avl.inorder_tree_walk()
    print("\n\n preorder walk ... \n")
    avl.preorder_tree_walk()
    print("\n\n postorder walk ... \n")
    avl.postorder_tree_walk()

