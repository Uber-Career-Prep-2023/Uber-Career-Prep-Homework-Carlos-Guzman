"""class BinarySearchTree {
    int min() // returns the minimum value in the BST
    int max() // returns the maximum value in the BST
    bool contains(int val) // returns a boolean indicating whether val is present in the BST
    // For simplicity, do not allow duplicates. If val is already present, insert is a no-op
    void insert(int val) // creates a new Node with data val in the appropriate location
    int delete(int val) // deletes the Node with data val, if it exists
}
"""

class Node:
    def __init__(self, data, left=None, right=None):
        self.value = data
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def min(self, root):  # returns the minimum value in the BST
        current = root
        while current.left is not None:
            current = current.left
        return current.value
    def max(self, root):  # returns the maximum value in the BST
        current = root
        while current.right is not None:
            current = current.right
        return current.value
    def contains(self, val):   # returns a boolean indicating whether val is present in the BST
        current = self.root
        while current is not None:
            if val < current.value:
                current = current.left
            elif val > current.value:
                current = current.right
            elif val == current.value:
                return True
        return False

    def insert(self, val):  # creates a new Node with data val in the appropriate location
        new_node = Node(val)
        if self.root is None:
            self.root = new_node
            return new_node

        current = self.root
        parent = None

        while current is not None:
            parent = current
            if val < current.value:
                current = current.left
            else:
                current = current.right

        if val < parent.value:
            parent.left = new_node
        else:
            parent.right = new_node

        return new_node

    def delete(self,val)   #deletes the Node with data val, if it exists
        current = self.root
        parent = None
        if val == current.value:
            del current
            return None
        while current.value != val or current == None:
            parent = current
            if val < current.value:
                current = current.left
            elif val > current.value:
                current = current.right

        return None