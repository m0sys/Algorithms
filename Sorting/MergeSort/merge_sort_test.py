from __future__ import annotations
import pytest
from mergeSort import *


def test_merge_sort():
    l = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    mergeSort(l)
    assert l == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    l2 = [100, 200, 100, 203, 100, 40, 30, 1, 22, 21, 37, 1000, 101]
    mergeSort(l2)
    assert l2 == [1, 21, 22, 30, 37, 40, 100, 100, 100, 101, 200, 203, 1000]


if __name__ == "__main__":
    import pytest
    pytest.main(['merge_sort_test.py'])

