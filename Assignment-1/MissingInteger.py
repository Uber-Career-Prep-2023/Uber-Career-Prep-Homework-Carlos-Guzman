"""
Given an integer n and a sorted array of integers of size n-1 which contains all but one of the integers in the range 1-n, find the missing integer.

Examples:
Input Array: [1, 2, 3, 4, 6, 7]
Input n: 7
Output: 5

Input Array: [1]
Input n: 2
Output: 2

Input Array: [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12]
Input n: 12
Output: 9

array =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
n = 13

"""


#solution complexity O(n) compelxity  O(1) time 14 min space 


array =  [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12]
n = 12
def missing_integer(array,n):
    if len(array) == 1 and len(array) < n:
        return(array[0]+1)
    for i, num in enumerate(array):
        if i == len(array)-1 and num != n:
            return n
        elif array[i+1] != num+1:
            return num+1
print(missing_integer(array,n)) 
