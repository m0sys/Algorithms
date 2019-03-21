from __future__ import annotations
from BinarySearchTree import *
from random import randint

START_OF_VALUES = 100
END_OF_VALUES = 2500


def _test_create_random_bst():
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


def _print_test_result(numTest, expected, actual):
    if actual != expected:
        print("Test #" + str(numTest))
        print("Actual is not equal to expected: actual = " + str(actual) + ", expected = " + str(expected))
        return False

    return True


def run_tests():
    print("Welcome! Testing BinarySearchTree methods... \n\n")

    # _create_random_bst unit test
    _test_create_random_bst()


if __name__ == '__main__':
    run_tests()
