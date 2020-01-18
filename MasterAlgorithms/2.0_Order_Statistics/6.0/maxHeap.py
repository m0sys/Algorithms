# Date: 2020/1/16.
# Implmenting a Max Heap data structure
# based on sections 6.1 - 6.5 of the
# algorithm textbook.

import math

class MaxHeap:
    def __init__(self, A: List[int]): -> None
        self.A = A
        self.heap_size = len(A)
        # TODO: Build max heap from this array.

    def parent(i: int): -> int
        """Return the parent idx of node at <A[i]>.
        """
        # TODO: Use right shift to implement this.
        return self.A[math.floor(i / 2)]

    def left(i: int): -> int
        """Return left child idx of node at <A[i]>.

        """
        # TODO: Use left shift to implement this.
        return self.A[2*i]

    def right(i: int): -> int
        """Return right child idx of node at <A[i]>.

        """
        # TODO: Use left shift + 1 to implement this.
        return self.A[2*i + 1]

    def max_heapify(self, i: int): -> None
        """Correct max heap property at node i in array.

        Precondition: Child of node i respects the max heap property.
        """
        l = self.left(i)
        r = self.right(i)
        if l <= self.heap_size and self.A[i] < self.A[l]:
            largest = l
        else:
            largest = i

        if r <= self.heap_size and self.A[i] < A[largest]:
            largest = r
        if largest != i:
            self._swap(i, j)
            self.max_heapify(largest)

    def _swap(self, i: int, j: int): -> None
        tmp = self.A[i]
        self.A[i] = self.A[j]
        self.A[j] = tmp

