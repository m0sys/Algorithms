from __future__ import annotations
from typing import Union, Any


class BinarySearchTree:
    """
    Binary search tree (bst) data structure.

    Private Attributes
    ------------------
    _root: the root of this bst.
    """
    def __init__(self, root=None):
        if root is None:
            self._root = None
            self._parent = None
            self._left = None
            self._right = None

        else:
            self._root = root
            self._parent = BinarySearchTree(None)
            self._left = BinarySearchTree(None)
            self._right = BinarySearchTree(None)

    def __str__(self):
        return str(self._root)

    def _help_print(self, indent):
        ## return str(s
        pass

    def __contains__(self, item):
        pass

    def isEmpty(self) -> bool:
        return self._root is None

    def inorderTreeWalk(self) -> None:
        """
        Print out the tree in order from smallest to greatest.
        This takes O(n) steps where n is the size of the BST.

        :return None:
        """
        if not self.isEmpty():
            if not self._left.isEmpty():
                self._left.inorderTreeWalk()
            print(self._root)
            if not self._right.isEmpty():
                self._right.inorderTreeWalk()

    def search(self, item: Any) -> Union[BinarySearchTree, None]:
        """
        Search the tree for the first occurrence of a node containing the root
        with value <item> and return it. If no such element exists return None.
        This takes O(h) steps where h is the height of the BST.

        Parameters:
            item (Any): value we want to find

        :param item:
        :return:

        doctest:
        >>> bst = BinarySearchTree(100)
        >>> node =  bst.search(100)
        >>> node._root
        100
        >>> bst.search(1000) is None
        True
        """
        # Base Case:
        if self._root is None:
            return None

        if self._root == item:
            return self

        # Recursive Case:
        elif item < self._root:
            return self._left.search(item)
        else:
            return self._right.search(item)

    def searchItr(self, item) -> Union[BinarySearchTree, None]:
        """
        Implementation of search but in a iterative fashion.
        :param item:
        :return:

        doctest:
        >>> bst = BinarySearchTree(100)
        >>> node =  bst.searchItr(100)
        >>> node._root
        100
        >>> bst.searchItr(1000) is None
        True
        """
        x = self
        while not x.isEmpty() and x._root != item:
            if item < x._root:
                x = x._left
            else:
                x = x._right

        if x._root is None:
            return None

        return x

    def maximum(self) -> Union[int, None]:
        """
        Return the maximum value in the tree.
        This takes O(h) steps where h is the height of the BST.
        :return maxKey: the max key in this tree or None

        doctest:
        >>> bst = BinarySearchTree()
        >>> bst.maximum() is None
        True
        >>> bst.insert(BinarySearchTree(1000))
        >>> bst.maximum()
        1000
        >>> bst.insert(BinarySearchTree(2000))
        >>> bst.insert(BinarySearchTree(2500))
        >>> bst.maximum()
        2500
        >>> bst.insert(BinarySearchTree(4000))
        >>> bst.maximum()
        4000
        >>> bst.insert(BinarySearchTree(3000))
        >>> bst.maximum()
        4000
        """
        # Base Case:
        if self.isEmpty():
            return None

        # Recursive Case:
        else:
            maxKey = self._root
            if not self._right.isEmpty():
                maxKey = self._right.maximum()

            return maxKey

    def minimum(self) -> Union[int, None]:
        """
        Return the minimum value in the tree.
        This takes O(h) steps where h is the height of the BST.
        :return minKey: the min key in this tree or None

        doctest:
        >>> bst = BinarySearchTree()
        >>> bst.minimum() is None
        True
        >>> bst.insert(BinarySearchTree(1000))
        >>> bst.minimum()
        1000
        >>> bst.insert(BinarySearchTree(2000))
        >>> bst.insert(BinarySearchTree(2500))
        >>> bst.minimum()
        1000
        >>> bst.insert(BinarySearchTree(500))
        >>> bst.minimum()
        500
        >>> bst.insert(BinarySearchTree(501))
        >>> bst.minimum()
        500
        >>> bst.insert(BinarySearchTree(499))
        >>> bst.minimum()
        499
        >>> bst.insert(BinarySearchTree(1))
        >>> bst.minimum()
        1
        """
        # Base Case:
        if self.isEmpty():
            return None

        # Recursive Case:
        else:
            minKey = self._root

            if not self._left.isEmpty():
                minKey = self._left.minimum()

            return minKey

    def findSuccessor(self, x):
        """
        A successor of a tree is the smallest element in the branch right of the
        root. That is the successor of any node in the BST is the smallest key
        node its' right branch.

        :param x: node in this tree
        :return:

        doctest:
        >>> bst = BinarySearchTree(5)
        >>> bst.insert(BinarySearchTree(10))
        >>> bst.insert(BinarySearchTree(15))
        >>> bst.insert(BinarySearchTree(8))
        >>> bst.insert(BinarySearchTree(4)) >>> bst.insert(BinarySearchTree(3)) >>> bst.insert(BinarySearchTree(2))
        >>> bst.insert(BinarySearchTree(1))
        >>> subtree1 = bst.search(1)
        >>> assert()
        """

        # TODO: Test and Understand find successor.
        if x.isEmpty():
            return None
        else:
            ## x = self
            if not x._right.isEmpty():
                return self._right.findSuccessor()
            y = self._parent
            while y is not None and x == y._right:
                x = y
                y = y._parent

            return y

    def findNode(self, level: int, pos: int) -> Union[BinarySearchTree, None]:
        """
        Find node at position <pos> in level <level>.

        Preconditions:
        --------------
        level >= 1 and pos >= 1.

        pos is counted from left to right, and it includes counting missing
        nodes as well.

        :param level: height where the node is to be found.
        :param pos:  position counted from left to right where the node is to
                     be found.
        :return:

        doctest:
        >>> bst = BinarySearchTree(5)
        >>> bst.insert(BinarySearchTree(10))
        >>> bst.insert(BinarySearchTree(4))
        >>> bst.insert(BinarySearchTree(8))
        >>> bst.insert(BinarySearchTree(15))
        >>> bst.insert(BinarySearchTree(3))
        >>> bst.insert(BinarySearchTree(1))
        >>> bst.insert(BinarySearchTree(2))

        >>> bst.findNode(1, 1).getRoot()
        5
        >>> bst.findNode(2, 1).getRoot()
        4
        >>> bst.findNode(2, 2).getRoot()
        10
        >>> bst.findNode(3, 3).getRoot()
        8
        >>> bst.findNode(4,1).getRoot()
        1
        """
        # Debug
        toPrint = False
        # Base cases:
        if not self.isEmpty() and level == 1 and pos == 1:
            return self

        if not self.isEmpty() and level == 2 and pos == 1:
            if toPrint:
                print("findNode: level is 2 and pos is 1!")
            return self._left

        elif not self.isEmpty() and level == 2 and pos == 2:
            if toPrint:
                print("findNode: level is 2 and pos is 2!")
            return self._right

        elif self.isEmpty():
            return None

        # Recursive case:
        else:
            if pos > 2 ** (level - 1) / 2:
                return self._right.findNode(level - 1, pos - 2 ** (level - 1) / 2)

            return self._left.findNode(level - 1, pos)

    def insert(self, node: BinarySearchTree) -> None:
        """
        Insert <node> into Tree while keeping the bst property.
        This takes O(h) steps where h is the height of the BST.
        :param node: the node to be inserted

        :return: None

        doctest:
        >>> bst = BinarySearchTree(2)
        >>> bst.insert(BinarySearchTree(399))
        >>> bst.insert(BinarySearchTree(387))
        >>> bst.insert(BinarySearchTree(219))
        >>> bst.insert(BinarySearchTree(266))
        >>> bst.insert(BinarySearchTree(382))
        >>> bst.insert(BinarySearchTree(381))
        >>> bst.insert(BinarySearchTree(278))
        >>> bst.insert(BinarySearchTree(363))
        >>> bst.getRoot()
        2
        >>> bst.getRight().getRoot()
        399
        >>> bst.getRight().getLeft().getRoot()
        387
        >>> bst.getRight().getLeft().getLeft().getRoot()
        219
        """
        y = None
        x = self

        while x is not None and not x.isEmpty():
            y = x
            if node._root < x._root:
                x = x._left
            else:
                x = x._right

        node._parent = y
        if y is None:  # Empty tree
            self._root = node._root
            self._left = node._left
            self._right = node._right
            self._parent = BinarySearchTree(None)

        elif node._root < y._root:
            y._left = node

        else:
            y._right = node

    def insert_recursive(self, node: BinarySearchTree) -> None:
        """
        Insert implemented recursively.

        :param node: the node to be inserted.
        :return:

        doctest:
        >>> bst = BinarySearchTree(2)
        >>> bst.insert_recursive(BinarySearchTree(399))
        >>> bst.insert_recursive(BinarySearchTree(387))
        >>> bst.insert_recursive(BinarySearchTree(219))
        >>> bst.insert_recursive(BinarySearchTree(266))
        >>> bst.insert_recursive(BinarySearchTree(382))
        >>> bst.insert_recursive(BinarySearchTree(381))
        >>> bst.insert_recursive(BinarySearchTree(278))
        >>> bst.insert_recursive(BinarySearchTree(363))
        >>> bst.getRoot()
        2
        >>> bst.getRight().getRoot()
        399
        >>> bst.getRight().getLeft().getRoot()
        387
        >>> bst.getRight().getLeft().getLeft().getRoot()
        219
        """
        if self.isEmpty():
            self._root = node._root
            self._right = node._right
            self._left = node._left

        else:
            if self._root < node._root:
                self._right.insert_recursive(node)

            else:
                self._left.insert_recursive(node)

    def insert_subtree(self, subtree: BinarySearchTree) -> None:
        # TODO: Implement insert subtree.
        pass

    def delete(self, node: BinarySearchTree) -> None:
        # TODO: Implement delete.
        pass

    def delete_recursive(self, node: BinarySearchTree) -> None:
        # TODO: Implement delete recursively.
        """

        :param node:
        :return:
        """
        pass


    def getRoot(self):
        return self._root

    def getLeft(self):
        return self._left

    def getRight(self):
        return self._right

    def getParent(self):
        return self._parent

