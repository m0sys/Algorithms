from typing import List
class search:
    def binarySearchIndex(self, arr: List[int], key: int, index: int) -> int:
        if len(arr) == 1:
            if arr[0] == key:
                return index
            return -1

        if len(arr) % 2 == 0:
            mid = len(arr) // 2 - 1
        else:
            mid = len(arr) // 2

        if arr[mid] == key:
            return abs(index - mid)

        if arr[mid] > key:
            return self.binarySearchIndex(arr[:mid], key, abs(index - mid))

        return self.binarySearchIndex(arr[mid + 1:], key, index + mid)


if __name__ == "__main__":
    s = search()

    # Test Case #1: odd array.
    arr = [1, 2, 3, 4, 5]
    result = s.binarySearchIndex(arr, 3, 0)
    expected = 2
    print("Test Case #1")
    print("result: " + str(result))
    print("expected: " + str(expected))
    print("Passed: " + str(expected == result))

    # Test Case #2: test the last elem.
    arr = [1, 2, 3, 4, 5]
    result = s.binarySearchIndex(arr, 5, 0)
    expected = 4
    print("\n\nTest Case #2")
    print("result: " + str(result))
    print("expected: " + str(expected))
    print("Passed: " + str(expected == result))

    # Test Case #3: test the first elem.
    arr = [1, 2, 3, 4, 5]
    result = s.binarySearchIndex(arr, 1, 0)
    expected = 0
    print("\n\nTest Case #3")
    print("result: " + str(result))
    print("expected: " + str(expected))
    print("Passed: " + str(expected == result))

    # Test Case #4: even array.
    arr = [1, 2, 3, 4, 5, 6]
    result = s.binarySearchIndex(arr, 4, 0)
    expected = 3
    print("\n\nTest Case #3")
    print("result: " + str(result))
    print("expected: " + str(expected))
    print("Passed: " + str(expected == result))

    # Test Case #5: test last elem.
    arr = [1, 2, 3, 4, 5, 6]
    result = s.binarySearchIndex(arr, 6, 0)
    expected = 5
    print("\n\nTest Case #3")
    print("result: " + str(result))
    print("expected: " + str(expected))
    print("Passed: " + str(expected == result))

    # Test Case #6: test first elem.
    arr = [1, 2, 3, 4, 5, 6]
    result = s.binarySearchIndex(arr, 1, 0)
    expected = 0
    print("\n\nTest Case #3")
    print("result: " + str(result))
    print("expected: " + str(expected))
    print("Passed: " + str(expected == result))
