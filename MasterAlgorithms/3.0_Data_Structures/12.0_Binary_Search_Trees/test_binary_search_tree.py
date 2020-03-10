from __future__ import annotations
import unittest
from binary_search_tree import *
import random

# GLOBAL CONSTANTS.
MAX_RANDOM = 5000
MIN_RANDOM = 1

class Test(unittest.TestCase):
    def test_insert(self):
        bst = BST(10)
        actual = bst.key
        expected = 10
        self.assertEqual(actual, expected)

        # Test 1: insert into right child.
        bst.insert(100)
        bst._check_rep_inv()
        actual = bst.right.key
        expected = 100
        self.assertEqual(actual, expected)

        # Test #2: insert into left child.
        bst.insert(6)
        actual = bst.left.key
        expected = 6
        self.assertEqual(actual, expected)

        # Test #3: insert into left left child.
        bst.insert(5)
        bst._check_rep_inv()
        actual = bst.left.left.key
        expected = 5
        self.assertEqual(actual, expected)

        # Test #4: insert into left right child.
        bst.insert(7)
        bst._check_rep_inv()
        actual = bst.left.right.key
        expected = 7
        self.assertEqual(actual, expected)

    def test_insert_node_ter(self) -> None:
        stack = [67, 19, 14, 9, 76, 54, 23, 12, 72, 17, 50]
        bst = None
        while stack != []:
            if bst is None:
                bst = BST(stack.pop())
            else:
                bst.insert_node_iter(BST(stack.pop()))

        actual = bst.key
        expected = 50
        self.assertEqual(actual, expected)

        # Left subtree.
        actual = bst.left.key
        expected = 17
        self.assertEqual(actual, expected)

        actual = bst.right.key
        expected = 72
        self.assertEqual(actual, expected)

        actual = bst.left.left.key
        expected = 12
        self.assertEqual(actual, expected)

        actual = bst.left.right.key
        expected = 23
        self.assertEqual(actual, expected)

        actual = bst.left.left.left.key
        expected = 9
        self.assertEqual(actual, expected)

        actual = bst.left.left.right.key
        expected = 14
        self.assertEqual(actual, expected)

        actual = bst.left.right.right
        expected = None
        self.assertEqual(actual, expected)

        actual = bst.left.right.left.key
        expected = 19
        self.assertEqual(actual, expected)

        # Right subtree.
        actual = bst.right.key
        expected = 72
        self.assertEqual(actual, expected)

        actual = bst.right.left.key
        expected = 54
        self.assertEqual(actual, expected)

        actual = bst.right.right.key
        expected = 76
        self.assertEqual(actual, expected)

        actual = bst.right.left.left
        expected = None
        self.assertEqual(actual, expected)

        actual = bst.right.left.right.key
        expected = 67
        self.assertEqual(actual, expected)

        actual = bst.right.right.left
        expected = None
        self.assertEqual(actual, expected)

        actual = bst.right.right.right
        expected = None
        self.assertEqual(actual, expected)

        bst._check_rep_inv()


    def test_rotate_right(self):
        # TODO Write down tests.
        pass


    def test_rotate_left(self):
        # TODO: Write down tests.
        pass


    def test_search(self):
        bst = self._build_balanced_bst()

        # Test #1: search root.
        actual = bst.search(50).key
        expected = 50
        self.assertEqual(actual, expected)

        # Test #2: find right left most child.
        actual = bst.search(67).key
        expected = 67
        self.assertEqual(actual, expected)

        # Test #3: find null.
        actual = bst.search(1000000)
        expected = None
        self.assertEqual(actual, expected)

        # Test #4: find min.
        actual = bst.search(9).key
        expected = 9
        self.assertEqual(actual, expected)

        # Test #5: find max.
        actual = bst.search(76).key
        expected = 76
        self.assertEqual(actual, expected)


    def test_minimum(self):
        bst = self._build_balanced_bst()

        # Test #1: find min of root.
        actual = bst.minimum().key
        expected = 9
        self.assertEqual(actual, expected)

        # Test #2: find min of left child of root.
        x = bst.search(17)
        actual = x.minimum().key
        expected = 9
        self.assertEqual(actual, expected)

        # Test #3: find min of right child of root.
        x = bst.search(72)
        actual = x.minimum().key
        expected = 54
        self.assertEqual(actual, expected)

        # Test #4: find min of node with no left child.
        x = bst.search(54)
        actual = x.minimum().key
        expected = 54
        self.assertEqual(actual, expected)

    def test_min_recursive(self):
        bst = self._build_balanced_bst()

        # Test #1: find min of root.
        actual = bst.min_recursive().key
        expected = 9
        self.assertEqual(actual, expected)

        # Test #2: find min of left child of root.
        x = bst.search(17)
        actual = x.min_recursive().key
        expected = 9
        self.assertEqual(actual, expected)

        # Test #3: find min of right child of root.
        x = bst.search(72)
        actual = x.min_recursive().key
        expected = 54
        self.assertEqual(actual, expected)

        # Test #4: find min of node with no left child.
        x = bst.search(54)
        actual = x.min_recursive().key
        expected = 54
        self.assertEqual(actual, expected)


    def test_max_recursive(self):
        bst = self._build_balanced_bst()

        # Test #1: find max of root.
        actual = bst.max_recursive().key
        expected = 76
        self.assertEqual(actual, expected)

        # Test #2: find max of left child of root.
        x = bst.search(17)
        actual = x.max_recursive().key
        expected = 23
        self.assertEqual(actual, expected)

        # Test #3: find max of right child of root.
        x = bst.search(72)
        actual = x.max_recursive().key
        expected = 76
        self.assertEqual(actual, expected)

        # Test #4: find max of node with no right child.
        x = bst.search(19)
        actual = x.max_recursive().key
        expected = 19
        self.assertEqual(actual, expected)


    def test_maximum(self):
        bst = self._build_balanced_bst()

        # Test #1: find max of root.
        actual = bst.maximum().key
        expected = 76
        self.assertEqual(actual, expected)

        # Test #2: find max of left child of root.
        x = bst.search(17)
        actual = x.maximum().key
        expected = 23
        self.assertEqual(actual, expected)

        # Test #3: find max of right child of root.
        x = bst.search(72)
        actual = x.maximum().key
        expected = 76
        self.assertEqual(actual, expected)

        # Test #4: find max of node with no right child.
        x = bst.search(19)
        actual = x.maximum().key
        expected = 19
        self.assertEqual(actual, expected)


    def test_successor(self):
        bst = self._build_balanced_bst()

        # Test #1: find successor of root.
        # Result: the success is the min of right child of root.
        actual = bst.successor().key
        expected = 54
        self.assertEqual(actual, expected)

        # Test #2: find successor of left child.
        # Result: the succesor is the min of right child, same case as if you have right child.
        x = bst.search(17)
        actual = x.successor().key
        expected = 19
        self.assertEqual(actual, expected)

        # Test #3: find successor of no right child node and right child of parent.
        # Result: the successor in this case is the grandparent of x given that the parent of x
        # is the left child of the grandparent. Othewise x does not have a successor.
        x = bst.search(23)
        actual = x.successor().key
        expected = 50
        self.assertEqual(actual, expected)

        # Test #4: find successor of no right and left child of parent.
        # Result: the successor in this casse is the parent of x.
        x = bst.search(9)
        actual = x.successor().key
        expected = 12
        self.assertEqual(actual, expected)

        # Test #4: find successor of no right child node and right child of parent with parent
        #          at right child of grandparent.
        # Result: x does not have a succesor. It should have had a stronger child.
        x = bst.search(76)
        actual = x.successor()
        expected = None
        self.assertEqual(actual, expected)

    def test_predecessor(self) -> None:
        pass



    def test_delete_node(self) -> None:
        bst = self._build_balanced_bst()

        # Test #0: Remove root.
        bst.delete_node()
        bst._check_rep_inv()
        actual = bst.key
        expected = 54
        ## self.assertEqual(actual, expected)

        # Test #1: Remove node with no children.
        bst = self._build_balanced_bst()
        x = bst.search(76)
        x.delete_node()
        bst._check_rep_inv()
        actual = bst.right.right
        expected = None
        self.assertEqual(actual, expected)

        # Test #2: Remove node with just one child.
        bst = self._build_balanced_bst()
        x = bst.search(54) # right child
        x.delete_node()
        bst._check_rep_inv()
        actual = bst.right.left.key
        expected = 67
        self.assertEqual(actual, expected)

        bst = self._build_balanced_bst()
        x = bst.search(23) # left child
        x.delete_node()
        bst._check_rep_inv()
        actual = bst.left.right.key
        expected = 19
        self.assertEqual(actual, expected)

        # Test #3: Remove node with two children.

        # part I: right child of node is the successor.
        bst = self._build_balanced_bst()
        x = bst.search(72)
        x.delete_node()
        bst._check_rep_inv()
        actual = bst.right.key
        expected = 76
        self.assertEqual(actual, expected)

        # part II: the min node of right child is the successor.
        bst = self._build_balanced_bst()
        x = bst.search(17)
        x.delete_node()
        bst._check_rep_inv()
        actual = bst.left.key
        expected = 19
        self.assertEqual(actual, expected)

    def test_transpant(self) -> None:
        bst = self._build_balanced_bst()

        # Transpant root with new_node.
        x = bst.search(17)
        bst._transplant(x)
        actual = bst.key
        expected = 17
        self.assertEqual(actual, expected)
        actual = bst.left.key
        expected = 12
        actual = bst.right.key
        expected = 23
        self.assertEqual(actual, expected)

        # Transpant non root element with left child.
        bst = self._build_balanced_bst()
        x = bst.search(17)
        v = bst.search(12)
        x._transplant(v)

        node = bst.left
        actual = node.key
        expected = 12
        self.assertEqual(actual, expected)
        actual = node.left.key
        expected = 9
        actual = node.right.key
        expected = 14
        self.assertEqual(actual, expected)
        actual = node.parent.key
        expected = 50
        self.assertEqual(actual, expected)

        # TODO: Transpant non root element with right child.
        bst = self._build_balanced_bst()
        x = bst.search(17)
        v = bst.search(23)
        x._transplant(v)

        node = bst.left
        actual = node.key
        expected = 23
        self.assertEqual(actual, expected)
        actual = node.left.key
        expected = 19
        actual = node.right
        expected = None
        self.assertEqual(actual, expected)
        actual = node.parent.key
        expected = 50
        self.assertEqual(actual, expected)



    def  _build_random_bst(self) -> BST:
        head = random.randint(MIN_RANDOM, MAX_RANDOM)
        bst = BST(head)
        for i in range(20):
            bst.insert(random.randint(MIN_RANDOM, MAX_RANDOM))

        bst._check_rep_inv()


    def _build_balanced_bst(self) -> BST:
        bst = BST(50)
        arr = [17, 72, 12, 23, 54, 76, 9, 14, 19, 67]
        for elem in arr:
            bst.insert(elem)
        return bst


    def test_build_balanced_bst(self):
        bst = self._build_balanced_bst()

        actual = bst.key
        expected = 50
        self.assertEqual(actual, expected)

        # Left subtree.
        actual = bst.left.key
        expected = 17
        self.assertEqual(actual, expected)

        actual = bst.right.key
        expected = 72
        self.assertEqual(actual, expected)

        actual = bst.left.left.key
        expected = 12
        self.assertEqual(actual, expected)

        actual = bst.left.right.key
        expected = 23
        self.assertEqual(actual, expected)

        actual = bst.left.left.left.key
        expected = 9
        self.assertEqual(actual, expected)

        actual = bst.left.left.right.key
        expected = 14
        self.assertEqual(actual, expected)

        actual = bst.left.right.right
        expected = None
        self.assertEqual(actual, expected)

        actual = bst.left.right.left.key
        expected = 19
        self.assertEqual(actual, expected)

        # Right subtree.
        actual = bst.right.key
        expected = 72
        self.assertEqual(actual, expected)

        actual = bst.right.left.key
        expected = 54
        self.assertEqual(actual, expected)

        actual = bst.right.right.key
        expected = 76
        self.assertEqual(actual, expected)

        actual = bst.right.left.left
        expected = None
        self.assertEqual(actual, expected)

        actual = bst.right.left.right.key
        expected = 67
        self.assertEqual(actual, expected)

        actual = bst.right.right.left
        expected = None
        self.assertEqual(actual, expected)

        actual = bst.right.right.right
        expected = None
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
