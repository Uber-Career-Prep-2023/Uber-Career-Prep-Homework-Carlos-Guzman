"""
Given an array of integers and a target integer, k, return the number of pairs of integers in the array that sum to k. In each pair, the two items must be distinct elements (come from different indices in the array).

Examples:

Input Array: [1, 10, 8, 3, 2, 5, 7, 2, -2, -1]
Input k: 10
Output: 3
(Pairs: (8, 2), (8, 2), (3, 7))

Input Array: [1, 10, 8, 3, 2, 5, 7, 2, -2, -1]
Input k: 8
Output: 3
(Pairs: (10, -2), (3, 5), (1, 7))

Input Array: [4, 3, 3, 5, 7, 0, 2, 3, 8, 6]
Input k: 6
Output: 5
(Pairs: (4, 2), (0, 6), (3, 3), (3, 3), (3, 3))

Input Array: [4, 3, 3, 5, 7, 0, 2, 3, 8, 6]
Input k: 1
output: 0
"""


#naive aproach

# array = [4, 3, 3, 5, 7, 0, 2, 3, 8, 6]
# k = 1

# count = 0

# for i in range(len(array)):
#     for j in range(i+1,len(array)):
#         if array[i]+array[j] == k and i != j:
#             count += 1
# print(count)

#The solution technique used in the algorithm is Hash Table
#time complexity of the algorithm is O(n), space complexity O(n),  time 33 min
array = [4, 3, 3, 5, 7, 0, 2, 3, 8, 6]
k = 1

def two_sum(array,k):
    
    my_dict = {}
    count = 0
    for i in array:
        if i in my_dict:
            my_dict[i] += 1   
        else:
            my_dict[i] = 1
    for i in array:
        if k-i in my_dict:
            count += 1
        if i in my_dict:
            my_dict[i] -= 1 
            if my_dict[i] == 0:
                del my_dict[i]
    return(count) 
 
print(two_sum(array,k))