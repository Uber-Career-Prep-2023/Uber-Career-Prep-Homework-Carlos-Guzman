"""Given a binary matrix in which 1s represent land and 0s represent water. Return the number of islands (contiguous 1s surrounded by 0s or the edge of the matrix).
"""

def num_islands(matrix):
    islands = 0  # Initialize the island count to zero

    # Iterate over each cell in the matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            # If a land cell (1) is found, increment the island count and sink the connected land
            if matrix[i][j] == 1:
                islands += 1
                dfs(matrix, i, j)

    return islands  # Return the total number of islands


def dfs(matrix, i, j):
    # If the cell is out of bounds or is water (0), return
    if i >= len(matrix) or j >= len(matrix[0]) or i < 0 or j < 0 or matrix[i][j] == 0:
        return

    # Sink the current land cell
    matrix[i][j] = 0

    # Perform depth-first search in the four cardinal directions
    dfs(matrix, i + 1, j)  # Down
    dfs(matrix, i - 1, j)  # Up
    dfs(matrix, i, j + 1)  # Right
    dfs(matrix, i, j - 1)  # Left


# Test Cases
matrix1 = [[1, 1, 0, 0, 0],
           [1, 1, 0, 0, 0],
           [0, 0, 1, 0, 0],
           [0, 0, 0, 1, 1]]
print(num_islands(matrix1))  # Expected output: 3

matrix2 = [[1, 1, 1, 1, 0],
           [1, 1, 0, 1, 0],
           [1, 1, 0, 0, 0],
           [0, 0, 0, 0, 0]]
print(num_islands(matrix2))  # Expected output: 1

matrix3 = [[1, 1, 0, 0, 0],
           [1, 1, 0, 0, 0],
           [0, 0, 0, 1, 1],
           [0, 0, 0, 1, 1]]
print(num_islands(matrix3))  # Expected output: 2
