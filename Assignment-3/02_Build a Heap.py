""" Write a min heap class according to the following API using an array as the underlying data structure. (A max heap has the same implementation; you simply need to flip the direction of the comparators.) For simplicity, you can assume that the heap holds integers rather than generic comparables.
class Heap {
    private:
      array<int> arr; // the underlying array

    public:
      int top(); // returns the min (top) element in the heap
      void insert(int x); // adds int x to the heap in the appropriate position
      void remove(); // removes the min (top) element in the heap
}

IF A NODE IS AT INDEX X  = i
HIS LEFT CHILD IS AT INDEX 2*i + 1
HIS RIGHT CHILD IS AT INDEX 2*i + 2
HIS PARENT IS AT INDEX FLOOR(i-1/2)
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
    
#Test cases
heap = Heap([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])

print(heap.top())  # Output: 1 (minimum element)
heap.insert(0)
print(heap.top())  # Output: 0 (minimum element after insertion)
print(heap.remove())  # Output: 0 (removed element)
print(heap.top())  # Output: 1 (new minimum element)
