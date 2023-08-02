"""A staircase on a hiking trail implements a rather unusual toll system to cover trail maintenance costs. Each stair in the staircase has a different toll which you only have to pay if you step on that stair. Due to the height of the stairs, you can only climb one or two stairs at once. This means that from the ground you must initially step on either stair 0 or stair 1 and that, if there are n stairs, the last stair you step on can be either stair n-1 or n-2. Given an array representing the costs per stair, what is the minimum possible toll you can pay to climb the staircase?

Examples:
Input: [4, 1, 6, 3, 5, 8]
Output: 9 (step on stairs 1, 3, 4 for a cost of 1+3+5)
"""


"""
My solution for the toll problem solves the minimum cost stair climbing problem: 

Initially, I used a greedy approach where I iterated over the array and at each step, I added the lesser cost to the total cost. However, this approach does not always provide the correct answer.

The correct way to solve this problem is by using dynamic programming. The steps are as follows:

1) Declare a memoization array of the same size as the original array and initialize it with -1.

2) Declare the size of the array as 'n' to know the maximum step we can reach.

3) Make a recursive call to another function with the values of the first step (which will be 0), the size of the cost array, the cost array itself, and the memoization array. Note: The memoization array will only be filled during backtracking and will store the least cost found to reach the current step.

4) Inside the recursion, first, verify that we have not reached the end of the cost array, i.e., the current step is not out of range.

5) If we haven't reached the end of the steps, check if we already have the least possible cost to reach the current step in the memoization array. This implies that we have already performed backtracking and know the least cost to avoid repeating calculations. If we have reached the end of the steps, return 0. If we have reached a step where we already know the least cost, return the value of that step.

6) If we have not set the least possible value for the current step, find the least possible cost from the current step. This means making two different recursive searches. One to check if taking a single step leads to the lowest cost, and the other to check the least possible cost when taking two steps. This is repeated recursively starting from step 3) until we reach the end of the steps or have set a lower cost for a step.

7) After calculating the cost of taking 1 or 2 steps from the current step, compare which cost is lower. We set the lower value between the two in the memo array at the current position, i.e., the value of memo at this step is the lower cost between taking one or two steps.

8) Return the memo value at this position or step so that in subsequent backtracking steps, we can keep track of the cost we have been accumulating to reach the higher steps.

9) If there are still steps to check, continue recursion from step 3). If not, we know the least cost from all the steps and should return the value of memo at position 0 (memo[0]), which is the first step and the minimum cost we can obtain if we take the most optimal path with the least cost.
"""


# Recursive function to calculate minimum cost of climbing stairs from stair 'i' to 'n'
def minCostStairClimbingRec(i, n, cost, memo):
    # If the current stair is out of range (i.e., we've reached the ground level from top), return 0
    if i >= n:
        return 0

    # If the minimum cost for the current stair is already calculated (i.e., memo[i] is not -1), return it
    if memo[i] != -1:
        return memo[i]
    
    # Otherwise, calculate the cost of climbing from the current stair with one step and two steps
    else:
        oneStep = cost[i] + minCostStairClimbingRec(i+1, n, cost, memo)
        twoStep = cost[i] + minCostStairClimbingRec(i+2, n, cost, memo)

        # Store the minimum of oneStep and twoStep in the memoization array for the current stair
        memo[i] = min(oneStep, twoStep)
        
        # Return the minimum cost of climbing stairs from stair 'i' to 'n'
        return memo[i]

def minCostStairClimbing(cost):
    # Initialize memoization array with -1
    memo = [-1] * len(cost)

    # Length of the cost array
    n = len(cost)

    # Calculate the minimum cost of climbing stairs from the ground level to the top
    return min(minCostStairClimbingRec(0, n, cost, memo), minCostStairClimbingRec(1, n, cost, memo))




# Test cases
print(minCostStairClimbing([4, 1, 6, 3, 5, 8]))  # Output: 9
print(minCostStairClimbing([1, 1, 1, 1, 1, 1]))  # Output: 3
print(minCostStairClimbing([4, 1, 6, 3, 5, 8, 1, 1, 1, 1, 1, 1]))  # Output: 12
print(minCostStairClimbing([4, 1, 6, 3, 5, 8, 1, 1, 1, 1, 1, 1, 1]))  # Output: 13
print(minCostStairClimbing([4, 1, 6, 3, 5, 8, 1, 1, 1, 1, 1, 1, 1, 1]))  # Output: 13
print(minCostStairClimbing([4, 1, 6, 3, 5, 8, 1, 1, 1, 1, 1, 1, 1, 1, 1]))  # Output: 14