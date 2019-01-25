from Node import Node


class LinkedList:
    def __init__(self):
        self.head = None

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
        First search for the first occurrence of the given value 'k' in this linked list. If found remove the Node containing the value 'k'  from the list.
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

    def printList(self):
        # Debug
        toPrint = False

        printStr = "["
        while self.head != None:
            if toPrint:
                print("Head is not null! ")

            printStr += str(self.head.value) + ", "

            if toPrint:
                print("My current printStr: " + printStr)

            self.head = self.head.next

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
