"""Given a binary tree, create an array of the left view (leftmost elements in each level) of the tree."""

def LeftView(root):
    # Initialize an empty list to store the left view nodes' values
    result = []
    
    # Initialize the queue with the root node
    queue = [root]

    # Continue processing nodes as long as there are nodes in the queue
    while queue:
        # Get the number of nodes in the current level
        level_size = len(queue)

        # Iterate over the nodes in the current level
        for i in range(level_size):
            # Remove and get the first node in the queue
            current = queue.pop(0)

            # If it's the first node in the level, add its value to the result
            if i == 0:
                result.append(current.value)

            # Add the left child to the queue if it exists
            if current.left:
                queue.append(current.left)

            # Add the right child to the queue if it exists
            if current.right:
                queue.append(current.right)

    # Return the list containing the left view of the binary tree
    return result



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
tree = BinaryTree()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

# Call the LeftView function with the root of the binary tree
left_view = LeftView(tree.root)

# Print the left view of the binary tree
print(left_view)  # Output: [1, 2, 4]
