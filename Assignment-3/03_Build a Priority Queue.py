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
        return self.max_heap[0][1] if self.max_heap else None

    def insert(self, node):
        # Inserts a new node to the heap
        heap = self.max_heap
        heap.append([node.priority, node.str])
        child_idx = len(heap) - 1
        parent_idx = (child_idx - 1) // 2

        # Heapify up: While the child node is greater than the parent node
        while child_idx > 0 and heap[child_idx][0] > heap[parent_idx][0]:
            # Swap child and parent
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
        if left_idx < len(self.max_heap) and self.max_heap[left_idx][0] > self.max_heap[largest][0]:
            largest = left_idx
        # If right child is greater than parent
        if right_idx < len(self.max_heap) and self.max_heap[right_idx][0] > self.max_heap[largest][0]:
            largest = right_idx
        # If a larger child is found, swap it with parent and heapify down
        if largest != idx:
            self.max_heap[largest], self.max_heap[idx] = self.max_heap[idx], self.max_heap[largest]
            self.heapify_down(largest)


class Node:
    def __init__(self, str, priority) -> None:
        # Initialize a node with string and priority
        self.str = str
        self.priority = priority


class Priority_Queue:
    def __init__(self) -> None:
        # Initialize a priority queue
        self.queue = Heap([])

    def insert(self, node):
        # Inserts a node into the queue
        self.queue.insert(node)

    def top(self):
        # Returns the highest priority string element
        return self.queue.top()

    def remove(self):
        # Removes the highest priority string element
        if len(self.queue.max_heap) == 0:
            return None
        self.queue.remove()


# Testing
pq = Priority_Queue()
pq.insert(Node("test1", 3))
pq.insert(Node("test2", 1))
pq.insert(Node("test3", 2))

print(pq.top())  # Should print: test1
pq.remove()
print(pq.top())  # Should print: test3
pq.remove()
print(pq.top())  # Should print: test2
