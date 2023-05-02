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
    
    def min(self, root):  # Function to find minimum value in BST
        current = root  # Set current node to root
        while current.left is not None:  # Traverse left subtree
            current = current.left  # Move to left child
        return current.value  # Return minimum value
    
    def max(self, root):  # Function to find maximum value in BST
        current = root  # Set current node to root
        while current.right is not None:  # Traverse right subtree
            current = current.right  # Move to right child
        return current.value  # Return maximum value
    
    def contains(self, val):  # Function to check if value is in BST
        current = self.root  # Set current node to root
        while current is not None:  # Traverse tree until value is found or end is reached
            if val < current.value:  # Move to left child if value is less than current node's value
                current = current.left
            elif val > current.value:  # Move to right child if value is greater than current node's value
                current = current.right
            elif val == current.value:  # Value is found if it is equal to current node's value
                return True
        return False  # Value is not found if the end of the tree is reached



    def insert(self, val):  # Function to insert the value in a appropiate location in the BST
        new_node = Node(val)  # Create a new node with the given value
        if self.root is None:  # If the BST is empty, set the new node as the root
            self.root = new_node
            return new_node

        current = self.root  # Start at the root of the tree
        parent = None

        while current is not None:  # Traverse the tree to find the appropriate location for the new node
            parent = current
            if val < current.value:
                current = current.left
            else:
                current = current.right

        if val < parent.value:  # Insert the new node as the left child of the parent if the value is less than the parent's value
            parent.left = new_node
        else:  # Insert the new node as the right child of the parent if the value is greater than or equal to the parent's value
            parent.right = new_node

        return new_node  # Return the new node that was inserted


    def delete(self,val):   # Define a function that deletes the node with the given value from the BST, if it exists
        current = self.root  # Set the current node to the root of the tree
        parent = None
        while current is not None:  # Traverse the tree to find the node to delete
            if val < current.value:  # If the value is less than the current node's value, move to the left child
                parent = current
                current = current.left
            elif val > current.value:  # If the value is greater than the current node's value, move to the right child
                parent = current
                current = current.right
            else:  # If the value is equal to the current node's value, the node to delete is found
                break
        else:  # If the value is not found, return None
            return None
        
        # Case 1: Node has no children
        if current.left == None and current.right == None:  # If the node has no children, simply remove it from the tree
            if parent.left == current:
                parent.left = None
            else:
                parent.right = None
        
        # Case 2: Node has one child
        elif current.left or current.right:  # If the node has one child, replace it with its child
            if current.left:  # If the node has a left child, replace it with the left child
                if parent.left == current:
                    parent.left = current.left
                else:
                    parent.right = current.left 
            else:  # If the node has a right child, replace it with the right child
                if parent.left == current:
                    parent.left = current.right
                else:
                    parent.right = current.right
        
        # Case 3: Node has two children
        else:  # If the node has two children, replace it with its successor
            pass  # This case has not been implemented

        return current  # Return the node that was deleted




# Create a new binary search tree and add some values
tree = BinaryTree()
tree.insert(8)
tree.insert(3)
tree.insert(1)
tree.insert(6)
tree.insert(10)
tree.insert(14)

# Create a new binary search tree and add some values
tree = BinaryTree()
tree.insert(8)
tree.insert(3)
tree.insert(1)
tree.insert(6)
tree.insert(10)
tree.insert(14)

# Test the min() function
print(tree.min(tree.root))   # The minimum value in the tree should be 1

# Test the max() function
print(tree.max(tree.root))  # The maximum value in the tree should be 14

# Test the contains() function
print(tree.contains(6)) # The value 6 should be present in the tree
print(tree.contains(12)) # The value 12 should not be present in the tree

# Test the delete() function
tree.delete(6)   # Delete the node with value 6
print(tree.contains(6) == False) # The value 6 should no longer be present in the tree
print(tree.contains(3) == True)  # The value 3 should still be present in the tree

