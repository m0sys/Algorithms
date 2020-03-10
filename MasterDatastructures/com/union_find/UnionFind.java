// Date: 2020/3/1.
// Implementing Union Find (Disjoin Set) datastructure based 
// on William Fiset's ds lecture series. 

package com.union_find;

public class UnionFind {
    // The number of elements in the union find.
    private int size;

    // Used to track the size of each of the components.
    private int[] sz;

    // id[i] points to the parent of i; if id[i] = i then i is a root node.
    private int[] id;

    // Tracks the number of components in the union find.
    private int numComponents;

    public UnionFind(int size) {
        if (size <= 0) throw new IllegalArgumentException("Size <= 0 is not allowed");
        this.size = numComponents = size;
        sz = new int[size];
        id = new int[size];

        for (int i = 0; i < size; i++) {
            id[i] = i; // link to itself (self root)
            sz[i] = 1; // each component is originally of size one
        }
    }

    // Find which component/set 'p' belongs to, takes amortized constant time.
    public int find(int p) {
        // Find the root of the component/set.
        int root = p;
        while (root != id[root]) root = id[root];

        // Compress the path leading back to the root.
        // Doing this operation is called "path compression"
        // and it is what gives us amortized time complexity.
        // Note that due to previous step root is not the root node of p.

        while (p != root) {
            int next = id[p];
            id[p] = root;
            p = next;
        }

        return root;
    }

    /*
     * This is an alternative recursive formulation for the find method.
     * public int find(int p) {
     *  if (p == id[p]) return p;
     *  return id[p] = find(id[p]);
     * }
    */

    /*
     * Return whether or not the elements 'p' and 
     * 'q' are in the same component/set.
     */
    public boolean connected(int p, int q) {
        return find(p) == find(q);
    }

    // Return the size of the component/set that 'p' belongs to.
    public int componentSize(int p) {
        return sz[find(p)];
    }

    // Returns the number of remaining components/sets.
    public int components() {
        return numComponents;
    }

    // Unify the components/sets containing element 'p' and 'q'.
    public void unify(int p, int q) {
        int root1 = find(p);
        int root2 = find(q);

        // They are in the same group.
        if (root1 == root2) {
            return;
        }

        // Merge smaller component/set into the larger one.
        if (sz[root1] <= sz[root2]) {
            sz[root2] += sz[root1];
            id[root1] = root2;
        } else {
            sz[root1] += sz[root2];
            id[root2] = root1;
        }

        numComponents--;
    }

    public static void main(String args[]) {
        UnionFind uf = new UnionFind(10);
        System.out.println("find 2: " + uf.find(2));
        uf.unify(2, 1);
        System.out.println("find 2: " + uf.find(2));
        System.out.println("find 1: " + uf.find(1));
        uf.unify(3, 1);
        System.out.println("find 2: " + uf.find(2));
        System.out.println("find 3: " + uf.find(3));
        System.out.println("find 1: " + uf.find(1));
        uf.unify(4, 2);
        System.out.println("size of 2: " + uf.componentSize(2));
        System.out.println("size of 3: " + uf.componentSize(3));
    }
}