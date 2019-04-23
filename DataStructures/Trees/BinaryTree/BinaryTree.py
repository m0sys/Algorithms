from __future__ import annotations
from typing import Optional, List


class BinaryTree:
    """

    """

    def __init__(self, root: Optional[BinaryTree] = None) -> None:
        if root is None:
            self._root = None
            self._left = None
            self._right = None

        else:
            self._root = root
            self._left = BinaryTree()
            self._right = BinaryTree()

    def is_symmetric(self) -> bool:
        # TODO: Implement is symmetric.
        if self._left is not None and self._right is not None:
            return self._is_mirror(self._left, self._right)

        return True

    def _is_mirror(self, leftTree: BinaryTree, rightTree: BinaryTree) -> List:
        """

        :param leftTree:
        :param rightTree:
        :return:

        doctest:
        >>> left_bst = BinarySearchTree(3)
        >>> left_bst.insert(BinarySearchTree(5))
        >>> left_bst.insert(BinarySearchTree(6))

        >>> right_bst = BinarySearchTree(3)
        >>> right_bst.insert(BinarySearchTree(5))
        >>> right_bst.insert(BinarySearchTree(6))
        """
        # TODO: Implement helper function is mirror.
        if leftTree is None and rightTree is None:
            return [True]

        results = []
        if leftTree._root == rightTree._root:
            results.append(True)
            leftResult = self._is_mirror(leftTree._left, rightTree._right)
            rightResult = self._is_mirror(leftTree._right, rightTree._left)
            print("_is_mirror: leftResult = " + str(leftResult))
            print("_is_mirror: rightResult = " + str(rightResult))
            results.extend(leftResult)
            results.extend(rightResult)

        return [all(results)]
