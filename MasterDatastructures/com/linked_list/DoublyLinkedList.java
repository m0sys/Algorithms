// Date: 2020/2/6.
// Implementing Doubly Linkedlist datastructure based 
// on William Fiset's ds lecture series. 
//
import java.util.Iterator;

public class DoublyLinkedList<T> implements Iterable<T> {
    private int size = 0;
    private Node<T> head = null;
    private Node<T> tail = null;

    // Internal node class to represent data.
    private static class Node<T> {
        private T data;
        private Node<T> prev, next;

        public Node(T data, Node<T> prev, Node<T> next) {
            this.data = data;
            this.prev = prev;
            this.next = next;
        }

        @Override
        public String toString() {
            return data.toString();
        }
    }

    /** Empty this linked list, O(n) */
    public void clear() {
        Node<T> trav = head;
        while (trav != null) {
            Node<T> next = trav.next;
            trav.prev = trav.next = null;
            trav.data = null;
            trav = next;
        }
        head = tail = trav = null;
        size = 0;
    }

    /** Return the size of this linked list. */
    public int size() {
        return size;
    }

    /** Is this linked list empty? */
    public boolean isEmpty() {
        return size() == 0;
    }

    /** Add an element to the tail of the linked list, O(1). */
    public void add(T elem) {
        addLast(elem);
    }

    /** Add a node to the tail of the linked list, O(1). */
    public void addLast(T elem) {
        if (isEmpty()) {
            head = tail = new Node<T>(elem, null, null);
        } else {
            tail.next = new Node<T>(elem, tail , null);
            tail = tail.next;
        }
        size++;
    }

    /** Add an element to the beginning to this linked list, O(1).  */
    public void addFirst(T elem) {
        if (isEmpty()) {
            head = tail = new Node<T>(elem, null, null);
        } else {
            head.prev = new Node<T>(elem, null, head);
            head = head.prev;
        }
        size++;
    }

    /** Add an element at a specificed index. */
    public void addAt(int index, T data) throws Exception {
        if (index < 0) {
            throw new Exception("Illegal Index");
        }

        if (index == 0) {
            addFirst(data);
            return;
        }

        if (index == size) {
            addLast(data);
            return;
        }

        Node<T> temp = head;
        for (int i = 0; i < index - 1; i ++) {
            temp = temp.next;
        }

        Node<T> newNode = new Node(data, temp, temp.next);
        temp.next.prev = newNode;
        temp.next = newNode;
        size++;
    }
    /** Check the value of the first node if it exists, O(1). */
    public T peekFirst() {
        if (isEmpty()) throw new RuntimeException("Empty list");
        return head.data;
    }

    /** Check the value of the last node if it exists, O(1). */
    public T peekLast() {
        if (isEmpty()) throw new RuntimeException("Empty list");
        return tail.data;
    }

    /** Remove the first value at the head of the linked list, O(1). */

    public T removeFirst() {
        if (isEmpty()) throw new RuntimeException("Empty list");

        // Extract the data at the head and move
        // the head pointer forwards one node.
        T data = head.data;
        head = head.next;
        --size;

        // IF the list is empty set the tail to null.
        if (isEmpty()) tail = null;

        // Do a memory cleanup of the previous node.
        else head.prev = null;

        /** Return the data that was at the first ndoe we just removed. */
        return data;
    }

    /** Remove the last value at the trail of the linked list, O(1). */
    public T removeLast() {
        if (isEmpty()) throw new RuntimeException("Empty list");

        // Extract the data at the tail and move
        // the tail pointer backward one node.
        T data = tail.data;
        tail = tail.prev;
        --size;

        // If the list is empty set the head to null.
        if (isEmpty()) head = null;

        // Do a memory clean of the node that was just removed.
        else tail.next = null;

        // Return the data that was in the last node we just removed.
        return data;
    }

    /** Remove an arbitrary node from the linked list, O(1). */
    private T remove(Node<T> node) {
        // If the node to remove is at tail or head.
        if (node.prev == null) return removeFirst();
        if (node.next == null) return removeLast();

        // Mkae te pointers of adj nodes skip over 'node'.
        node.next.prev = node.prev;
        node.prev.next = node.next;

        // Temporarily store data we want to return.
        T data = node.data;

        // Memory cleanup.
        node.data = null;
        node = node.prev = node.next = null;
        --size;

        // Return the data in the node we just removed.
        return data;
    }

    /** Remove a  node at a particular index, O(n). */
    public T removeAt(int index) {
        if (index <0 || index >= size) {
            throw new IllegalArgumentException();
        }

        int i;
        Node<T> trav;
        
        // Search from the front of the list.
        if (index < size / 2) {
            for (i = 0, trav = head; i != index; i++) {
                trav = trav.next;
            }
        } else {
            for (i = size, trav = tail; i != index; i--) {
                trav = trav.prev;
            }
        }
        return remove(trav);
    }

    /** Remove a particular value in the linked list, O(n) */
    public boolean remove(Object obj) {
        // Support searching for null.
        if (obj == null) {
            for (Node<T> trav = head; trav != null; trav = trav.next) {
                if (trav.data == null) {
                    remove(trav);
                    return true;
                }
            }
        }

        // Search for non null object.
        else {
            for (Node<T> trav = head; trav != null; trav = trav.next) {
                if (obj.equals(trav.data)) {
                    remove(trav);
                    return true;
                }
            }

        }
        return false;
    }

    /** Find the index of a particular value in the linked list, O(n). */
    public int indexOf(Object obj) {
        int index = 0;
        Node<T> trav = head;

        // Support searching for null.
        if (obj == null) {
            for (; trav != null; trav = trav.next, index++) {
                if (trav.data == null) {
                    return index;
                }
            }
        }

        else {
            for (; trav != null; trav = trav.next, index++) {
                if (obj.equals(trav.data)) {
                    return index;
                }
            }
        }
        return -1;
    }

    /** Check if a value is contained within the linked list. */
    public boolean contains(Object obj) {
        return indexOf(obj) != -1;
    }

    @Override
    public Iterator<T> iterator() {
        return new Iterator<T>() {
            private Node<T> trav = head;

            @Override
            public boolean hasNext() {
                return trav != null;
            }

            @Override
            public T next() {
                T data = trav.data;
                trav = trav.next;
                return data;
            }

            @Override
            public void remove() {
                throw new UnsupportedOperationException();
            }
        };
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("[ ");
        Node<T> trav = head;
        while (trav != null) {
            sb.append(trav.data + ", ");
            trav = trav.next;
        }
        sb.append(" ]");
        return sb.toString();
    }
}