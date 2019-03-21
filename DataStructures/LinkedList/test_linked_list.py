from LinkedList import *
from random import randint

START_OF_VALUES = 100

END_OF_VALUES = 1000


def test_insert_front():
    """
    Testing insert front method.

    :return None:
    """
    _print_test_start("test_insert_front")
    # Test #1
    passed = True

    l = LinkedList()
    for i in range(10):
        l.insertFront(i)

    # l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    l.printList()
    _print_test_status(passed, "test_insert_front")


def test_insert_back():
    _print_test_start("test_insert_back")
    # Test #1
    passed = True

    l = LinkedList()
    for i in range(10):
        l.insertBack(i)

    l.printList()
    _print_test_status(passed, "test_insert_back")


def test_mix_insert_back_and_front():
    _print_test_start("test_mix_insert_back_and_front")
    # Test #1
    passed = True
    l = LinkedList()
    for i in range(20):
        if i % 2 == 0:
            l.insertBack(i)

        else:
            l.insertFront(i)

    l.printList()
    _print_test_status(passed, "test_mix_insert_back_and_front")


def test_search():
    _print_test_start("test_search")
    passed = True
    l = LinkedList()
    for i in range(50):
        l.insertBack(i)
    # Test #1

    # actual = l.search(25)
    temp = l.search(25)
    actual = [temp[0].value, temp[1]]
    expected = [25, 25]

    if actual != expected:
        print("Test #1")
        print("Actual is not equal to expected: " + " actual = " + str(actual) + ", expected = " + str(expected))
        passed = False


    # Test #2
    temp = l.search(100)
    actual = [temp[0], temp[1]]
    expected = [None, -1]

    if actual != expected:
        print("Test #2")
        print("Actual is not equal to expected: actual = " + str(actual) + ", expected = " + str(expected))
        passed = False

    _print_test_status(passed, "test_search")


def test_remove_front():
    _print_test_start("test_remove_front")
    passed = True

    l = LinkedList()

    # Test #0
    actual = l.removeFront()
    expected = None

    if actual != expected:
        print("Test #0")
        print("Actual is not equal to expected = " + str(actual) + ", expected = " + str(expected))
        passed = False

    for i in range(10):
        l.insertBack(i)

    # Test #1
    actual = l.removeFront()
    expected = 0

    if actual.value != expected:
        print("Test #1")
        print("Actual is not equal to expected = " + str(actual.value) + ", expected = " + str(expected))
        passed = False

    # test #2
    actual = l.removeFront()
    expected = 1

    if actual.value != expected:
        print("Test #2")
        print("Actual is not equal to expected = " + str(actual.value) + ", expected = " + str(expected))
        passed = False

    # test #3
    actual = l.removeFront()
    expected = 2

    if actual.value != expected:
        print("Test #3")
        print("Actual is not equal to expected = " + str(actual.value) + ", expected = " + str(expected))
        passed = False

    l.printList()
    _print_test_status(passed, "test_remove_front")


def test_remove_back():
    _print_test_start("test_remove_back")
    passed = True

    l = LinkedList()

    # Test 0
    actual = l.removeBack()
    expected = None

    if actual != expected:
        print("Test #0")
        print("Actual is not equal to expected = " + str(actual) + ", expected = " + str(expected))
        passed = False

    for i in range(25):
        l.insertBack(i)

    # Test #1
    actual = l.removeBack()
    expected = 24

    if actual.value != expected:
        print("Test #1")
        print("Actual is not equal to expected = " + str(actual.value) + ", expected = " + str(expected))
        passed = False

    # Test #2
    actual = l.removeBack()
    expected = 23

    if actual.value != expected:
        print("Test #2")
        print("Actual is not equal to expected = " + str(actual.value) + ", expected = " + str(expected))
        passed = False

    # Test #3
    actual = l.removeBack()
    expected = 22

    if actual.value != expected:
        print("Test #3")
        print("Actual is not equal to expected = " + str(actual.value) + ", expected = " + str(expected))
        passed = False

    # Test #4
    actual = l.removeBack()
    expected = 21

    if actual.value != expected:
        print("Test #4")
        print("Actual is not equal to expected = " + str(actual.value) + ", expected = " + str(expected))
        passed = False

    l.printList()
    _print_test_status(passed, "test_remove_back")


def test_mix_remove_front_back():
    _print_test_start("test_remove_back")
    passed = True

    l = LinkedList()

    # Test 0
    actual = l.removeBack()
    expected = None

    if actual != expected:
        print("Test #0")
        print("Actual is not equal to expected = " + str(actual) + ", expected = " + str(expected))
        passed = False

    for i in range(25):
        l.insertBack(i)


def test_remove():
    _print_test_start("test_remove")
    passed = True
    l = LinkedList()

    for i in range(50):
        l.insertBack(i)

    # Test #1
    actual = l.remove(10)
    expected = 10

    if actual.value != expected:
        print("Test #1")
        print("Actual is not equal to expected = " + str(actual.value) + ", expected = " + str(expected))
        passed = False

    # Test #2
    actual = l.remove(45)
    expected = 45

    if actual.value != expected:
        print("Test #2")
        print("Actual is not equal to expected = " + str(actual.value) + ", expected = " + str(expected))
        passed = False

    # Test #3
    actual = l.remove(40)
    expected = 40

    if actual.value != expected:
        print("Test #3")
        print("Actual is not equal to expected = " + str(actual.value) + ", expected = " + str(expected))
        passed = False

    # Print resulting ll
    l.printList()

    # Test #4
    l = LinkedList()
    l.insertBack(5)

    actual = l.remove(5)
    expected = 5

    if actual.value != expected:
        print("Test #4")
        print("Actual is not equal to expected = " + str(actual.value) + ", expected = " + str(expected))
        passed = False

    # Test #5
    l = LinkedList()
    l.insertBack(5)

    actual = l.remove(10)
    expected = None

    if actual != expected:
        print("Test #5")
        print("Actual is not equal to expected = " + str(actual) + ", expected = " + str(expected))
        passed = False

    # Test #6
    l = LinkedList()

    for i in range(100):
        l.insertBack(100)

    actual = l.remove(200)
    expected = None

    if actual != expected:
        print("Test #5")
        print("Actual is not equal to expected = " + str(actual) + ", expected = " + str(expected))
        passed = False

    _print_test_status(passed, "test_remove")


def test_find_mid_point():
    _print_test_start("test_find_mid_point")
    passed = True

    # Test #1
    l = _create_increasing_ordered_list(10)
    actual = l.findMidPoint()
    ## l.printList()
    passed = _print_test_result(1, 4, actual[0].value)
    passed = _print_test_result(1, 4, actual[1])

    # Test #2
    l = _create_decreasing_ordered_list(10)
    actual = l.findMidPoint()
    ## l.printList()
    passed = _print_test_result(2, 5, actual[0].value)
    passed = _print_test_result(2, 4, actual[1])

    # Test #3
    l = _create_increasing_ordered_list(200)
    actual = l.findMidPoint()
    ## l.printList()
    passed = _print_test_result(3, 99, actual[0].value)
    passed = _print_test_result(3, 99, actual[1])

    # Test #4
    l = _create_decreasing_ordered_list(200)
    actual = l.findMidPoint()
    ## l.printList()
    passed = _print_test_result(4, 100, actual[0].value)
    passed = _print_test_result(4, 99, actual[1])

    # Test #5
    l = _create_increasing_ordered_list(21)
    actual = l.findMidPoint()
    passed = _print_test_result(5, 10, actual[0].value)
    passed = _print_test_result(5, 10, actual[1])

    # Test #6
    l = _create_increasing_ordered_list(20)
    actual = l.findMidPoint()
    passed = _print_test_result(6, 9, actual[0].value)
    passed = _print_test_result(6, 9, actual[1])


    _print_test_status(passed, "test_find_mid_point")


def test_reverse( ):
    _print_test_start("test_reverse")
    passed = True

    # Test #1
    l = _create_increasing_ordered_list(20)
    l.printList()
    l.reverse()
    l.printList()

    actual = l.head
    expected = 19
    passed = _print_test_result(1, expected, actual.value)

    # Test #2
    l = _create_increasing_ordered_list(50)
    l.printList()
    l.reverse()
    l.printList()
    node = l.head

    for i in range(49, -1, -1):
        ## print("i = " + str(i) + ", value of head: " + str(node.value))
        passed = _print_test_result(2, i, node.value)
        node = node.next

    _print_test_status(passed, "test_reverse")


def test_reverse_up_to():
    _print_test_start("test_reverse_up_to")
    passed = True

    # Test #1
    l = _create_increasing_ordered_list(20)
    l.printList()
    actual = l.reverseUpTo(10)
    print("Original ll: ")
    l.printList()
    expected = _create_decreasing_ordered_list(10)
    actual_ll = LinkedList(actual)
    actual_ll.printList()

    actualNode = actual_ll.head
    expectedNode = expected.head

    while expectedNode != None and expectedNode.next != None:
        if expectedNode.value != actualNode.value:
            passed = False
            _print_test_result(1, expectedNode.value, actualNode.value)

        expectedNode = expectedNode.next
        actualNode = actualNode.next

    _print_test_status(passed, "test_reverse_up_to")


def test_reverse_up_to_node():
    _print_test_start("test_reverse_up_to_node")
    passed = True

    # Test #1
    print("\n\n Test number 1")
    l = _create_increasing_ordered_list(20)
    l.printList()
    middleNode, index = l.findMidPoint()
    print("MidPoint now: " +str(middleNode.value))

    actual = l.reverseUpToNode(middleNode)
    actual_ll = LinkedList(actual)
    actual_ll.printList()
    expected = _create_decreasing_ordered_list(10)

    actualNode = actual_ll.head
    expectedNode = expected.head

    while expectedNode != None and expectedNode.next != None:
        if expectedNode.value != actualNode.value:
            passed = _print_test_result(1, expectedNode.value, actualNode.value)

        expectedNode = expectedNode.next
        actualNode = actualNode.next

    # Test #2
    print("\n\n Test number 2")
    l = _create_increasing_ordered_list(21)
    l.printList()
    middleNode, index = l.findMidPoint()
    print("MidPoint now: " +str(middleNode.value))

    actual = l.reverseUpToNode(middleNode)
    actual_ll = LinkedList(actual)
    actual_ll.printList()
    expected = _create_decreasing_ordered_list(11)

    actualNode = actual_ll.head
    expectedNode = expected.head

    while expectedNode != None and expectedNode.next != None:
        if expectedNode.value != actualNode.value:
            passed = _print_test_result(1, expectedNode.value, actualNode.value)

        expectedNode = expectedNode.next
        actualNode = actualNode.next

    # Test #3 palindromes
    print("\n\n Test number 3")
    l = _create_palindrome_ll(20)
    l.printList()
    middleNode, index  = l.findMidPoint()
    print("MidPoint now: " +str(middleNode.value))
    print("Next value after midPoint: " + str(middleNode.next.value))

    actual = l.reverseUpToNode(middleNode)
    actual_ll = LinkedList(actual)
    reversedMidNode, rIndex = actual_ll.findMidPoint()
    print("RMidPoint now: " + str(reversedMidNode.value))
    print("Next value after rMidePoint: " + str(reversedMidNode.next.value))
    actual_ll.printList()
    expected = _create_decreasing_ordered_list(10)

    actualNode = actual_ll.head
    expectedNode = expected.head

    while expectedNode != None and expectedNode.next != None:
        if expectedNode.value != actualNode.value:
            passed = _print_test_result(1, expectedNode.value, actualNode.value)

        expectedNode = expectedNode.next
        actualNode = actualNode.next


    _print_test_status(passed, "test_reverse_up_to_node")


def test_is_palindrome():
    _print_test_start("test_isPalindrome")
    passes = []

    # Test #1
    print("\n\n Test #1")
    l = _create_palindrome_ll(20)
    l.printList()
    actual = l.isPalindrome()
    expected = True
    passes.append(_print_test_result(1 ,expected, actual))

    # Test #2
    print("\n\n Test #2")
    l = _create_palindrome_ll(21)
    l.printList()
    actual = l.isPalindrome()
    expected = True
    passes.append(_print_test_result(2, expected, actual))

    # Test #3
    print("\n\n Test #3")
    l = _create_increasing_ordered_list(10)
    l.printList()
    actual = l.isPalindrome()
    expected = False
    passes.append(_print_test_result(3, expected, actual))

    # Test #4
    print("\n\n Test #4")
    l = _create_increasing_ordered_list(21)
    l.printList()
    actual = l.isPalindrome()
    expected = False
    passes.append(_print_test_result(4, expected, actual))

    # Test #5
    print("\n\n Test #5")
    l = _create_decreasing_ordered_list(10)
    l.printList()
    actual = l.isPalindrome()
    expected = False
    passes.append(_print_test_result(5, expected, actual))

    # Test #6
    print("\n\n Test #6")
    l = _create_decreasing_ordered_list(21)
    l.printList()
    actual = l.isPalindrome()
    expected = False
    passes.append(_print_test_result(6, expected, actual))

    _print_test_status(all(passes), "test_isPalindrome")


def test_getItem():
    _print_test_start("test_getItem")
    passed = True

    ll = _create_increasing_ordered_list(100)

    # Test #1
    try:
        actual = ll.getItem(50)

    except IndexError:
        print("Error occurred!")
        actual = -1

    if actual == -1:
        passed = _print_test_result(1, 49, actual)

    else:
        passed = _print_test_result(1, 49, actual.value)

    # Test #2
    try:
        actual = ll.getItem(1000)

    except IndexError:
        print("Error occurred!")
        actual = -1

    if actual == -1:
        passed = _print_test_result(2, -1, actual)

    else:
        passed = _print_test_result(2, -1, actual.value)

    _print_test_status(passed, "test_getItem")


def test_print():
    l = _create_random_linked_list(10)
    l.printList()


# Helper functions
def _create_random_linked_list(length):
    ll = LinkedList()
    for i in range(length):
        ll.insertFront(randint(START_OF_VALUES, END_OF_VALUES))

    return ll


def _create_increasing_ordered_list(length):
    ll = LinkedList()
    for i in range(length):
        ll.insertBack(i)

    return ll


def _create_decreasing_ordered_list(length):
    ll = LinkedList()
    for i in range(length):
        ll.insertFront(i)

    return ll


def _create_ll_between_bounds(first, last):
    ll = LinkedList()
    if first >= last:

        for i in range(first, last + 1):
            ll.insertBack(i)

    else:
        for i in range(last, first + 1):
            ll.insertFront(i)

    return ll


def _create_palindrome_ll(length):
    ll = LinkedList()

    if length % 2 == 0:
        for i in range(int(length/ 2)):
            ll.insertBack(i)

        for i in range(int(length / 2) - 1, -1, -1):
            ll.insertBack(i)

    else:
        for i in range(int(length / 2) + 1):
            ll.insertBack(i)

        for i in range(int(length / 2) - 1, -1, -1):
            ll.insertBack(i)

    return ll


def _print_test_start(testName):
    print("Testing " + testName + " ...")


def _print_test_status(passed, testName):
    if passed:
        print(testName + ": " + "Test Passed! \n")

    else:
        print(testName + ": " + "Test Failed! \n")


def _print_test_result(numTest, expected, actual):
    if actual != expected:
        print("Test #" + str(numTest))
        print("Actual is not equal to expected: actual = " + str(actual) + ", expected = " + str(expected))
        return False

    return True


def run_tests():
    # Print unit test
    test_print()

    # Insert front unit test
    test_insert_front()

    # Insert back unit test
    test_insert_back()

    # Insert mix back and front unit test
    test_mix_insert_back_and_front()

    # Search unit test
    test_search()

    # Remove front unit test
    test_remove_front()

    # Remove back unit test
    test_remove_back()

    # Remove unit test
    test_remove()

    # Find mid point unit test
    test_find_mid_point()

    # Reverse unit test
    test_reverse()

    # Reverse up to unit test
    test_reverse_up_to()

    # Reverse up to node unit test
    test_reverse_up_to_node()

    # Is palindrome unit test
    test_is_palindrome()


run_tests()
