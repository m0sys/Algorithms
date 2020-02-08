from typing import List
class search:
    def binarySearch(self, arr: List[int], key: int, start: int, end: int) -> bool:
        """In place binary search.

        Precondtions:
            - 0 <= start <= len(arr) - 1
            - 0 <= end <= len(arr) - 1
        """

        if end - start  == 0:
            if arr[start] == key:
                return True
            return False

        if (end - start) % 2 == 0:
            mid = start +  ((end - start) // 2 - 1)

        else:
            mid = start + ((end - start) // 2)

        if arr[mid] == key:
            return True

        if arr[mid] > key:
            return self.binarySearch(arr, key, start, mid - 1)
        return self.binarySearch(arr, key, mid + 1, end)

    def binarySearchIndex(self, arr: List[int], key: int, start: int, end: int) -> int:
        """In place binary search which returns the index of the item if found.

        If found return index. If not found return -1.

        Preconditions:
            - 0 <= <start> <= len(arr) - 1
            - 0 <= <end> <= len(arr) - 1

        Return:
            if key is in arr return first key occrance index.
            if key not in arr return the index of the next greatest element in arr relative to key.
        """

        if (end - start) == 0:
            if arr[start] == key:
                return start
            else:
                return -1


        if (end - start) % 2 == 0:
            mid = start + ((end - start) // 2 - 1)
        else:
            mid = start + ((end - start) // 2)

        if arr[mid] == key:
            return mid

        if arr[mid] > key:
            return self.binarySearchIndex(arr, key, start, mid - 1)
        return self.binarySearchIndex(arr, key, mid + 1, end)

    def binarySearchNextGreatestIndex(self, arr: List[int], key: int, start: int, end: int) -> int:
        """Search for the next greatest element in <arr> relative to <key>.

        Preconditions:
            - 0 <= <start> <= len(arr) - 1
            - 0 <= <end> <= len(arr) - 1
        """

        if (end - start) == 0:
            if arr[start] >= key:
                return start
            return - 1


        if (end - start) % 2 == 0:
            mid = start +  ((end - start) // 2 + -1)

        else:
            mid = start + ((end - start) // 2)

        if arr[mid] == key:
            return mid

        if arr[mid] > key:
            if mid - 1 <= end and arr[mid - 1] == key:
                return mid - 1

            if mid - 1 <= end and arr[mid - 1] < key:
                return mid

            return self.binarySearchNextGreatestIndex(arr, key, start, mid - 1)

        return self.binarySearchNextGreatestIndex(arr, key, mid + 1, end)





        ## if arr[start] >= key:
        ##     return start
        ## if arr[end] < key:
        ##     return -1


        ## if (end - start) % 2 == 0:
        ##     mid = start +  ((end - start) // 2 + -1)

        ## else:
        ##     mid = start + ((end - start) // 2)

        ## print ("Elem at mid = " + str(mid) + ": " + str(arr[mid]))

        ## if arr[mid] >= key:
        ##     return mid

        ## if arr[mid] > key:
        ##     if mid + 1 <= end and arr[mid + 1] >= key:
        ##         return mid + 1
        ##     else:
        ##         return self.binarySearchNextGreatestIndex(arr, key, mid + 1, end)

        ## return self.binarySearchNextGreatestIndex(arr, key, start, mid - 1)


if __name__ == "__main__":
    s = search()
    # Test binary search:
    print("Testing binary search...")
    # Test Case #1: odd array.
    arr = [1, 2, 3, 4, 5]
    result = s.binarySearch(arr, 3, 0, len(arr) - 1)
    expected = True
    print("Test Case #1")
    print("result: " + str(result))
    print("expected: " + str(expected))
    print("Passed: " + str(expected == result))

    # Test Case #2: test the last elem.
    arr = [1, 2, 3, 4, 5]
    result = s.binarySearch(arr, 5, 0, len(arr) - 1)
    expected = True
    print("\n\nTest Case #2")
    print("result: " + str(result))
    print("expected: " + str(expected))
    print("Passed: " + str(expected == result))

    # Test Case #3: test the first elem.
    arr = [1, 2, 3, 4, 5]
    result = s.binarySearch(arr, 1, 0, len(arr) - 1)
    expected = True
    print("\n\nTest Case #3")
    print("result: " + str(result))
    print("expected: " + str(expected))
    print("Passed: " + str(expected == result))

    # Test Case #4: even array.
    arr = [1, 2, 3, 4, 5, 6]
    result = s.binarySearch(arr, 4, 0, len(arr) - 1)
    expected = True
    print("\n\nTest Case #4")
    print("result: " + str(result))
    print("expected: " + str(expected))
    print("Passed: " + str(expected == result))

    # Test Case #5: test last elem.
    arr = [1, 2, 3, 4, 5, 6]
    result = s.binarySearch(arr, 6, 0, len(arr) - 1)
    expected = True
    print("\n\nTest Case #5")
    print("result: " + str(result))
    print("expected: " + str(expected))
    print("Passed: " + str(expected == result))

    # Test Case #6: test first elem.
    arr = [1, 2, 3, 4, 5, 6]
    result = s.binarySearch(arr, 1, 0, len(arr) - 1)
    expected = True
    print("\n\nTest Case #6")
    print("result: " + str(result))
    print("expected: " + str(expected))
    print("Passed: " + str(expected == result))

    # Test Case #7: test first elem.
    arr = [1, 2, 3, 4, 5, 6]
    result = s.binarySearch(arr, 20, 0, len(arr) - 1)
    expected = False
    print("\n\nTest Case #7")
    print("result: " + str(result))
    print("expected: " + str(expected))
    print("Passed: " + str(expected == result))


    # Test binary index:
    print("\n\nTesting binary index... ")

    # Test Case #1: odd array.
    arr = [1, 2, 3, 4, 5]
    result = s.binarySearchIndex(arr, 3, 0, len(arr) - 1)
    expected = 2
    print("Test Case #1")
    print("result: " + str(result))
    print("expected: " + str(expected))
    print("Passed: " + str(expected == result))

    # Test Case #2: test the last elem.
    arr = [1, 2, 3, 4, 5]
    result = s.binarySearchIndex(arr, 5, 0, len(arr) - 1)
    expected = 4
    print("\n\nTest Case #2")
    print("result: " + str(result))
    print("expected: " + str(expected))
    print("Passed: " + str(expected == result))

    # Test Case #3: test the first elem.
    arr = [1, 2, 3, 4, 5]
    result = s.binarySearchIndex(arr, 1, 0, len(arr) - 1)
    expected = 0
    print("\n\nTest Case #3")
    print("result: " + str(result))
    print("expected: " + str(expected))
    print("Passed: " + str(expected == result))

    # Test Case #4: even array.
    arr = [1, 2, 3, 4, 5, 6]
    result = s.binarySearchIndex(arr, 4, 0, len(arr) - 1)
    expected = 3
    print("\n\nTest Case #4")
    print("result: " + str(result))
    print("expected: " + str(expected))
    print("Passed: " + str(expected == result))

    # Test Case #5: test last elem.
    arr = [1, 2, 3, 4, 5, 6]
    result = s.binarySearchIndex(arr, 6, 0, len(arr) - 1)
    expected = 5
    print("\n\nTest Case #5")
    print("result: " + str(result))
    print("expected: " + str(expected))
    print("Passed: " + str(expected == result))

    # Test Case #6: test first elem.
    arr = [1, 2, 3, 4, 5, 6]
    result = s.binarySearchIndex(arr, 1, 0, len(arr) - 1)
    expected = 0
    print("\n\nTest Case #6")
    print("result: " + str(result))
    print("expected: " + str(expected))
    print("Passed: " + str(expected == result))

    # Test next greatest binary index:
    print("\n\n Testing next greatest binary search... ")

    # Test Case #1: odd array.
    arr = [1, 2, 3, 4, 5]
    result = s.binarySearchNextGreatestIndex(arr, 3, 0, len(arr) - 1)
    expected = 2
    print("Test Case #1")
    print("result: " + str(result))
    print("expected: " + str(expected))
    print("Passed: " + str(expected == result))

    # Test Case #2: test the last elem.
    arr = [1, 2, 3, 4, 5]
    result = s.binarySearchNextGreatestIndex(arr, 5, 0, len(arr) - 1)
    expected = 4
    print("\n\nTest Case #2")
    print("result: " + str(result))
    print("expected: " + str(expected))
    print("Passed: " + str(expected == result))

    # Test Case #3: test the first elem.
    arr = [1, 2, 3, 4, 5]
    result = s.binarySearchNextGreatestIndex(arr, 1, 0, len(arr) - 1)
    expected = 0
    print("\n\nTest Case #3")
    print("result: " + str(result))
    print("expected: " + str(expected))
    print("Passed: " + str(expected == result))

    # Test Case #4: even array.
    arr = [1, 2, 3, 4]
    result = s.binarySearchNextGreatestIndex(arr, 3, 0, len(arr) - 1)
    expected = 2
    print("\n\nTest Case #4")
    print("result: " + str(result))
    print("expected: " + str(expected))
    print("Passed: " + str(expected == result))

    # Test Case #5: test last elem.
    arr = [1, 2, 3, 4, 5, 6]
    result = s.binarySearchNextGreatestIndex(arr, 6, 0, len(arr) - 1)
    expected = 5
    print("\n\nTest Case #5")
    print("result: " + str(result))
    print("expected: " + str(expected))
    print("Passed: " + str(expected == result))

    # Test Case #6: test first elem.
    arr = [1, 2, 3, 4, 5, 6]
    result = s.binarySearchNextGreatestIndex(arr, 1, 0, len(arr) - 1)
    expected = 0
    print("\n\nTest Case #6")
    print("result: " + str(result))
    print("expected: " + str(expected))
    print("Passed: " + str(expected == result))

    # Test Case #7: test next greatest on the left of first mid point.
    arr = [1, 2, 3, 4, 5, 6, 10, 11, 14]
    result = s.binarySearchNextGreatestIndex(arr, 7, 0, len(arr) - 1)
    expected = 6
    print("\n\nTest Case #7")
    print("result: " + str(result))
    print("expected: " + str(expected))
    print("Passed: " + str(expected == result))

