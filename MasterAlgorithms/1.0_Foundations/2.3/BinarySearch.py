# Date: 2020/1/11
# Binary Search: ans to exercise 2.3.5
# on page 39.

class Search:
    def binarySearch(self, A, start, end, k):
        """
        Precondition: A[start .. end] inclusive is a sorted list and is none empty.
        Postcondition: Return true if k in A.
        """
        if end == start:
            return A[start] == k

        mid = (start + end) // 2

        if A[mid] == k:
            return True

        if A[mid] > k:
            return self.binarySearch(A, start, mid - 1, k)
        return self.binarySearch(A, mid + 1, end, k)


if __name__ == "__main__":
    s = Search()
    # Test #1
    arr = [1, 2, 3, 4, 5, 6]
    print("Searching " + str(arr) + " for 4 ...")
    print("Found 4? " + str(s.binarySearch(arr, 0, len(arr) - 1, 4)))

    # Test #2
    arr = [1, 2, 3, 4, 5, 6, 7]
    print("\n\nSearching " + str(arr) + " for 4 ...")
    print("Found 4? " + str(s.binarySearch(arr, 0, len(arr) - 1, 4)))
    # Test #3
    arr = [1, 2, 3, 4, 5, 6, 7]
    print("\n\nSearching " + str(arr) + " for 8 ...")
    print("Found 8? " + str(s.binarySearch(arr, 0, len(arr) - 1, 8)))
