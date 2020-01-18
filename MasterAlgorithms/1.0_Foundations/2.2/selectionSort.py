# Date: 2020/1/9.
# Selection sort: ans to exercise 2.2.2.
# on page 22.

class Sort:
    def selectionSort(self, A, toPrint = False):
        for i in range(len(A)):
            smallest = i
            for j in range(i, len(A)):
                    if A[j] < A[smallest]:
                        smallest = j

            if toPrint:
                print("Smallest found on iteration: i = " + str(i) + ", smallest " + str(smallest))
                print("current state of my list: " + str(A))
            self.swap(A, smallest, i)
            if toPrint:
                print("new state of my list: " + str(A) + "\n")

    def swap(self, A, idx1, idx2):
        tmp = A[idx1]
        A[idx1] = A[idx2]
        A[idx2] = tmp

if __name__ == "__main__":
    s = Sort()
    arr = [5, 2, 4, 6, 1, 3]
    print("Sorting ... " + str(arr))
    s.selectionSort(arr)
    print("Sorted: " + str(arr))

    arr = [26, 31, 41, 41, 58, 59]
    print("Sorting in Reverse ... " + str(arr))
    s.selectionSort(arr)
    print("Sorted: " + str(arr))


