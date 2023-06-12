"""Given an array of pairs of values representing edges in an unweighted graph, create the equivalent adjacency list/set representation (a map from element to a list or set of elements). Pairs represent directed edges: (A, B) means there is an edge from A to B. If the pair (B, A) is also provided then there is an undirected edge between A and B. For simplicity, you may assume that each node of the graph stores an integer rather than a generic data type and that the elements are distinct. Implement a basic DFS and BFS searching for a target value and a topological sort (using either DFS or Kahn’s algorithm).
"""

def build_adjacency_list(edges):
    # Initialize an empty dictionary to hold the adjacency list
    adjacency_list = {}

    # Loop through each edge in the input list
    for i in range(len(edges)):
        # If the origin node of the edge is not already in the adjacency list, add it with an empty list as its value
        if edges[i][0] not in adjacency_list:
            adjacency_list[edges[i][0]] = []
        # If the destination node of the edge is not already in the adjacency list, add it with an empty list as its value
        if edges[i][1] not in adjacency_list:
            adjacency_list[edges[i][1]] = []
        # Add the destination node to the list of adjacent nodes for the origin node
        adjacency_list[edges[i][0]].append(edges[i][1])
    
    # Return the completed adjacency list
    return adjacency_list

def dfs(adjacency_list, target):
    # Choose the first node in adjacency list as starting point
    start_node = list(adjacency_list.keys())[0]
    
    # If the start node is the target, return True immediately
    if start_node == target:
        return True

    # Create a set to keep track of visited nodes
    visited = set([start_node])

    # Create a stack for DFS, initialize with start node
    stack = [start_node]

    # Keep looping until there's elements in the stack
    while stack:
        # Pop the top node from stack
        current = stack.pop()

        # Traverse all the neighbours of current node
        for i in adjacency_list[current]:
            # If the neighbour node is the target, return True
            if i == target:
                return True

            # If the neighbour node hasn't been visited yet, mark it as visited and add to the stack
            if i not in visited:
                visited.add(i)
                stack.append(i)

    # If we've gone through all nodes and haven't found the target, return False
    return False



def bfs(adjacency_list, target):
    # Choose the first node in adjacency list as starting point
    start_node = list(adjacency_list.keys())[0]
    
    # If the start node is the target, return True immediately
    if start_node == target:
        return True

    # Initialize a queue with start node for BFS
    queue = [start_node]

    # Create a set to keep track of visited nodes
    visited = set([start_node])

    # Keep looping until there's elements in the queue
    while queue:
        # Dequeue the front node from queue
        current = queue.pop(0)

        # Traverse all the neighbours of current node
        for i in adjacency_list[current]:
            # If the neighbour node is the target, return True
            if i == target:
                return True

            # If the neighbour node hasn't been visited yet, mark it as visited and enqueue it
            if i not in visited:
                visited.add(i)
                queue.append(i)

    # If we've gone through all nodes and haven't found the target, return False
    return False     

# Recursive function to perform DFS on a node and its neighbors
def dfs_visit(adjacency_list, visited, sorted_list, node):
    # Iterate over all neighbors of the current node
    for neighbor in adjacency_list[node]:
        # If this neighbor hasn't been visited yet
        if neighbor not in visited:
            # Mark the neighbor as visited
            visited.add(neighbor)
            # Recursively perform DFS on the neighbor
            dfs_visit(adjacency_list, visited, sorted_list, neighbor)
    # After visiting the current node and its neighbors, insert the current node at the start of the sorted list
    sorted_list.insert(0, node)

# Function to perform a topological sort on a graph
def topological_sort(adjacency_list):
    # Initialize an empty set to keep track of visited nodes
    visited = set()
    # Initialize an empty list to store the topological sort
    sorted_list = []
    # Iterate over all nodes in the adjacency list
    """ Iterate over all nodes in the adjacency list
        We do this to ensure that all nodes are visited, even if the graph is not connected.
        In other words, this helps us handle the scenario where there are nodes in the graph
        that are not reachable from the initial starting node.
        Without this iteration, our topological sort would not include these unreachable nodes,
        resulting in an incorrect output. """ 
    for i in adjacency_list:
        # If this node hasn't been visited yet
        if i not in visited:
            # Mark the node as visited
            visited.add(i)
            # Perform DFS on the node
            dfs_visit(adjacency_list, visited, sorted_list, i)
    # Return the topologically sorted list of nodes
    return sorted_list



# Test Cases
print(build_adjacency_list([(1, 2), (2, 3), (1, 3), (3, 2), (2, 0)])) 
# Expected Output: {1: [2, 3], 2: [3, 0], 3: [2], 0: []}

print(build_adjacency_list([(0, 1), (1, 2), (2, 3), (3, 4)]))
# Expected Output: {0: [1], 1: [2], 2: [3], 3: [4], 4: []}

print(build_adjacency_list([(1, 3), (2, 3), (3, 4), (4, 1), (4, 2)])) 
# Expected Output: {1: [3], 3: [4], 2: [3], 4: [1, 2]}

edges = [(1, 2), (2, 3), (1, 3), (3, 2), (2, 0)]
adjacency_list = build_adjacency_list(edges)
print(dfs(adjacency_list, 3))  # Expected: True
print(dfs(adjacency_list, 4))  # Expected: False

print(bfs(adjacency_list, 3))  # Expected: True
print(bfs(adjacency_list, 4))  # Expected: False


# Single-node components
graph1 = {1: [], 2: [], 3: []}
print(topological_sort(graph1))  # Expected output: [1, 2, 3] or any permutation of [1, 2, 3]

# Single linear chain
graph2 = {
    1: [2],
    2: [3],
    3: []
}
print(topological_sort(graph2))  # Expected output: [1, 2, 3]

# Two separate chains
graph3 = {
    1: [2],
    2: [],
    3: [4],
    4: []
}
print(topological_sort(graph3))  # Expected output: [3, 4, 1, 2] or [1, 2, 3, 4]

# More complex graph with a common dependency
graph4 = {
    1: [2, 3],
    2: [4],
    3: [4],
    4: []
}
print(topological_sort(graph4))  # Expected output: [1, 3, 2, 4] or [1, 2, 3, 4] or any other valid topological sort


