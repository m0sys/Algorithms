import sys
sys.path.append('../3.0_Data_Structures/12.0_Binary_Search_Trees/')

from binary_search_tree import BST
from __future__ import annotations

class Node:
    def __init__(key: int):
        self.key = key
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(root: Node):
        self.root = Node
        self.left = None
        self.right = None

    def insert_node(n: Node):
        # TODO: implement generic binary tree insert.
        pass


def breath_first_search(T: BST):
    queue = [T]
    result = []
    while queue:
        cur_node = queue.remove(0)
        if cur.left is not None:
            queue.append(cur.left)
        if cur.right is not None:
            queue.append(cur.right)
        result.append(cur.key)
    return result

if __name__ == "__main__":
    bst = BST(1)
    bst.insert(4)
    bst.insert(2)
    bst.insert(3)
    bst.insert(3)







