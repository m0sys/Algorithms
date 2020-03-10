# Date: 2020/2/1.
# Implementing a BST data structure based on the
# algorithm textbook.

from __future__ import annotations
class BST:
    """A Binary Search Tree implementation.

    Representation Invariant:
        - The root of the tree is the only node where 'self.parent' is None.

        Binary Search Property:
        - All nodes in the left subtree is less than or equal to self.
        - All nodes in the right subtree is greater than or equal to self.
    """
    def __init__(self, key: int) -> None:
        self.key = key
        self.parent = None
        self.right = None
        self.left = None

    def insert_node(self, node: BST) -> None:
        if self.key >= self.node.key:
            if self.left is not None:
                self.left.insert_node(node)
            else:
                node.parent = self
                self.left = node

        else:
            if self.right is not None:
                self.right.insert_node(node)
            else:
                node.parent = self
                self.right = node


    def insert_node_iter(self, node: BST) -> None:
        y = None
        x = self
        while x is not None:
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right
        node.parent = y

        # y will never be empty given that root is never empty,
        # and y will have the child where node must be insert into empty.
        if node.key < y.key:
            y.left = node
        else:
            y.right = node



    def insert(self, key: int) -> None:
        if self.key >= key:
            if self.left is not None:
                self.left.insert(key)
            else:
                new_node = BST(key)
                new_node.parent = self
                self.left = new_node

        elif self.key <= key:
            if self.right is not None:
                self.right.insert(key)
            else:
                new_node = BST(key)
                new_node.parent = self
                self.right = new_node


    def delete_node(self) -> None:
        ## print("Self key: " + str(self.key))
        if self.left is None:
            # Replace self with right child.
            self._transplant(self.right)

        elif self.right is None:
            self._transplant(self.left)
        else:
            # Both children available. find successor.
            successor = self.successor()
            self.key, successor.key = successor.key, self.key
            successor.delete_node()
            ## if successor != self.right:
            ##     # replace successor with its right subtree.
            ##     successor._transplant(successor.right)
            ##     successor.right = self.right
            ##     successor.right.parent = successor
            ## # replace self with successor.
            ## print("self.left: " + str(self.left.key))
            ## self._transplant(successor)
            ## print("self.left after transplant: " + str(self.left.key))
            ## successor.left = self.left
            ## successor.left.parent = successor


    def right_rotate(self) -> BST:
        """Rotate right.


        Preconditions:
            - self has a left subtree.

        Return the success of the self.
        i.e. the node that has replaced self. (left child of self)
        """
        p = self.parent
        b = self.left # the successor of self
        self.left = b.right
        if b.right is not None:
            b.right.parent = self
        b.right = self # point successor right node to self
        # Update parent down line.
        if p is not None:
            if p.left == self:
                p.left = b
            else:
                p.right = b
        return b


    def left_rotate(self) -> BST:
        """Rotate left.

        Preconditions:
            - self has a right subtree.

        Return the successor of self.
        i.e the node that replaced self. (right child of self)

        """
        p = self.parent
        b = self.right
        self.right = b.left
        if b.left is not None:
            b.left.parent = self
        b.left = self
        # Update parent down line.
        if parent is not None:
            if p.left == self:
                p.left = b
            else:
                p.right = b

        return b


    def search(self, key: int) -> BST:
        """Find the sub bst with key 'key'.
        """
        # Base Cases.
        if self.key != key and self.left == None and self.right == None:
            return None

        if self.key == key:
            return self

        # Recursive Cases.
        if self.key >=  key and self.left is not None:
            return self.left.search(key)

        if self.key <= key and self.right is not None:
            return self.right.search(key)

    def minimum(self) -> BST:
        tmp = self
        while tmp.left != None:
            tmp = tmp.left
        return tmp

    def min_recursive(self) -> BST:
        if self.left is not None:
            return self.left.min_recursive()
        return self

    def maximum(self) -> BST:
        tmp = self
        while tmp.right != None:
            tmp = tmp.right
        return tmp

    def max_recursive(self) -> BST:
        if self.right is not None:
            return self.right.max_recursive()
        return self

    def successor(self) -> BST:
        """Return the success of this BST.

        The successor of a node x is the node with the smallest key greater than 'self.key'.
        """
        if self.right is not None:
            return self.right.minimum()

        x = self
        y = x.parent
        while y is not None and x == y.right:
            x = y
            y = y.parent
        return y


    def predecessor(self) -> BST:
        """Return the predecessor of this BST.

        The predecessor of a node x is the node that is largest key smaller than 'self.key'.
        """
        if self.left is not None:
            return self.left.maximum()

        x = self
        y = x.parent
        while y is not None and x == y.left:
            x = y
            y = y.parent
        return y


    def inorder_tree_walk(self):
        if self.left != None:
            self.left.inorder_tree_walk()
        print(self.key)
        if self.right != None:
            self.right.inorder_tree_walk()


    def _transplant(self, v: BST) -> None:
        """Replace self with subtree v.

        Preconditions:
            - v must be subtree.
        """
        if self.parent is None:
            # Self is the root of the tree.
            if v is not None:
                self.key = v.key
                self.right = v.right
                self.left = v.left
                ## v.left = None
                ## v.right = None
            else:
                self.key = None
                self.right = None
                self.left = None

        elif self == self.parent.left:
            self.parent.left = v
        else:
            self.parent.right = v

        if v is not None:
            v.parent = self.parent

    def _validate_bst(self):
        stack = [(root, float('-inf'), float('inf')), ]
        while stack:
            root, lower, upper = stack.pop()
            if not root:
                continue
            val = root.val
            if val <= lower or val >= upper:
                return False
            stack.append((root.right, val, upper))
            stack.append((root.left, lower, val))
        return True

    def _check_rep_inv(self) -> None:
        """
        Check ds representation invariant each time you update the tree.
        """
        if self.left is not None:
            assert(self.left.key <= self.key)
            self.left._check_rep_inv()
        if self.right is not None:
            assert(self.right.key >= self.key)
            self.right._check_rep_inv()



    ## def preorder_tree_walk(self):
    ##     if self.key != None:
    ##         print(self.key)
    ##         if self.left != None:
    ##             self.left.inorder_tree_walk()
    ##         if self.right != None:
    ##             self.right.inorder_tree_walk()

    ## def postorder_tree_walk(self):
    ##     if self.key != None:
    ##         if self.left != None:
    ##             self.left.inorder_tree_walk()
    ##         if self.right != None:
    ##             self.right.inorder_tree_walk()
    ##         print(self.key)


if __name__ == "__main__":
    print("Testing BST ... \n\n")

    bst = BST(3)
    bst.insert(10)
    bst.insert(20)
    bst.insert(1)
    bst.insert(2)
    bst.insert(100)
    bst.insert(5)
    bst.insert(4)
    bst.insert(3)
    ## print("\n\n inorder walk ... \n")
    ## bst.inorder_tree_walk()

