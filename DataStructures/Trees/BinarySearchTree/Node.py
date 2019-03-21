# Node for BST:
class Node:
    def __init__(self, key):
        self._key = key
        self._parent = Node(None)
        self._left = Node(None)
        self._right = Node(None)
