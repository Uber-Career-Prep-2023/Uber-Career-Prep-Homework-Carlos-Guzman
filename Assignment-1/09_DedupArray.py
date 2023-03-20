"""
Given a sorted array of non-negative integers, modify the array by removing duplicates so each element only appears once. If arrays are static (aka, not dynamic/resizable) in your language of choice, the remaining elements should appear in the left-hand side of the array and the extra space in the right-hand side should be padded with -1s.

Examples:
Input Array: [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
Modified Array: [1, 2, 3, 4] 
or [1, 2, 3, 4, -1, -1, -1, -1, -1, -1] (depending on language)

Input Array: [0, 0, 1, 4, 5, 5, 5, 8, 9, 9, 10, 11, 15, 15]
Modified Array: [0, 1, 4, 5, 8, 9, 10, 11, 15]
or [1, 4, 5, 8, 9, 10, 11, 15, -1, -1, -1, -1, -1] (depending on language)

Input Array: [1, 3, 4, 8, 10, 12]
Modified Array: [1, 3, 4, 8, 10, 12]


"""

# easy with a set it will resolve in O(n) time 1 min
"""
array = [1, 3, 4, 8, 10, 12]

my_set = set(array)
result = list(my_set)
print(result)
"""

# another solution O(n), uses a set data structure to remove duplicates, The space complexity is O(n), time 1 min
# array = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
# def DedupArray(array):
#     my_set = set()
#     for i in array:
#         my_set.add(i)
#     result = list(my_set)
#     return result
# print(DedupArray(array))


array = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

# Check if array is empty
if len(array) == 0:
    print(array)

# Two pointers i and j
j = 0

# Iterate over the array with i starting at 1
for i in range(1, len(array)):
    # If the element at i is different from the element at j,
    # increment j and replace the element at j with the element at i
    if array[i] != array[j]:
        j += 1
        array[j] = array[i]

# Fill the remaining positions in the array with -1
while j < len(array) - 1:
    j += 1
    array[j] = -1

# Print the modified array
print(array[:j+1])