"""Question 4: CopyTree
Given a binary tree, create a deep copy. Return the root of the new tree.
"""

# Function to create a deep copy of a binary tree.
def copy_Tree(root):
    # If the root node is None, the tree is empty and the function returns None.
    if root == None:
        return None
    
    # Recursively create deep copies of the left and right subtrees.
    left_child = copy_Tree(root.left)
    right_child = copy_Tree(root.right)
    
    # Create a new node with the copied data and subtrees, and return it as the root of the copied tree.
    return Node(root.data, left_child, right_child)



"""From here on, there is a previous implementation and test cases for the previous function."""
# Class representing a node in a binary tree.
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.right = right
        self.left = left
# Create the nodes of the binary tree.
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)

# Connect the nodes to form a binary tree.
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7

# Create a deep copy of the binary tree.
copied_tree = copy_Tree(node1)
