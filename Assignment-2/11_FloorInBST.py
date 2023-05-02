"""Given a target numeric value and a binary search tree, return the floor (greatest element less than or equal to the target) in the BST.
"""
def FloorInBST(target, root):
    # Initialize the current node to the root of the BST
    current = root
    
    # Initialize the floor value to None
    floor_value = None

    # Continue traversing the BST until reaching a None node
    while current is not None:
        # If the current node's value equals the target, we found the floor
        if current.value == target:
            return current.value
        
        # If the current node's value is less than the target, update the floor value and move to the right subtree
        if current.value < target:
            floor_value = current.value
            current = current.right
        
        # If the current node's value is greater than the target, move to the left subtree
        else:
            current = current.left
    
    # Return the floor value found (or None if no floor value was found)
    return floor_value

    
"""From here on, there is a previous implementation of a binary tree and test cases for the previous function."""


class Node:
    def __init__(self, data, left=None, right=None):
        self.value = data
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None

# Create the binary tree
bst = BinaryTree()
bst.root = Node(10)
bst.root.left = Node(5)
bst.root.right = Node(15)
bst.root.left.left = Node(3)
bst.root.left.right = Node(7)
bst.root.right.left = Node(12)
bst.root.right.right = Node(17)

# test cases
print(FloorInBST(11, bst.root))  # Output: 10
print(FloorInBST(7, bst.root))   # Output: 7
print(FloorInBST(2, bst.root))   # Output: None
print(FloorInBST(13, bst.root))  # Output: 12
print(FloorInBST(20, bst.root))  # Output: 17
