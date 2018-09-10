# Quick sort algorithm: interactivepython.org
def quickSort(alist):
    quickSortHelper(alist, 0, len(alist) - 1)

def quickSortHelper(alist, first, last):
    if first < last:
        splitPoint = partition(alist, first, last)

        quickSortHelper(alist, first, splitPoint - 1) # left hand of split point
        quickSortHelper(alist, splitPoint + 1, last) # right hand of split point

def partition(alist, first, last):
    pivotValue = alist[first]
    
    leftMark = first + 1
    rightMark = last

    done = False

    while not done:
        while leftMark <= rightMark and alist[leftMark] <= pivotValue:
            leftMark += 1

        while alist[rightMark] >= pivotValue and rightMark >= leftMark:
            rightMark -= 1
        
        if rightMark < leftMark:
            done = True

        else:
            # Swap the two items that are out of place with respect to the 
            # eventual split point.
            temp = alist[leftMark]
            alist[leftMark] = alist[rightMark]
            alist[rightMark] = temp

    # Since rightMark is less than leftMark, the position of rightMark is 
    # now the split point. The pivot value can be exchanged with the 
    # contents of the split point and the pivot value is now in place.
    temp = alist[first]
    alist[first] = alist[rightMark]
    alist[rightMark] = temp

    return rightMark

# Testing:
passed = True

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quickSort(alist)

expected = [17, 20, 26, 31, 44, 54, 55, 77, 93]

if (alist == expected and passed):
    print("Test passed! \n")
    print(alist)

else:
    print("Failed! \n")
    print(alist)
