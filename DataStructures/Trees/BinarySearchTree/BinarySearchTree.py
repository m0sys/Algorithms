from __future__ import annotations
from typing import Union, Any


class BinarySearchTree:
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

        return x

    def maximum(self) -> Union[int, None]:
        """
        Return the maximum value in the tree.
        This takes O(h) steps where h is the height of the BST.
        :return maxKey: the max key in this tree or None
        """
        # Base Case:
        if self.isEmpty():
            return None

        # Recursive Case:
        else:
            maxKey = self._root
            if self._right is not None:
                maxKey = self._right.maximum()

            return maxKey

    def minimum(self) -> Union[int, None]:
        """
        Return the minimum value in the tree.
        This takes O(h) steps where h is the height of the BST.
        :return minKey: the min key in this tree or None
        """
        # Base Case:
        if self.isEmpty():
            return None

        # Recursive Case:
        else:
            minKey = self._root

            if self._left is not None:
                minKey = self._left.maximum()

            return minKey

    def findSuccessor(self):
        """
        A successor of a tree is the smallest element in the branch right of the
        root. That is the successor of any node in the BST is the smallest key
        node its' right branch.

        :return:
        """
        if self.isEmpty():
            return None
        else:
            x = self
            if not self._right.isEmpty():
                return self._right.findSuccessor()
            y = self._parent
            while y is not None and x == y._right:
                x = y
                y = y._parent

            return y

    def insert(self, node: BinarySearchTree) -> None:
        """
        Insert <node> into Tree while keeping the bst property.
        This takes O(h) steps where h is the height of the BST.
        :param node: the node to be inserted
        :return: None
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
        if y is None: # Empty tree
            self._root = node._root
            self._left = node._left
            self._right = node._right

        elif node._root < y._root:
            y._left = node

        else:
            y._right = node

    def getRoot(self):
        return self._root

    def getLeft(self):
        return self._left

    def getRight(self):
        return self._right

    def getParent(self):
        return self._parent
