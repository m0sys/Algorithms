# Top worst sorting algorithms to never use in life.
class BadSorts():
    def __init__(self, mArray, printMe = False):
        self.mArray = mArray
        self.mToPrint = printMe
        self.mLen = len(mArray)

    def selectionSort(self):
        # Play it dumb and you might just make it.
        toPrint = self.getToPrint()

        for i in range(self.getLength()):
            minIdx = i
            for j in range(i + 1, self.getLength()):
                if self.mArray[minIdx] > self.mArray[j]:
                    minIdx = j

            if minIdx != i:
                self.swap(i, minIdx)

    def insertionSort(self):
        # Think of this as a better version of your dumbness.
        array = self.getArray()
        for i in range(1, self.getLength()):
            self._insertHelper(i)
        pass

    def _insertHelper(self, j):
        while j > 0 and self.mArray[j - 1] > self.mArray[j]:
            self.swap(j - 1, j)
            j -= 1
        pass

    def bubbleSort(self):
        # Even Senator Obama knew not to use this sorting algorithm, and he ain't no coder (2011 Page).
        toPrint = self.getToPrint()

        swappable = True
        numPasses = 0
        while swappable:
            swapCount = 0
            for i in range(1, self.getLength() - numPasses):
                if self.mArray[i - 1] > self.mArray[i]:

                    if toPrint:
                        print("Swapping: " + str(self.mArray[i - 1]) + " with " + str(self.mArray[i]))

                    swapCount += 1
                    self.swap(i - 1, i)

            numPasses += 1

            if swapCount == 0: # check if swapped for current pass
                swappable = False

    def __str__(self):
        return "List to sort: " + str(self.getArray())

    def __repr__(self):
        return str(self.mArray)

    def swap(self, firstIdx, secondIdx):
        temp = self.mArray[firstIdx]
        self.mArray[firstIdx] = self.mArray[secondIdx]
        self.mArray[secondIdx] = temp

    def togglePrint(self):
        self.setToPrint(not self.getToPrint())

    def getArray(self):
        return self.mArray

    def getToPrint(self):
        return self.mToPrint

    def getLength(self):
        return self.mLen

    def setArray(self, newArray):
        self.mArray = newArray

    def setToPrint(self, newBool):
        self.mToPrint = newBool

    def setLength(self, newLength):
        self.mLen = newLength


# Testing

# Unit testing:


def test_selection_sort():
    print("Testing selection sort... ")
    passed = True

    myArray = [10, 232, 123, 11, 110, 50, 40, 20, 1, 34, 54, 59, 2]
    myBadSort = BadSorts(myArray)

    myBadSort.togglePrint()
    myBadSort.selectionSort()

    actual = myBadSort.getArray()
    expected = [1, 2, 10, 11, 20, 34, 40, 50, 54, 59, 110, 123, 232]
    print(str(myBadSort))
    print("Actual = " + str(actual))

    # Test #1
    if actual != expected:
        print("Test #1 Failed!")
        passed = False

    else:
        print("Test #1 passed!")

    if passed:
        print("Unit test passed! :D \n\n")

    else:
        print("Unit test failed...  :/ \n\n")

    return passed

def test_insertion_sort():
    print("Testing insertion sort... ")
    passed = True

    myArray = [10, 232, 123, 11, 110, 50, 40, 20, 1, 34, 54, 59, 2]
    myBadSort = BadSorts(myArray)

    myBadSort.togglePrint()
    myBadSort.insertionSort()

    actual = myBadSort.getArray()
    expected = [1, 2, 10, 11, 20, 34, 40, 50, 54, 59, 110, 123, 232]
    print(str(myBadSort))
    print("Actual = " + str(actual))

    # Test #1
    if actual != expected:
        print("Test #1 Failed!")
        passed = False

    else:
        print("Test #1 passed!")

    if passed:
        print("Unit test passed! :D \n\n")

    else:
        print("Unit test failed...  :/ \n\n")

    return passed

def test_bubble_sort():
    print("Testing bubble sort... ")
    passed = True

    myArray = [10, 232, 123, 11, 110, 50, 40, 20, 1, 34, 54, 59, 2]
    myBadSort = BadSorts(myArray)

    myBadSort.togglePrint()
    myBadSort.bubbleSort()

    actual = myBadSort.getArray()
    expected = [1, 2, 10, 11, 20, 34, 40, 50, 54, 59, 110, 123, 232]
    print(str(myBadSort))
    print("Actual = " + str(actual))

    # Test #1
    if actual != expected:
        print("Test #1 Failed!")
        passed = False

    else:
        print("Test #1 passed!")

    if passed:
        print("Unit test passed! :D \n\n")

    else:
        print("Unit test failed...  :/ \n\n")

    return passed

def run_test():
    count = 0

    if test_selection_sort():
        count += 1

    if test_insertion_sort():
        count += 1

    if test_bubble_sort():
        count += 1

    print("Passed " + str(count) + " out of " + str(3))
    pass

run_test()
