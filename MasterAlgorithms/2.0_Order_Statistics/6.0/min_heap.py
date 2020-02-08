# Date: 2020/1/25.
# Implementing a Min Heap data structure
# based on exercise 6.2.2 in algorithm
# textbook.

from math import floor, ceil
from typing import List

class MinHeap:
    """A Min Heap datastructure.

    This datastructure is used for sorted an array in decreasing order.


    Attributes:
        heap_size: size of the heap.
        arr: the arr sorting the integers in the heap.

    Representation invariant:
        - A[Parent(i)] <= A[i] for every node i except the root.
          also known as the min heap property.
        - the root is the minimum element in the tree.
        - 0 <= heap_size <= length of <arr> - 1.
    """
    heap_size: int
    arr: List[int]

    def __init__(self, arr: List[int]) -> None:
        self.heap_size = len(arr) - 1
        self.arr = arr

    def _parent(self, i: int) -> int:
        return floor(i / 2);

    def _left(self, i: int) -> int:
        return 2 * i + 1

    def _right(self, i: int) -> int:
        return 2 * i + 2

    def _min_heapify(self, i: int) -> None:
        """Fix the min heap property at node i.

        Preconditions:
            - left child and right child respect min heap property.
        """
        l = self._left(i)
        r = self._right(i)

        if l <= self.heap_size and self.arr[l] < self.arr[i]:
            smallest = l
        else:
            smallest = i

        if r <= self.heap_size and self.arr[r] < self.arr[smallest]:
            smallest = r

        if smallest != i:
            self._swap(i, smallest)
            self._min_heapify(smallest)

    def build_min_heap(self):
        """Sort <self.arr> in min heap order.
        """
        self.heap_size = len(self.arr) - 1
        for i in range(floor(self.heap_size / 2), -1, -1):
            self._min_heapify(i)

    def heap_sort(self):
        """Sort <self.arr> in decreasing order.
        """
        self.build_min_heap()
        length = self.heap_size
        for i in range(length, 0, -1):
            self._swap(0, i)
            self.heap_size -= 1
            self._min_heapify(0)

    def _swap(self, idx1: int, idx2: int) -> None:
        tmp = arr[idx1]
        arr[idx1] = arr[idx2]
        arr[idx2] = tmp



if __name__ == "__main__":
    print("Testing min heap ... \n\n")
    arr = [1, 2, 3, 4, 5, 6]
    heap = MinHeap(arr)
    heap.heap_sort()
    print("Sorted arr: " + str(arr))
    expected = [6, 5, 4, 3, 2, 1]
    passed = expected == arr
    print("Test #1 passed? " + str(passed))



