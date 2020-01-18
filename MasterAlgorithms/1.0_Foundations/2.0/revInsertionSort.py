# Date: 2020/1/6
# Rev insertion sort: ans to exercise 2.1.2
# on page 22.


class Sort:
    def insertionSort(self, A):
        for j in range(1, len(A)):
            key = A[j]
            i = j - 1
            while i >= 0 and A[i] > key:
                A[i + 1] = A[i]
                i -= 1
            A[i + 1] = key

    def revInsertionSort(self, A):
        for j in range(1, len(A)):
            key = A[j]
            i = j - 1
            while i >= 0 and A[i] < key:
                A[i + 1] = A[i]
                i -= 1
            A[i + 1] = key

if __name__ == "__main__":
    s = Sort()
    arr = [5, 2, 4, 6, 1, 3]
    print("Sorting ... " + str(arr))

    s.insertionSort(arr)
    print("Sorted: " + str(arr))

    arr = [26, 31, 41, 41, 58, 59]
    print("Sorting in Reverse ... " + str(arr))
    s.revInsertionSort(arr)
    print("Sorted: " + str(arr))






