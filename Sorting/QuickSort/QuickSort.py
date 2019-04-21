from __future__ import annotations
from typing import List

# Quick Sort Algorithm
# ====================


def quick_sort(l: List) -> None:
    """
    Implementation of the Quick Sort Algorithm.

    Quick Sort is a Comparison based sorting  algorithm, and all elements are
    sorted in place.

    Parameters:
    -----------
    :param l:

    Return Value:
    -------------
    :return:

    doctest:
    --------
    >>> l = [2, 8, 7, 1, 3, 5, 6, 4]
    >>> quick_sort(l)
    >>> l
    [1, 2, 3, 4, 5, 6, 7, 8]
    """
    _quick_sort_helper(l, 0, len(l))


def _quick_sort_helper(l: List, start: int, end: int) -> None:
    """
    Quick Sort helper function.

    Quick sort takes a **pivot** point and compares all other elements to the
    pivot.

    Parameters:
    -----------
    :param l:
    :param start:
    :param end:

    Return Value:
    -------------
    :return:
    """
    if start < end:
        q = _partition(l, start, end)
        _quick_sort_helper(l, start, q)
        _quick_sort_helper(l, q + 1, end)


def _swap(l, index1, index2):
    l[index1], l[index2] = l[index2], l[index1]


def _partition(l: List, first: int, last: int) -> int:
    """
    Partition the list with respect to a **pivot** point.

    In this implementation of partition the pivot is taken to be at
    index <last>. As this method runs it partitions the sub array l[first: last]
    into four (possibly empty) regions.

    The four regions have the following invariance for each iteration of the
    loop.

    Loop Invariant:
    ---------------
    Let x represent the pivot point at index <end>. For any array index k:
    1. If first <= k <= i, then l[k] <= x.
    2. If i + 1 <= k <= j - 1, then l[k] > x.
    3. If k == last, then A[k] = x.

    Parameters:
    -----------
    :param l:
    :param first:
    :param last:

    Return Value:
    -------------
    :return:
    """
    # Assign pivot to last element in current sub array.
    x = l[last - 1]
    i = first
    for j in range(first, last - 1):
        if l[j] <= x:
            _swap(l, i, j)
            i += 1
    _swap(l, i, last - 1)
    return i
