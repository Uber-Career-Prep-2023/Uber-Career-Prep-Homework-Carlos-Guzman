"""Given a binary tree, determine if it is a binary search tree
"""
def is_BST(root, lower=float('-inf'), upper=float('inf')):
    # If the current node is None, it means we reached the end of a branch
    if root == None:
        return True

    # Check if the current node's value is within the lower and upper bounds
    if lower < root.value < upper:
        # If the current node's value is within bounds, continue checking
        # its left child with an updated upper bound, and its right child
        # with an updated lower bound
        return is_BST(root.left, lower, root.value) and is_BST(root.right, root.value, upper)
    else:
        # If the current node's value is not within bounds, it is not a BST
        return False

# Test cases
# Define a simple binary tree node class for testing purposes
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Test Case 1: A valid BST
root1 = TreeNode(10)
root1.left = TreeNode(5)
root1.right = TreeNode(15)
root1.left.left = TreeNode(3)
root1.left.right = TreeNode(7)
root1.right.left = TreeNode(12)
root1.right.right = TreeNode(18)

print(is_BST(root1))  # Should print True

# Test Case 2: An invalid BST
root2 = TreeNode(10)
root2.left = TreeNode(5)
root2.right = TreeNode(15)
root2.left.left = TreeNode(3)
root2.left.right = TreeNode(12)  # Invalid position (violates BST property)
root2.right.left = TreeNode(11)
root2.right.right = TreeNode(18)

print(is_BST(root2))  # Should print False
