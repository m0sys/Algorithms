from __future__ import annotations
from typing import List
import math
import random
## import pytest

# Implement Merge Sort Algorithm
# ==============================

# Constants
# ---------
INF = math.inf
RAND_START = 100
RAND_END = 50300


def mergeSort(l: List) -> List:
    """
    Merge sort algorithm. Sort is done in increasing order, and mergeSort is
    a comparision based sorting algorithm, meaning that there is an explicit
    notion of 'greatest' and 'least'.

    Parameters:
    -----------
    :param l: list of element to sort.

    Return Value:
    -------------
    :return: l

    doctest:
    --------
    >>> l0 = [5, 2, 4, 7, 1, 3, 2, 6]
    >>> mergeSort(l0)
    [1, 2, 2, 3, 4, 5, 6, 7]

    >>> l = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    >>> mergeSort(l)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    >>> l2 = [100, 200, 100, 203, 100, 40, 30, 1, 22, 21, 37, 1000, 101]
    >>> mergeSort(l2)
    [1, 21, 22, 30, 37, 40, 100, 100, 100, 101, 200, 203, 1000]
    """
    _merge_sort_helper(l, 0, len(l))
    return l


def _merge_sort_helper(l: List, start: int, end: int) -> None:
    """
    Merge sort helper function.

    Parameters:
    -----------
    :param l: list of elements to sort.
    :param start: index of the first element in l.
    :param end: index of the last element in l.

    Return Value:
    -------------
    :return: None
    """
    # Debug
    toPrint = False
    middle = (start + end) // 2
    if toPrint:
        print("_merge_sort_helper: middle = " + str(middle))

    if end - start - 1 == 0:
        return
    _merge_sort_helper(l, start, middle)
    _merge_sort_helper(l, middle, end)
    _merge(l, start, middle, end)


def _merge(l: List, left: int, middle: int, right: int) -> None:
    """
    Merge the two sub arrays l[left : middle] and l[left + 1 : right].

    Preconditions:
    --------------
    1) sub array l[left: middle] and l[middle + 1 : right] is sorted.
    2) left <= middle < right

    Parameters:
    -----------
    :param l: list of elements that have a notion of comparision.
    :param left: index at the starting point.
    :param middle: index at middle of the starting point and end point.
    :param right: index at the end point.

    Return Value:
    -------------
    :return: None
    """
    # Debug
    toPrint = False

    n1 = middle - left
    n2 = right - middle
    ll = [0 for _ in range(n1 + 1)]
    rl = [0 for _ in range(n2 + 1)]

    try:
        assert len(ll) + len(rl) == right - left + 2
    except AssertionError:
        print("\n\n")
        print("_merge: Assertion Error!")
        print("_merge: actual: len ll + rl = " + str(len(ll) + len(rl)))
        print("_merge: expected: " + str(right - left + 2))

    for i in range(n1):
        ll[i] = l[left + i]

    for j in range(n2):
        rl[j] = l[middle + j]

    # Add sentinel elements at the end of left, right list
    ll[n1] = INF
    rl[n2] = INF

    if toPrint:
        print("_merge: Sorted ll: " + str(ll))
        print("_merge: Sorted rl: " + str(rl))
        print("\n\n")

    i = 0  # left index
    j = 0  # right index

    for k in range(left, right):
        if ll[i] <= rl[j]:
            l[k] = ll[i]
            i += 1

        else:
            l[k] = rl[j]
            j += 1

def _generateRandomList(size: int) -> List:
    result = []
    for i in range(size):
        result.append(random.randint(RAND_START, RAND_END))
    return result


if __name__ == "__main__":
    l = _generateRandomList(30)
    print("My random gen list: " + str(l))
    mergeSort(l)
    print("My sorted random gen list: " + str(l))
