"""Given a square matrix of 0s and 1s, find the dimension of the largest square consisting only of 1s.

Examples: (squares corresponding to output are highlighted for readability)
Input:
0   1   0   1
0   0   1   1
0   1   1   1
0   0   1   1

Output: 2
Input:
0   1   0   1   1
0   0   1   1   1
1   1   1   1   1
1   1   1   1   1
0   1   1   0   0

Output: 3"""




""" Uses dynamic programming

1) Create a matrix of the same size as the given matrix, but only fill in the spots in the first column and the first row with 
the same values as the original matrix; leave the rest as unknown or null values.
2) Start traversing the original matrix from the second value in the column and the second value in the row at a[1][1].
3) Declare a variable that will track the maximum size we have found in the matrix up to that point, initializing it to 0.
4) In each cell of the matrix, check if it is a 0 or a 1.
5) If it's a zero, mark the cell of the copy of the matrix in the same position where you are standing in the original matrix as 0.
6) If it's a 1, check only 3 cells of the copied matrix: the one above, upper-left, and the left.
7) From those 3 values, take the smallest value and assign it to the current cell where you are standing in the copied matrix plus 1.
8) Compare the value of the maximum square we have found so far with the one we have formed in the current position of the copied matrix,
and assign the largest value to the tracking variable.
9) Continue iterating through the entire matrix, going through all the values, repeating all the steps from step 4.
10) Return the value of the tracking variable.
"""


def LargestSquareOf1s(matrix):
    n = len(matrix)   # Number of rows
    m = len(matrix[0]) # Number of columns

    # Initialize a dp  matrix with the same dimensions
    dp = [[0]*m for _ in range(n)]

    # Copy the first row and column from the original matrix to the dp matrix
    for i in range(n):
        dp[i][0] = matrix[i][0]
    for j in range(m):
        dp[i][0] = matrix[0][j]

    max_length = 0  # To keep track of the maximum length of square of 1s

    # Iterate through the original matrix starting from the second row and second column
    for i in range(1, n):
        for j in range(1, m):
            if matrix[i][j] == 0:
                dp[i][j] = 0
            else:
                # If the cell contains 1, take the minimum of the upper, upper-left, and left cells in dp and add 1
                dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
                # Update max_length if the current cell value in dp is greater
                max_length = max(max_length, dp[i][j])

    return max_length  # Return the maximum length of square of 1s

matrix1 = [
    [0, 1, 0, 1],
    [0, 0, 1, 1],
    [0, 1, 1, 1],
    [0, 0, 1, 1]
]
print(LargestSquareOf1s(matrix1)) # Output: 2

matrix2 = [
    [0, 1, 0, 1, 1],
    [0, 0, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [0, 1, 1, 0, 0]
]
print(LargestSquareOf1s(matrix2)) # Output: 3