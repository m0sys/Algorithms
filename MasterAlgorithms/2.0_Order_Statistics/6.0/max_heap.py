# Date: 2020/1/16.
# Implmenting a Max Heap data structure
# based on sections 6.1 - 6.5 of the
# algorithm textbook.

import math
from typing import List

class MaxHeap:
    def __init__(self, A: List[int]) -> None:
        self.A = A
        self.heap_size = len(A) - 1

    def _parent(self, i: int) -> int:
        """Return the parent idx of node at <A[i]>.
        """
        # TODO: Use right shift to implement this.
        return math.floor(i / 2)

    def _left(self, i: int) -> int:
        """Return left child idx of node at <A[i]>.

        """
        # TODO: Use left shift to implement this.
        return 2*i + 1

    def _right(self, i: int) -> int:
        """Return right child idx of node at <A[i]>.

        """
        # TODO: Use left shift + 1 to implement this.
        return 2*i + 2

    def _max_heapify(self, i: int) -> None:
        """Correct max heap property at node i in array.

        Precondition: Child of node i respects the max heap property.
        """
        ## print("Elem at i = " + str(i) + ": " + str(self.A[i]))
        l = self._left(i)
        r = self._right(i)
        ## print("l = " + str(l))
        ## print("r = " + str(r))
        if l <= self.heap_size and self.A[i] < self.A[l]:
            largest = l
        else:
            largest = i

        if r <= self.heap_size and self.A[largest] < self.A[r]:
            largest = r
        if largest != i:
            # Here by calling max heapify you are perculating down the tree until the max heap invariant becomes true. (2020/2/26)
            self._swap(i, largest)
            self._max_heapify(largest)

    def _build_max_heap(self) -> None:
        """Build max heap from array A
        """
        # Note that the first half of the node abide the max heap property, therefore check max heap
        # prop for the remaining half nodes at the top. (2020/2/26)
        ## self.heap_size = len(self.A)
        for i in range(math.floor(self.heap_size / 2), -1, -1):
            ## print("Building max heap: i = " + str(i))
            self._max_heapify(i)

    def heap_sort(self) -> None:
        self._build_max_heap()
        for i in range(len(self.A) -1, 0, -1):
            ## print("Heap sort: i = " + str(i))
            self._swap(0, i)
            self.heap_size -= 1
            self._max_heapify(0)


    def _swap(self, i: int, j: int) -> None:
        tmp = self.A[i]
        self.A[i] = self.A[j]
        self.A[j] = tmp


if __name__ == "__main__":
    # Test #1
    arr = [5, 3, 17, 10, 84, 19, 6, 22, 9]
    print("Test #1: init state:" + str(arr))
    max_heap = MaxHeap(arr)
    max_heap._build_max_heap()

    expected = [84, 22, 19, 10, 3, 17, 6, 5, 9]
    passed = arr == expected
    print("Actual: " + str(arr))
    print("Expected: " + str(expected))
    print("Passed? " + str(passed))

    # Test #2
    arr = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    print("\n\nTest #2: init state:" + str(arr))
    max_heap = MaxHeap(arr)
    max_heap._build_max_heap()

    expected = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
    passed = arr == expected
    print("Actual: " + str(arr))
    print("Expected: " + str(expected))
    print("Passed? " + str(passed))

    # Test #3
    arr = [5, 13, 2, 25, 7, 17, 20, 8, 4]
    print("\n\nTest #3: init state:" + str(arr))
    max_heap = MaxHeap(arr)
    max_heap._build_max_heap()

    ## passed = arr == expected
    print("Actual: " + str(arr))
    ## print("Expected: " + str(expected))
    ## print("Passed? " + str(passed))

    # Test Heap Sort:
    print("\n\nTesting heapsort... \n\n")

    # Test #1
    arr = [5, 3, 17, 10, 84, 19, 6, 22, 9]
    print("Test #1: init state:" + str(arr))
    max_heap = MaxHeap(arr)
    max_heap.heap_sort()

    expected = [3, 5, 6, 9, 10, 17, 19, 22, 84]
    passed = arr == expected
    print("Actual: " + str(arr))
    print("Expected: " + str(expected))
    print("Passed? " + str(passed))



