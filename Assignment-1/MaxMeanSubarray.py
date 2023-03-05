"""
Given an array of integers and an integer, k, find the maximum mean of a subarray of size k,
 
array = [4, 5, -3, 2, 6, 1]
k = 2
output =  4.5

array =  [4, 5, -3, 2, 6, 1]
k = 3
output = 3

Input Array: [1, 1, 1, 1, -1, -1, 2, -1, -1, 6]
Input k = 3
Output: 1


Input Array: [1, 1, 1, 1, -1, -1, 2, -1, -1, 6]
Input k = 4
output: 1.5
"""

#array = [1, 1, 1, 1, -1, -1, 2, -1, -1, 6]
#k = 4
# naive aproach
# 
#     aux=0
#     max=0
#     for i in range(len(array)-k+1):   #n
#         aux = sum(array[i:i+k])/k #n
#         if aux > max:
#             max = aux
#     print(max)
#     return max
# 


# solution using Sliding Windows, time complexity  O(n), space complexity of the algorithm is O(1), time 37 min
array = [1, 1, 1, 1, -1, -1, 2, -1, -1, 6] 
k = 5

def MaxMeanSubarray(array,k):
    suma = 0
    maxsum = 0
    suma = sum(array[:k])
    maxsum = suma
    for i in range(len(array)-k):
        suma = suma - array[i] + array[i+k]
        if suma > maxsum:
            maxsum = suma
    return(maxsum/k)
print(MaxMeanSubarray(array,k))
