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


def test_print():
    l = _create_random_linked_list(10)
    l.printList()


# Helper functions
def _create_random_linked_list(length):
    l = LinkedList()
    for i in range(length):
        l.insertFront(randint(START_OF_VALUES, END_OF_VALUES))

    return l


def _print_test_start(testName):
    print("Testing " + testName + " ...")


def _print_test_status(passed, testName):
    if passed:
        print(testName + ": " + "Test Passed! \n")

    else:
        print(testName + ": " + "Test Failed! \n")


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


run_tests()
