from __future__ import annotations
from typing import Any
from BinarySearchTree import *
from random import randint

START_OF_VALUES = 100
END_OF_VALUES = 2500


def test_search() -> None:
    _print_test_start('test_search')
    passes = []
    bst = BinarySearchTree(1000)
    bst.insert(BinarySearchTree(200))
    bst.insert(BinarySearchTree(100))
    bst.insert(BinarySearchTree(50))
    bst.insert(BinarySearchTree(25))
    bst.insert(BinarySearchTree(20))
    bst.insert(BinarySearchTree(1050))
    bst.insert(BinarySearchTree(1200))
    bst.insert(BinarySearchTree(1250))
    bst.insert(BinarySearchTree(1300))
    bst.insert(BinarySearchTree(1400))
    bst.insert(BinarySearchTree(1320))
    bst.insert(BinarySearchTree(2000))
    bst.insert(BinarySearchTree(1))
    bst.insert(BinarySearchTree(23))

    # Test #1
    actual = bst.search(200)
    expected = 200
    passes.append(_print_test_result(1, expected, actual._root))

    # Test #2
    actual = bst.search(1000)
    expected = 1000
    passes.append(_print_test_result(2, expected, actual._root))

    # Test #3
    actual = bst.search(5000)
    expected = None
    passes.append(_print_test_result(3, expected, actual))

    _print_test_status(all(passes), 'test_search')


def test_maximum() -> None:
    _print_test_start('test_maximum')
    passes = []
    bst = BinarySearchTree(1000)
    bst.insert(BinarySearchTree(200))
    bst.insert(BinarySearchTree(100))
    bst.insert(BinarySearchTree(50))
    bst.insert(BinarySearchTree(25))
    bst.insert(BinarySearchTree(20))
    bst.insert(BinarySearchTree(1050))
    bst.insert(BinarySearchTree(1200))
    bst.insert(BinarySearchTree(1250))
    bst.insert(BinarySearchTree(1300))
    bst.insert(BinarySearchTree(1400))
    bst.insert(BinarySearchTree(1320))
    bst.insert(BinarySearchTree(2000))
    bst.insert(BinarySearchTree(1))
    bst.insert(BinarySearchTree(23))

    # Test #1
    expected = 2000
    actual = bst.maximum()
    passes.append(_print_test_result(1, expected, actual))

    # Test #2
    bst.insert(BinarySearchTree(2001))
    bst.insert(BinarySearchTree(1999))
    expected = 2001
    actual = bst.maximum()
    passes.append(_print_test_result(2, expected, actual))

    _print_test_status(all(passes), 'test_maximum')


def test_minimum() -> None:
    _print_test_start('test_maximum')
    passes = []
    bst = BinarySearchTree(1000)
    bst.insert(BinarySearchTree(200))
    bst.insert(BinarySearchTree(100))
    bst.insert(BinarySearchTree(50))
    bst.insert(BinarySearchTree(25))
    bst.insert(BinarySearchTree(20))
    bst.insert(BinarySearchTree(1050))
    bst.insert(BinarySearchTree(1200))
    bst.insert(BinarySearchTree(1250))
    bst.insert(BinarySearchTree(1300))
    bst.insert(BinarySearchTree(1400))
    bst.insert(BinarySearchTree(1320))
    bst.insert(BinarySearchTree(2000))
    bst.insert(BinarySearchTree(53))
    bst.insert(BinarySearchTree(23))

    # Test #1
    expected = 20
    actual = bst.minimum()
    passes.append(_print_test_result(1, expected, actual))

    # Test #2
    bst.insert(BinarySearchTree(21))
    expected = 20
    actual = bst.minimum()
    passes.append(_print_test_result(2, expected, actual))

    # Test #3
    bst.insert(BinarySearchTree(19))
    expected = 19
    actual = bst.minimum()
    passes.append(_print_test_result(3, expected, actual))

    _print_test_status(all(passes), 'test_minimum')


def test_insert() -> None:
    _print_test_start('test_insert')
    passes = []
    bst = BinarySearchTree()

    assert bst.isEmpty()

    bst.insert(BinarySearchTree(924))
    expected = 924
    actual = bst.getRoot()
    passes.append(_print_test_result(1, expected, actual))

    bst.insert(BinarySearchTree(220))
    expected = 220
    actual = bst.getLeft().getRoot()
    passes.append(_print_test_result(1, expected, actual))

    bst.insert(BinarySearchTree(901))
    expected = 901
    actual = bst.getLeft().getRight().getRoot()
    passes.append(_print_test_result(1, expected, actual))

    bst.insert(BinarySearchTree(244))
    expected = 244
    actual = bst.getLeft().getRight().getLeft().getRoot()
    passes.append(_print_test_result(1, expected, actual))

    bst.insert(BinarySearchTree(898))
    expected = 898
    actual = bst.getLeft().getRight().getLeft().getRight().getRoot()
    passes.append(_print_test_result(1, expected, actual))

    bst.insert(BinarySearchTree(258))
    expected = 258
    actual = bst.getLeft().getRight().getLeft().getRight().getLeft().getRoot()
    passes.append(_print_test_result(1, expected, actual))

    bst.insert(BinarySearchTree(362))
    expected = 362
    actual = bst.getLeft().getRight().getLeft().getRight().getLeft().getRight().getRoot()
    passes.append(_print_test_result(1, expected, actual))

    bst.insert(BinarySearchTree(363))
    expected = 363
    actual = bst.getLeft().getRight().getLeft().getRight().getLeft().getRight().getRight().getRoot()
    passes.append(_print_test_result(1, expected, actual))

    bst.insert(BinarySearchTree(1000))
    expected = 1000
    actual = bst.getRight().getRoot()
    passes.append(_print_test_result(1, expected, actual))

    bst.insert(BinarySearchTree(950))
    expected = 950
    actual = bst.getRight().getLeft().getRoot()
    passes.append(_print_test_result(1, expected, actual))

    bst.insert(BinarySearchTree(949))
    expected = 949
    actual = bst.getRight().getLeft().getLeft().getRoot()
    passes.append(_print_test_result(1, expected, actual))


    bst.inorderTreeWalk()

    # Test #2: Symmetric insert -> This should not work on a bst.
    bst = BinarySearchTree(1)
    expected = 1
    actual = bst.getRoot()
    passes.append(_print_test_result(2, expected, actual))

    bst.insert(BinarySearchTree(2))
    expected = 2
    actual = bst.getRight().getRoot()
    passes.append(_print_test_result(2, expected, actual))

    bst.insert(BinarySearchTree(2))
    expected = 2
    actual = bst.getLeft().getRoot()
    passes.append(_print_test_result(2, expected, actual))

    bst.insert(BinarySearchTree(3))
    expected = None
    actual = bst.getRight().getRight().getRoot()
    passes.append(_print_test_result(2, expected, actual))

    bst.insert(BinarySearchTree(3))
    expected = None
    actual = bst.getLeft().getLeft().getRoot()
    passes.append(_print_test_result(2, expected, actual))

    bst.insert(BinarySearchTree(4))
    expected = bst.getRight().getLeft().getRoot()
    actual = bst.getLeft().getL
    passes.append(_print_test_result(2, expected, actual))

    bst.insert(BinarySearchTree(4))
    expected = None
    actual = bst.getLeft().getRight().getRoot()
    passes.append(_print_test_result(2, expected, actual))


    _print_test_status(all(passes), 'test_insert')


def test_is_mirror() -> None:
    _print_test_start('test_is_mirror')
    passes = []
    _print_test_status(all(passes), 'test_is_mirror')


def _test_create_random_bst():
    _print_test_start('_test_create_random_bst')
    bst = _create_random_bst(10)
    bst.inorderTreeWalk()


def _create_random_bst(size) -> BinarySearchTree:
    newBST = BinarySearchTree()
    for i in range(size):
        newNode = BinarySearchTree(randint(START_OF_VALUES, END_OF_VALUES))
        newBST.insert(newNode)
    return newBST


def _print_test_start(testName):
    print("Testing " + testName + " ...")


def _print_test_status(passed, testName):
    if passed:
        print(testName + ": " + "Test Passed! \n")

    else:
        print(testName + ": " + "Test Failed! \n")


def _print_test_result(numTest: int, expected: Any, actual: Any) -> bool:
    if actual != expected:
        print("Test #" + str(numTest))
        print("Actual is not equal to expected: actual = " + str(actual) + ", expected = " + str(expected))
        return False

    return True


def run_tests():
    print("Welcome! Testing BinarySearchTree methods... \n\n")

    # search unit test
    test_search()

    # insert unit test
    test_insert()

    # maximum unit test
    test_maximum()

    # minimum unit test
    test_minimum()

    # _create_random_bst unit test
    _test_create_random_bst()



if __name__ == '__main__':
    run_tests()
