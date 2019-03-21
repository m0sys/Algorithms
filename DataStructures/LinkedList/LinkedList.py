from Node import Node


class LinkedList:
    def __init__(self, node=None):
        self.head = node

    def insertFront(self, newValue):
        # Debug
        toPrint = False
        newNode = Node(newValue)

        if toPrint:
            print("New Node value = " + str(newNode.value))

        newNode.next = self.head

        if toPrint:
            print("New Node dot next = " + str(newNode.next))

            if newNode.next != None:
                print("Value of new node dot next = " + str(newNode.next.value))

        self.head = newNode

    def insertBack(self, newValue):
        newNode = Node(newValue)

        # List is empty
        if self.head == None:
            self.insertFront(newValue)
            return

        # List is not empty
        tail = self.head
        while tail.next != None:
            tail = tail.next

        tail.next = newNode

    def insertNodeFront(self, newNode):
        pass


    def insertNodeBack(self, newNode):
        pass

    def extend(self, newll):
        pass


    def search(self, k):
        """
        Finds the first element with value k in this linked list by a simple linear search,
        returning a list containing the node of this element and its' index. If the element is not within this linked list, search
        will return a list container the values None and '-1'.



        :complexity = big O of n.

        :param k: (type) -> element to find within this linked list.
        :return [x, index]: x -> Node of the element found or None; index: int -> The index of the the element.
        """
        x = self.head
        index = 0
        while x != None and x.value != k:
            x = x.next
            index += 1

        # Check to see if element was found.
        if x == None:
            index = -1

        return [x, index]

    def removeFront(self):
        """
        Remove the first element in the linked list and return it.
        :return removed: Node or None -> element removed
        """
        # Check to see if list is empty.
        if self.head == None:
            return None

        # List is not empty.
        removed = self.head
        self.head = self.head.next
        return removed

    def removeBack(self):
        """
        Remove the last element in the linked list and return it.
        :return: tail: Node or None -> element removed
        """
        # Check to see if list is empty.
        if self.head == None:
            return None

        tail = self.head
        prevTail = self.head

        while tail.next != None:
            tail = tail.next
            if tail.next != None:
                prevTail = prevTail.next

        prevTail.next = None # remove tail
        return tail

    def remove(self, k):
        """
        First search for the first occurrence of the given value 'k' in this
        linked list. If found remove the Node containing the value 'k'  from the
        list.
        :param k:
        :return removed: Node or None -> element removed
        """
        prev = self._find_previous(k)

        # Check empty list or zero occurrence found.
        if prev == None:
            return None

        # Prev is first element
        if prev == self.head:
            return self.removeFront()

        x = prev.next
        prev.next = x.next
        return x

    def findMidPoint(self):
        """
        Find the mid point of the linked list.
        :return: slow: Tuple(x: Node or None, count: int) -> element in the middle of this linked list and its' index in a tuple.
        """
        count = 0
        fast = self.head
        slow = self.head

        while fast != None and fast.next != None and fast.next.next != None:
            count += 1
            fast = fast.next.next
            slow = slow.next

        return (slow, count)

    def reverse(self):
        """
        Reverse the linked list.
        :return: None
        """
        # Debug
        toPrint = False
        if toPrint:
            print("Debugging reverse method! \n")

        lostNode = self.head
        prev = self.head
        x = self.head

        if toPrint:
            print("Lost Node value: " + str(lostNode.value))
            print("Prev Node value: " + str(prev.value))
            print("X Node value: " + str(x.value))

        while lostNode != None and lostNode.next != None:
            x = lostNode
            if toPrint:
                print("Is x == self.head? " + str(x == self.head))

            if x == self.head:
                if toPrint:
                    print("X is equal to head!")
                lostNode = lostNode.next
                x.next = None
                if toPrint:
                    print("Value of x: " + str(x.value))
                    print("Value of lostNode: " + str(lostNode.value))
            else:
                if toPrint:
                    print("X is not equal to head!")
                lostNode = lostNode.next
                x.next = prev
                prev = x

                ## if lostNode.next == None:
                ##     x = lostNode
                ##     x.next = prev
                ##     prev = x

            if toPrint:
                print("Value of lostNode: " + str(lostNode.value))
                print("Value of x: " + str(x.value))
                print("Value of prev: " + str(prev.value))

        # Add Last Node
        x = lostNode
        x.next = prev

        self.head = x

    def reverseUpTo(self, i):
        """
        Reverse the list only up to element at index <i>.

        :param i: index where the reverse process stops
        :return x: node pointing to a sublist of the original list in reverse order
        """
        lostNode = self.head
        x = self.head
        prev = self.head
        firstElem = self.head
        counter = 0

        while lostNode != None and lostNode.next != None and counter < i:
            counter += 1
            x = lostNode

            if x == self.head:
                lostNode = lostNode.next
                x.next = None

            else:
                lostNode = lostNode.next
                x.next = prev
                prev = x


        if i - counter == 1:
            # Add Last Node
            x = lostNode
            x.next = prev

        elif i - counter != 0:
            # Raise Index Error
            # raise IndexError
            pass


        # Update head and concatenate reversed node with the rest of the
        # original ll.
        self.head = x
        firstElem.next = lostNode

        return x

    def reverseUpToNode(self, node):
        """
        Reverse the list up to the node and including <node>.

        :param node: element in this ll where the reverse process stops
        :return x: node pointing to a sublist of the original list in reverse order
        """
        lostNode = self.head
        x = self.head
        prev = self.head
        firstElem = self.head

        while lostNode != None and lostNode.next != None and lostNode != node:
            x = lostNode

            if x == self.head:
                lostNode = lostNode.next
                x.next = None

            else:
                lostNode = lostNode.next
                x.next = prev
                prev = x

        if x != node:
            if lostNode == node:
                # Add Last Node
                x = lostNode
                lostNode = lostNode.next
                x.next = prev

        ## print("lostNode final value: " + str(lostNode.value))
        ## print("lostNode next value: " + str(lostNode.next.value))
        ## print("x final value: " + str(x.value))
        ## print("x next value: " + str(x.next.value))

        # Update head and concatenate reversed node with the rest of the
        # original ll.
        self.head = x
        firstElem.next = lostNode

        return x

    def isPalindrome(self):
        """
        Check to see if this ll is a palindrome or not.

        For a ll to be a palindrome all elements from the mid point and on should
        be a 'mirror' reflection of all the elements before the mid point.
        Here 'mirror' is used to refer to all properties that apply
        when light is reflected off of a physical mirror. Specifically speaking
        it is referring to the pi/2 rotation that is present when holding a writen
        note in front of a mirror.

        === Invariants ===
        Solves the problem in O(n) steps and O(1) additional steps regardless of
        n.

        :return: {bool}
        """
        ## print("isPalindrome debugging!")
        midPoint, indexOfMid = self.findMidPoint()
        nextMidPoint = midPoint.next
        print("MidPoint: " + str(midPoint.value) + ", nextMidPoint: " + str(nextMidPoint.value))
        print("Index of Mid: " + str(indexOfMid))
        if indexOfMid % 2 == 0:
            # len is odd
            nextMidPoint
            reverseX = self.reverseUpTo(indexOfMid)

        else:
            # len is even
            reverseX = self.reverseUpTo(indexOfMid + 1)

        print("My orginal self: ")
        self.printList()

        while reverseX != None and reverseX.next != None and nextMidPoint != None and nextMidPoint.next != None:
            print("reverseX value: " + str(reverseX.value) + ", nMidPointX.value: " + str(nextMidPoint.value))
            if reverseX.value != nextMidPoint.value:
                return False
            reverseX = reverseX.next
            nextMidPoint = nextMidPoint.next

        return True

    def getItem(self, i):
        """
        Get item at index <i>.

        Raise IndexError if i is out of range or greater than the length of the list.

        :param i: int -> index of item that the user wants.:
        :return item: None or Node -> node at index <i>:
        """
        x = self.head
        index = 0
        while x != None and x.next != None and index != i:
            x = x.next
            index += 1

        if index != i:
            raise IndexError()

        return x

    def printList(self):
        # Debug
        toPrint = False

        x = self.head

        printStr = "["
        while x != None:
            if toPrint:
                print("Head is not null! ")

            printStr += str(x.value) + ", "

            if toPrint:
                print("My current printStr: " + printStr)

            x = x.next

        print(printStr[:-2] + "]")

    # Helper Functions
    def _find_previous(self, k):
        """
        Find the previous node to the first Node with value k.

        :param k: int -> value of the node.
        :return: prev: Node or None -> the previous node to node k.
        """
        x = self.head
        prev = self.head

        while x != None and x.value != k:
            x = x.next
            if x != None and x.value != k:
                prev = prev.next

            elif x == None: # reached the end of the list and did not find k
                return None

        return prev
