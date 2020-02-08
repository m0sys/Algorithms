import math
from maxHeap.py import MaxHeap

class MaxPriorityQueue(MaxHeap):
    def __init__(self, A: List[int]) -> None:
        super().__init__(self, A)
        self._build_max_heap()

    def heap_max(self) -> int:
        return self.A[0]

    def extract_max(self) -> int:
        """Extract the max from the tree.

        Postconditons:
            - the tree conserves the max heap property.
        """
        if self.A.heap_size < 1:
            raise Exception("Heap Underflow")

        max = self.heap_max()
        self.A[0] = self.A[self.heap_size]
        self.heap_size -= 1
        self._max_heapify(0)
        return max

    def increase_key(i: int, key: int) -> None:
        """Increase key at index <i> to <key>.


        Preconditions:
            - 0 <= i <= <self.heap_size>
        """
        if key < self.A[i]:
            raise Exception("New key is smaller the current key")

        self.A[i] = key
        while i > 0 and self.A[i] > self.A[self._parent(i)]:
            self._swap(i, self._parent(i))
            i = self._parent(i)

    def insert(self, key) -> None:
        """Insert new node with value <key> into the max heap tree.
        """
        self.heap_size += 1
        self.A.append(-math.inf)
        self.increase_key(self.heap_size, key)


if __name__ == "__main__":
    pass

