"""Given an array of k sorted arrays, merge the k arrays into a single sorted array."""
"""
Time: O(N log K) (Inserting N elements into a min-heap, where K is the number of sorted arrays)
Space: O(N + K) (Storing the merged and sorted array and the min-heap)
Technique: Heap-based Merge
Time: ~40 minutes.
"""

import math

class Heap:
    def __init__(self, heap=None):
        self.min_heap = heap if heap is not None else []  # Initialize the min-heap with the given heap array
    
    def top(self):
        # Return the minimum element of the min-heap (element at index 0)
        return self.min_heap[0] if self.min_heap else None
    
    def insert(self, value):
        heap = self.min_heap
        heap.append(value)  # Add the value to the end of the heap
        parent = math.floor(((len(heap) - 1) / 2))  # Calculate the index of the parent of the newly added value
        position_val = len(heap) - 1  # Position of the newly added value

        while heap[position_val] < heap[parent]:
            # Swap the value with its parent if it is smaller
            heap[position_val], heap[parent] = heap[parent], heap[position_val]
            position_val = parent
            parent = math.floor(((position_val - 1) / 2))  # Calculate the index of the new parent
        return position_val
    
    def remove(self):
        heap = self.min_heap
        if len(heap) == 0:
            return None
        val = heap[0]  # Store the minimum value (root of the heap)
        heap[0] = heap[len(heap) - 1]  # Replace the root with the last element
        heap.pop()  # Remove the last element
        crr_position = 0

        while True:
            left_child = math.floor((2 * crr_position) + 1)  # Index of the left child
            right_child = math.floor((2 * crr_position) + 2)  # Index of the right child
            min_index = crr_position

            if left_child < len(heap) and heap[min_index] > heap[left_child]:
                # If the left child is smaller, update the minimum index
                min_index = left_child
            if right_child < len(heap) and heap[min_index] > heap[right_child]:
                # If the right child is smaller, update the minimum index
                min_index = right_child
            heap[crr_position], heap[min_index] = heap[min_index], heap[crr_position]
            if crr_position == min_index:
                break
            crr_position = min_index
        return val

def MergeKSortedArrays(arrays):
    sorted_arr = []  # Initialize an empty array to store the merged and sorted elements
    heap = Heap()  # Create an instance of the Heap class

    # Iterate over each array in the input arrays
    for i in arrays:
        # Iterate over each element in the current array
        for j in i:
            heap.insert(j)  # Insert the element into the heap

    # Extract the smallest element from the heap until it becomes empty
    while heap:
        sorted_arr.append(heap.remove())  # Remove the smallest element and append it to the sorted array

    return sorted_arr  # Return the merged and sorted array


# Test Case 1
arrays1 = [[1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [11, 13, 15, 17, 19]]
result1 = MergeKSortedArrays(arrays1)
print(result1)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15, 17, 19]

# Test Case 2
arrays2 = [[5, 10, 15], [2, 4, 6, 8], [1, 3, 7, 9, 12]]
result2 = MergeKSortedArrays(arrays2)
print(result2)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15]

# Test Case 3
arrays3 = [[100, 200, 300], [50, 150, 250, 350, 450], [75, 125, 175, 225]]
result3 = MergeKSortedArrays(arrays3)
print(result3)  # Output: [50, 75, 100, 125, 150, 175, 200, 225, 250, 300, 350, 450]
