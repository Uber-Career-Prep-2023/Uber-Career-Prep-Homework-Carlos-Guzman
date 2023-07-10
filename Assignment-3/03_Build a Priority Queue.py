"""A priority queue functions like a queue except that elements are removed in order of priority rather than insertion. This is typically implemented as a max heap that stores pairs of elements and numeric weights, with the weights used as the values in the heap. Implement a priority queue according to the following API using a heap as the underlying data structure. For simplicity, you can assume the priority queue stores string elements with integer priorities. Start by copy-pasting your heap implementation from question 2 and making modifications.

class PriorityQueue {
    private:
      array<pair<string, int>> arr; // the underlying array

    public:
      int top(); // returns the highest priority (first) element in the PQ
      void insert(string x, int weight); // adds string x to the PQ with priority weight
      void remove(); // removes the highest priority (first) element in the PQ
}

"""

class Heap:
    def __init__(self, heap) -> None:
        # Initialize a max heap
        self.max_heap = heap

    def top(self):
        # Returns the highest priority string element
        return self.max_heap[0][2] if self.max_heap else None

    def insert(self, node):
        # Inserts a new node to the heap
        heap = self.max_heap
        heap.append([node.priority, node.order, node.str])
        child_idx = len(heap) - 1
        parent_idx = (child_idx - 1) // 2

        # Heapify up: While the child node is greater than the parent node
        while child_idx > 0 and (heap[child_idx][0] > heap[parent_idx][0] or (heap[child_idx][0] == heap[parent_idx][0] and heap[child_idx][1] < heap[parent_idx][1])):
            # Swap the child node with the parent node
            heap[child_idx], heap[parent_idx] = heap[parent_idx], heap[child_idx]
            # Move up one level
            child_idx = parent_idx
            parent_idx = (child_idx - 1) // 2

    def remove(self):
        # Removes the highest priority string element
        heap = self.max_heap
        if len(heap) == 0:
            return None
        val = heap[0]
        heap[0] = heap[-1]  # Move the last element to the top
        heap.pop()  # Remove the last element
        self.heapify_down(0)  # Heapify down from the root
        return val

    def heapify_down(self, idx):
        # Heapify down: While the parent node is less than the child node
        left_idx = 2 * idx + 1
        right_idx = 2 * idx + 2
        largest = idx
        
        # If left child is greater than parent
        if left_idx < len(self.max_heap) and (self.max_heap[left_idx][0] > self.max_heap[largest][0] or (self.max_heap[left_idx][0] == self.max_heap[largest][0] and self.max_heap[left_idx][1] < self.max_heap[largest][1])):
            largest = left_idx
        # If right child is greater than parent
        if right_idx < len(self.max_heap) and (self.max_heap[right_idx][0] > self.max_heap[largest][0] or (self.max_heap[right_idx][0] == self.max_heap[largest][0] and self.max_heap[right_idx][1] < self.max_heap[largest][1])):
            largest = right_idx
        # If a larger child is found, swap it with parent and heapify down
        if largest != idx:
            self.max_heap[largest], self.max_heap[idx] = self.max_heap[idx], self.max_heap[largest]
            self.heapify_down(largest)


class Node:
    def __init__(self, str, priority, order) -> None:
        # Initialize a node with string and priority
        self.str = str
        self.priority = priority
        self.order = order

class Priority_Queue:
    def __init__(self) -> None:
        # Initialize a priority queue
        self.queue = Heap([])
        self.insertion_order = 0
    def insert(self, str, priority):
        # Inserts a node into the queue
        self.insertion_order += 1
        self.queue.insert(Node(str, priority, self.insertion_order))
    def top(self):
        # Returns the highest priority string element
        return self.queue.top()

    def remove(self):
        # Removes the highest priority string element
        if len(self.queue.max_heap) == 0:
            return None
        return self.queue.remove()

# # Testing
# pq = Priority_Queue()

# # Inserting elements with different priorities
# pq.insert("Element 1", 3)
# pq.insert("Element 2", 1)
# pq.insert("Element 3", 5)
# pq.insert("Element 4", 7)
# pq.insert("Element 5", 6)

# # Expect: Element 4
# print(pq.top())  
# pq.remove()

# # Expect: Element 5
# print(pq.top())
# pq.remove()

# # Expect: Element 3
# print(pq.top())
# pq.remove()

# # Expect: Element 1
# print(pq.top())
# pq.remove()

# # Expect: Element 2
# print(pq.top())

# # Inserting elements with the same priorities
# pq.insert("Element 6", 4)
# pq.insert("Element 7", 4)
# pq.insert("Element 8", 4)
# pq.insert("Element 9", 4)

# # Removal should respect the insertion order for the elements with equal priorities

# # Expect: Element 6
# print(pq.top())  
# pq.remove()

# # Expect: Element 7
# print(pq.top())
# pq.remove()

# # Expect: Element 8
# print(pq.top())
# pq.remove()

# # Expect: Element 9
# print(pq.top())
# pq.remove()

# Test Case
pq = Priority_Queue()

pq.insert("Node A", 3)
pq.insert("Node B", 2)
pq.insert("Node C", 2)
pq.insert("Node D", 1)
pq.insert("Node E", 2)
pq.insert("Node F", 2)

# Expect: Node A (highest priority 3)
print(pq.top())  
pq.remove()

# Expect: Node B (second highest priority 2, first with this priority)
print(pq.top())  
pq.remove()

# Expect: Node C (second highest priority 2, second with this priority)
print(pq.top())  
pq.remove()

# Expect: Node E (second highest priority 2, third with this priority, inserted before Node F)
print(pq.top())
pq.remove()

# Expect: Node F (second highest priority 2, fourth with this priority)
print(pq.top())
pq.remove()

# Expect: Node D (lowest priority 1)
print(pq.top())
pq.remove()
