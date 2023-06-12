""" 
Given an origin and a destination in a directed graph in which edges can be blue or red, determine the length of the shortest path from the origin to the destination in which the edges traversed alternate in color. Return -1 if no such path exists.

this is called a Bipartite graph
"""
from collections import deque

def build_adjacency_list(edges):
    # Create an empty dictionary to hold the adjacency list
    adjacency_list = {}

    # Iterate over all the edges in the input
    for i in range(len(edges)):
        # If the start node of an edge is not already in the adjacency list,
        # add it as a key with an empty list as its value
        if edges[i][0] not in adjacency_list:
            adjacency_list[edges[i][0]] = []
        # Do the same for the end node of the edge
        if edges[i][1] not in adjacency_list:
            adjacency_list[edges[i][1]] = []
        # Add the end node and color of the edge as a tuple to the list of the start node
        adjacency_list[edges[i][0]].append((edges[i][1], edges[i][2]))
    
    # Return the completed adjacency list
    return adjacency_list

def bfs(graph, origin, destination):
    # Create an empty set to hold the nodes we've visited
    visited = set()
    # Create a queue and add the origin node, with None as its previous color and 0 as its path length
    queue = deque()
    queue.append((origin, None, 0))

    # Continue until the queue is empty
    while queue:
        # Take the next node, previous color, and path length from the front of the queue
        crr_node, prev_color, path_len = queue.popleft()

        # Iterate over all the neighbors of the current node in the graph
        for i in graph[crr_node[0]]:
            # If the color of the edge to the neighbor is different from the previous color,
            # and we haven't visited the neighbor before, then we can go to the neighbor
            if prev_color != i[1] and i[0] not in visited:
                # Add the neighbor, its color, and the incremented path length to the queue
                queue.append((i[0], i[1], path_len + 1))
                # If the neighbor is the destination, return the incremented path length
                if i[0] == destination:
                    return path_len + 1
                # Add the neighbor to the set of visited nodes
                visited.add(i[0])
        
    # If we've checked all possible paths and haven't found the destination, return -1
    return -1

def AlternatingPath(graph, origin, destination):
    # If the origin and destination are the same, return 0 because no travel is needed
    if origin == destination:
        return 0
    # Build the adjacency list for the graph
    directed_graph = build_adjacency_list(graph)
    # Run the BFS on the graph and return the result
    return bfs(directed_graph, origin, destination)



# Test case 1: Example with no valid path because all edges have the same color
edges1 = [("A", "B", "blue"), ("B", "C", "blue"), ("C", "D", "blue")]
print(AlternatingPath(edges1, "A", "D"))  # Output: -1

# Test case 2: Example with a single edge, this is a valid path since there's no need to alternate colors
edges2 = [("A", "B", "blue")]
print(AlternatingPath(edges2, "A", "B"))  # Output: 1

# Test case 3: Example with two edges of different colors, this is a valid alternating path
edges3 = [("A", "B", "blue"), ("B", "C", "red")]
print(AlternatingPath(edges3, "A", "C"))  # Output: 2

# Test case 4: Example with three edges, but no valid alternating path
edges4 = [("A", "B", "blue"), ("B", "C", "blue"), ("C", "D", "red")]
print(AlternatingPath(edges4, "A", "D"))  # Output: -1

# Test case 5: Larger graph with a valid alternating path
edges5 = [("A", "B", "red"), ("B", "C", "blue"), ("C", "D", "red"), ("D", "E", "blue")]
print(AlternatingPath(edges5, "A", "E"))  # Output: 4

# Test case: Large graph with multiple valid and invalid alternating paths
edges = [
    ("A", "B", "red"), ("B", "C", "blue"), ("C", "D", "red"), ("D", "E", "blue"), 
    ("E", "F", "red"), ("F", "G", "blue"), ("G", "H", "red"), ("H", "I", "blue"), 
    ("I", "J", "red"), ("J", "K", "blue"), ("K", "L", "red"), ("L", "M", "blue"), 
    ("M", "N", "red"), ("N", "O", "blue"), ("O", "P", "red"), ("P", "Q", "blue"),
    ("Q", "R", "red"), ("R", "S", "blue"), ("S", "T", "red"), ("T", "U", "blue"),
    ("U", "V", "red"), ("V", "W", "blue"), ("W", "X", "red"), ("X", "Y", "blue"),
    ("Y", "Z", "red"), ("A", "Z", "blue"), ("Z", "B", "blue")
]

print(AlternatingPath(edges, "A", "Z"))  # Output: 2 (path: A→Z (blue))
print(AlternatingPath(edges, "A", "M"))  # Output: 13 (path: A→B (red)→C (blue)→D (red)→E (blue)→F (red)→G (blue)→H (red)→I (blue)→J (red)→K (blue)→L (red)→M (blue))
print(AlternatingPath(edges, "A", "R"))  # Output: -1 (no valid path exists)
