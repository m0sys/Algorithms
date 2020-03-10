/**
 * Date: 2020/2/8.
 * Implementing AVL Tree datastructure based 
 * on William Fiset's ds lecture series. 
 */

 package com.avl_tree;

 import com.utils.TreePrinter;
 import com.utils.TreePrinter.PrintableNode;


 public class AVLTree<T extends Comparable<T>> implements Iterable<T> {
     public class Node implements PrintableNode {
         // 'bf' is short for Balance Factor.
         public int bf;

         // The value/data contained within the node.
         public T value;

         // The height of this node in the tree.
         public int height;

         // The left and the right children of this node.
         public Node left, right;

         public Node(T value) {
             this.value = value;
         }
         @Override
         public PrintableNode getLeft() {
           return left;
         }

         @Override
         public PrintableNode getRight() {
           return right;
         }

         @Override
         public String getText() {
           return value.toString();
         }

     }

     // The root node of the AVL tree.
     public Node root;

     // Tracks the number of nodes inside the tree.
     private int nodeCount = 0;

     // Special token value used as an aternative to returning 'null'.
     // The TOKEN is used to indicate special return signals. For example,
     // we can return the TOKEN instead of null when we're inserting a new item
     // and discover the value we were inserting already exists in the tree.
     private Node TOKEN = new Node(null);

     // The height of a rooted tree is the number of edges between the tree's
     // root and its deepest leaf. This means that a tree containing a single node
     // has a height of 0.
     public int height() {
         if (root == null) return 0;
         return root.height;
     }

     // Returns the number of nodes in the tree.
     public int size() {
         return nodeCount;
     }

     // Returns whether or not the tree is empty.
     public boolean isEmpty() {
         return size() == 0;
     }

     // Return true/false depending on whether a value exists in the tree.
     public boolean contains(T value) {
         Node node = root;
         while (node != null) {
             // Compare current value to the value in the node.
             int cmp = value.compareTo(node.value);
             
             if (cmp < 0) node = node.left;
             else if (cmp > 0) node = node.right;
             else return true;

         }
         return false;
     }


     // Insert/add a value to the AVL tree. The value must not be null, O(log(n))
     public boolean insert(T value) {
         if (value == null) return false;
         Node newRoot = insert(root, value);
         boolean insertedNode = (newRoot != TOKEN);
         if (insertedNode) {
             nodeCount++;
             root = newRoot;
         }
         return insertedNode;
     }

     // Inserts a vlaue inside the AVL tree. This method retunrs 'TOKEN' if
     // the value we tried to insert was already inside the tree, otherwise
     // the new (or old) root node is returned.
     private Node insert(Node node, T value) {
         // Base case.
         if (node == null) return new Node(value); // found local with no child

         // Compare current value to the vlaue in the node.
         int cmp = value.compareTo(node.value);

         // Insert node in the left subtree if true.
         if (cmp < 0) {
             Node newLeftNode = insert(node.left, value);
             if (newLeftNode == TOKEN) return TOKEN; // found duplicate value
             node.left = newLeftNode;
             // Insert node in the right susbtree if true.
         } else if (cmp > 0) {
             Node newRightNode = insert(node.right, value);
             if (newRightNode == TOKEN) return TOKEN;
             node.right = newRightNode;

             // Return 'TOKEN' to indicate a duplicate value in the tree.
         } else return TOKEN;

         // Update balance  factor and height values.
         update(node);

         // Re-balance tree.
         return balance(node);
     }

     // Update a node's height and balance factor.
     private void update(Node node) {
         // If node is a leaf return -1 for both children in order to have height 0.
         int leftNodeHeight = (node.left == null) ? -1: node.left.height;
         int rightNodeHeight = (node.right == null) ? -1: node.right.height;

         // Update this node's height.
         node.height = 1 + Math.max(leftNodeHeight, rightNodeHeight);

         // Update balance factor.
         node.bf = rightNodeHeight - leftNodeHeight;
     }

     // Re-balance a node if this balance factor is +2 or -2.
    private Node balance(Node node) {
        // Left heavy subtree.
        if (node.bf == -2) {
            // Left-Left case.
            if (node.left.bf <= 0) {
                return leftLeftCase(node);
                // Left-Right case.
            } else {
                return leftRightCase(node); // Rotate left, then rotate right.
            } 
            // Right heavy subtree needs balancing.
        } else if (node.bf == +2) {
            // Right-Right case.
            if (node.right.bf >= 0) {
                return rightRightCase(node);
                // Right-Left case.
            } else {
                return rightLeftCase(node); // rotate right, then rotate left.
            }
        }
        // Node either has a balance factor of 0, +1, -1, which is fine.
        return node;

    }

    private Node leftLeftCase(Node node) {
        return rightRotation(node);
    }

    private Node leftRightCase(Node node) {
        node.left = leftRotation(node.left);
        return leftLeftCase(node);
    }

    private Node rightRightCase(Node node) {
        return leftRotation(node);
    }

    private Node rightLeftCase(Node node) {
        node.right = rightRotation(node.right);
        return rightRightCase(node);
    }

    private Node leftRotation(Node node) {
        Node newParent = node.right;
        node.right = newParent.left;
        newParent.left = node;
        update(node);
        update(newParent);
        return newParent;
    }

    private Node rightRotation(Node node) {
        Node newParent = node.left;
        node.left = newParent.right;
        newParent.right = node;
        update(node);
        update(newParent);
        return newParent;
    }

    // Remove a value from tis binary tree if it exists, O(log(n)).
    public boolean remove(T elem) {
        Node newRoot = remove(root, elem);
        boolean removeNode = (newRoot != TOKEN) || (newRoot == null); 
        if (removeNode) {
            root = newRoot;
            nodeCount--;
            return true;
        }
        return false;
    }

    // Removes a value from the AVL tree. If the value we're trying to remove
    // does not exist in the tree then the 'TOKEN' value is returned. Otherwise.
    // the new (or old) root node is returned.
    private Node remove(Node node, T elem) {
        // Return 'TOKEN' to indicate value to remove was not found.
        if (node == null) return TOKEN;

        int cmp = elem.compareTo(node.value);

        // Dig into the left subtree, the value we're looking 
        // for is smaller than the current value.
        if (cmp < 0) {
            Node newLeftNode = remove(node.left, elem);
            if (newLeftNode == TOKEN) return TOKEN;  
            node.left = newLeftNode;
            // DIg into the right subtree.
        } else if (cmp > 0) {
            Node newRightNode = remove(node.right, elem);
            if (newRightNode == TOKEN) return TOKEN;
            node.right = newRightNode;
            // Found the node we wish to remove.
        } else {
            // This is the case with only a right subtree or no subtree at all.
            // Swap the node to be removed with right subtree.
            if (node.right == null) {
                return node.right;
                // This is the case with only a left subtree or no subtree at all.  
                // Swap the node to be removed with left subtree.
            } else if (node.right == null) {
                return node.left;
                // When removing a node from a binary tree with two links the 
                // successor of the node being removed can either be the largest 
                // value in the left subtree or the smallest value in the right
                // subtree. As a heuristic, the subtree with the most nodes will 
                // be removed in hopes that this may help with balancing. -william
            } else {
                // Choose to remove from left subtree
                if (node.left.height > node.right.height) {
                    // Swap the value of the successor ino the node.

                    // TODO: To optimize find max should return the node
                    //  so that there is no need to search for successor value
                    // for a second time.
                    T successorValue = findMax(node.left); // predecesor
                    node.value = successorValue;
                    Node replacement = remove(node.left, successorValue);
                    if (replacement == TOKEN) return TOKEN;
                    node.left = replacement;
                } else {
                    // Swap the value of the successor in to the node.

                    T successorValue = findMin(node.right); // successor                     
                    node.value = successorValue;

                    // Go into the right subtree and remove the left most node
                    // can find.
                    Node replacement = remove(node.right, successorValue);
                    if (replacement == TOKEN) return TOKEN;
                    node.right = replacement;
                }
            }
        }
        // Update balance factor and height values.
        update(node);
        // Re-balance tree.
        return balance(node);
    } 

    public void inOrderWalk(Node node) {
        if (node == null) return;
            if (node.left != null) inOrderWalk(node.left);
            System.out.println(node.value);
            if (node.right != null) inOrderWalk(node.right);
    }


    // Helper method to find leftmost node.
    private T findMin(Node node) {
        while (node.left != null) node = node.left;
        return node.value;
    }


    // Helper method to find rightmost node.
    private T findMax(Node node) {
        while (node.right != null) node = node.right;
        return node.value;
    }


    // Make sure bst invarient holds.
    boolean validateBSTInvarient(Node node) {
        if (node == null) return true;
        T val = node.value;
        boolean isValid = true;
        if (node.left != null) isValid = isValid && node.left.value.compareTo(val) < 0;
        if (node.right != null) isValid = isValid && node.right.value.compareTo(val) > 0;
        return isValid && validateBSTInvarient(node.left) && validateBSTInvarient(node.right);
    }


    // Returns as iterator to traverse the tree in order.
    public java.util.Iterator<T> iterator() {
        final int expectedNodeCount = nodeCount;
        final java.util.Stack<Node> stack = new java.util.Stack<>();
        stack.push(root);

        return new java.util.Iterator<T>() {
        Node trav = root;

        @Override
        public boolean hasNext() {
          if (expectedNodeCount != nodeCount) throw new java.util.ConcurrentModificationException();
          return root != null && !stack.isEmpty();
        }

        @Override
        public T next() {

          if (expectedNodeCount != nodeCount) throw new java.util.ConcurrentModificationException();

          while (trav != null && trav.left != null) {
            stack.push(trav.left);
            trav = trav.left;
          }

          Node node = stack.pop();

          if (node.right != null) {
            stack.push(node.right);
            trav = node.right;
          }

          return node.value;
        }

        @Override
        public void remove() {
          throw new UnsupportedOperationException();
        }
    }; 
  }

  @Override
  public String toString() {
      return TreePrinter.getTreeDisplay(root);
  }
  public static void main(String args[]) {
      AVLTree<Integer> avl = new AVLTree<Integer>();
      avl.insert(22);
      avl.insert(3);
      avl.insert(4);
      avl.insert(15);
      avl.insert(25);
      avl.insert(0);
      avl.insert(8);
      avl.insert(29);
      avl.insert(19);
      avl.insert(12);
      avl.insert(7);
      avl.insert(11);
      System.out.println(avl.toString());
      avl.remove(19);
      System.out.println(avl.toString());

    }
}