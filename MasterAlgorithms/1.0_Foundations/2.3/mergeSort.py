# Date: 2020/1/6
# Merge sort based on page 31 of algorithm textbook.

import math
import random

class Sort:
    def _smartMerge(self, A, p, q, r):
        i = p
        j = q + 1
        for k in range(p, r + 1):
            if A[i] >= A[j]:
                self._swap(A, i, k)
                i += 1

    def mergeSort(self, A, p, r, smart = True):
        """
        Precondition: 0 <= p <= A.length - 1, 0 <= r <= A.length - 1.
        Postcondition: A[p : r + 1]  is sorted.
        """
        if p < r:
            mid = (p + r) // 2
            self.mergeSort(A, p, mid)
            self.mergeSort(A, mid + 1, r)
            self._merge(A, p, mid, r)

    def _merge(self, A, p, q, r):
        """
        Precondition: A[p : q + 1] and A[q + 1 : r] are sorted in ascending order and
        Postcondition: A[p .. r] is sorted in ascending order.
        """
        L = []
        R = []
        for i in range (p, q + 1):
            L.append(A[i])

        for i in range(q + 1, r + 1):
            R.append(A[i])

        ## print("\n\nL found in merge: " + str(L))

        ## print("\n\nR found in merge: " + str(R))
        i = 0
        j = 0

        # Add sentinal nodes.
        L.append(math.inf)
        R.append(math.inf)


        for k in range(p, r + 1):
            if L[i] <= R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1

    def _swap(self, A, idx1, idx2):
        tmp = A[idx1]
        A[idx1] = A[idx2]
        A[idx2] = tmp

def makeRandomArray(n):
    a = []
    for i in range(n):
        a.append(random.randint(0, n))

    return a


if __name__ == "__main__":
    s = Sort()
    print("Being Sorting ... \n\n ")

    # Test #1
    print("Test #1 ...")
    arr = [5]
    print("Sorting ... " + str(arr))
    s.mergeSort(arr, 0, len(arr) - 1)
    print("Sorted: " + str(arr))

    # Test #2
    print("\n\nTest #2 ...")
    arr = [5, 2]
    print("Sorting ... " + str(arr))
    s.mergeSort(arr, 0, len(arr) - 1)
    print("Sorted: " + str(arr))

    # Test #3
    print("\n\n Test #3 ...")
    arr = [5, 2, 4, 6, 1, 3]
    print("Sorting ... " + str(arr))
    s.mergeSort(arr, 0, len(arr) - 1)
    print("Sorted: " + str(arr))

    # Test #4
    print("\n\nTest #4 ...")
    arr = [10, 23, 1, 2 , 9, 4, 5, 3, 100, 200, 50, 40, 30, 20]
    print("Sorting ... " + str(arr))
    s.mergeSort(arr, 0, len(arr) - 1)
    print("Sorted: " + str(arr))

    # Test #5
    print("\n\nTest #5 ...")
    arr = makeRandomArray(2)
    print("Sorting ... " + str(arr))
    s.mergeSort(arr, 0, len(arr) - 1)
    print("Sorted: " + str(arr))
