"""Given a list of courses that a student needs to take to complete their major and a map of courses to their prerequisites, return a valid order for them to take their courses assuming they only take one course for their major at once
"""
"""This problem is solved using a topological sort."""
"""
Time: O(V + E) (building the adjacency list and performing the topological sort)
Space: O(V + E) (storing the adjacency list, visited nodes set, and sorted list)
Technique: Topological Sort
Time: ~35 minutes.
"""
# Function to build an adjacency list from a list of nodes and a dictionary of edges
def build_adjacency_list(nodes, edges):
    # Initialize an empty adjacency list dictionary
    adjacency_list = {}

    # Initialize an empty list for each node in the adjacency list
    for node in nodes:
        adjacency_list[node] = []

    # Iterate over the edges dictionary
    for node, prerequisites in edges.items():
        # Iterate over each prerequisite for the current node
        for prerequisite in prerequisites:
            # Check if the prerequisite exists in the adjacency list
            if prerequisite in adjacency_list:
                # Add the current node as a neighbor to the prerequisite node
                adjacency_list[prerequisite].append(node)

    # Return the completed adjacency list
    return adjacency_list


# Recursive function to perform Depth-First Search (DFS) on a node and its neighbors
def dfs_visit(adjacency_list, visited, sorted_list, node):
    # If this node has already been visited, return
    if node in visited:
        return

    # Mark the node as visited
    visited.add(node)

    # Visit each neighbor of the current node
    for neighbor in adjacency_list[node]:
        dfs_visit(adjacency_list, visited, sorted_list, neighbor)

    # After visiting all neighbors, insert the current node at the beginning of the sorted list
    sorted_list.insert(0, node)


# Function to perform a topological sort on a graph represented by an adjacency list
def topological_sort(adjacency_list):
    # Initialize an empty set to keep track of visited nodes
    visited = set()
    # Initialize an empty list to store the topological sort
    sorted_list = []

    # Iterate over all nodes in the adjacency list
    for node in adjacency_list:
        # Perform DFS on each unvisited node
        dfs_visit(adjacency_list, visited, sorted_list, node)

    # Return the topologically sorted list of nodes in the correct order
    return sorted_list


def PrerequisiteCourses(courses, prerequisites):
    # Build the adjacency list for the graph
    graph = build_adjacency_list(courses, prerequisites)
    # Perform topological sort on the graph
    return topological_sort(graph)


# Test case 1
courses_1 = ["Intro to Programming", "Data Structures", "Advanced Algorithms", "Operating Systems", "Databases"]
prerequisites_1 = {
    "Data Structures": ["Intro to Programming"],
    "Advanced Algorithms": ["Data Structures"],
    "Operating Systems": ["Advanced Algorithms"],
    "Databases": ["Advanced Algorithms"]
}
expected_output_1 = [
    ["Intro to Programming", "Data Structures", "Advanced Algorithms", "Operating Systems", "Databases"],
    ["Intro to Programming", "Data Structures", "Advanced Algorithms", "Databases", "Operating Systems"]
]

# Test case 2
courses_2 = ["Intro to Writing", "Contemporary Literature", "Ancient Literature", "Comparative Literature", "Plays & Screenplays"]
prerequisites_2 = {
    "Contemporary Literature": ["Intro to Writing"],
    "Ancient Literature": ["Intro to Writing"],
    "Comparative Literature": ["Ancient Literature", "Contemporary Literature"],
    "Plays & Screenplays": ["Intro to Writing"]
}
expected_output_2 = [
    ["Intro to Writing", "Plays & Screenplays", "Contemporary Literature", "Ancient Literature", "Comparative Literature"],
    ["Intro to Writing", "Contemporary Literature", "Plays & Screenplays", "Ancient Literature", "Comparative Literature"],
    ["Intro to Writing", "Contemporary Literature", "Ancient Literature", "Plays & Screenplays", "Comparative Literature"],
    ["Intro to Writing", "Ancient Literature", "Contemporary Literature",  "Plays & Screenplays", "Comparative Literature"],
    ["Intro to Writing", "Ancient Literature",  "Plays & Screenplays",  "Contemporary Literature", "Comparative Literature"],
    ["Intro to Writing", "Plays & Screenplays", "Ancient Literature",  "Contemporary Literature", "Comparative Literature"],
    ["Intro to Writing", "Ancient Literature",  "Contemporary Literature", "Comparative Literature", "Plays & Screenplays"],
    ["Intro to Writing", "Contemporary Literature",  "Ancient Literature", "Comparative Literature", "Plays & Screenplays"]
]

# Call the function for each test case and check if the output is in the expected output list
assert PrerequisiteCourses(courses_1, prerequisites_1) in expected_output_1
assert PrerequisiteCourses(courses_2, prerequisites_2) in expected_output_2

print("All test cases passed!")



