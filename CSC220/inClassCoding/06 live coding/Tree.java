/*
Name:     	[Your Name Here]
Date:       [Current Date Here]
Course:     CSC 220 - Data Structures
*/

public class Tree {

    /**
     * Default constructor - tree has no TNodes by default
     */
    public Tree() {
		
    }

    /**
     * Returns true if empty and false otherwise
     * @return 			true if empty, false otherwise
     */
    public boolean isEmpty() {
    	return false;
    }

    /**
     * Returns true if full and false otherwise
     * @return 			true if full, false otherwise
     */
    public boolean isFull() {
    	return false;
    }

    /**
     * Adds a node to the tree in the proper position (preserves binary search tree properties)
     * @param 			data - data to add to the tree
     */
    public void add(int data) {

    }

    /**
     * Private recursive function that takes a Node attached to its own
     * subtrees, and attaches the data to the tree in the proper location.
     * @param 			data - data to add to the tree
     * @param 			parent - potential parent Node of incoming data
     */
    private void add(int data, TNode parent) {
    	// Case 1 - the new node is smaller than the current parent node

		// Case 2 - the new node is larger than the current parent node

		// Case 3 - the new node is equal to the current parent node, so we don't add it (do nothing)
    }

    /**
     * Returns the the in-order traversal of the tree as a string, or "NULL" if the tree is empty
     * @return 			in-order traversal of the tree as a string (NULL if empty)
     */
    public String toString() {
		return "";
    }

    /**
     * Recursive method that returns the in-order traversal of the tree as a String
     * The order in which it travels to nodes and visits them is LVR (travel left, visit node, travel right)
     * @param 			a - the current node
     * @param 			s - a String of the nodes that have been visited
     * @return 			a String of nodes in the order they were visited
     */
    private String inOrder(TNode a, String s) {
		return "";
    }
    
    /**
     * Prints out the tree in a sideways view
     */
    public void displayTree() {
    	
    }

    /**
     * Private recursive method that prints out the tree sideways
     * @param 			n - the root node of the current tree/subtree
     * @param 			lev - the level of n
     */
    private void displayTree(TNode n, int lev) {
		
    }

    /**
     * Finds and removes the node containing the given data (if it exists)
     * @param 			data - the data to find and remove
     */
    public void remove(int data) {
		
	}

    /**
     * Recursively searches for and removes the given data
     * @param 			parent - the current parent node
     * @param 			data - the element being searched for in the tree
     * @return 			the updated child node after the node containing data has been removed
     */
    private TNode remove(TNode parent, int data) {
		return null;
    }

    /**
     * Find the successor to a node (next largest node in the tree)
     * @param 			a - the node to find the successor of
     * @return 			the successor of node a
     */
    private TNode successor(TNode a) {
		return null;
    }

    /**
     * Returns the maximum value in the tree, or -1 for an empty tree
     * @return 			the max value in the tree (or -1 if empty)
     */
    public int getMax() {
		return -1;
    }

    /**
     * Returns the minimum value in the tree, or -1 for an empty tree
     * @return 			the min value in the tree (or -1 if empty)
     */
    public int getMin() {
		return -1;
    }
}