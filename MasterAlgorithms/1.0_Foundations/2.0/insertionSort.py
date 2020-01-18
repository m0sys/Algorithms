# Date: 2020/1/6
# Insertion sort based on page 18 of algorithm textbook.

def insertionSort(A):
    for j in range(1, len(A)):
        # Key is the card we want to place in order for this
        # current iteration.
        key = A[j]
        # Insert A[j] into the sorted sequence A[0 .. j - 1]
        i = j - 1
        # i will be one element before the card we want to
        # sort. So essentially we are checking to see if
        # key is already in place. If it is not, we would like
        # to place it in the subarry[0 : j - 1] that we know
        # is already sorted.
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key

if __name__ == "__main__":
    arr = [5, 2, 4, 6, 1, 3]
    print("Sorting ... " + str(arr))

    insertionSort(arr)
    print("Sorted: " + str(arr))

    arr = [10, 23, 1, 2 , 9, 4, 5, 3, 100, 200, 50, 40, 30, 20]
    print("Sorting ... " + str(arr))

    insertionSort(arr)
    print("Sorted: " + str(arr))
