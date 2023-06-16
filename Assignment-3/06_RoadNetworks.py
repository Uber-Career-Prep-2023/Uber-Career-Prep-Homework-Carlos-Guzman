"""In some states, it is not possible to drive between any two towns because they are not connected to the same road network. Given a list of towns and a list of pairs representing roads between towns, return the number of road networks. (For example, a state in which all towns are connected by roads has 1 road network, and a state in which none of the towns are connected by roads has 0 road networks.)
"""
"""
Time: O(V+E) (DFS traversal on adjacency list)
Space: O(V) (storing visited nodes and adjacency list)
Technique: Depth-First Search (DFS) on each non-visited town.
Time: ~38 minutes.
"""

def build_adjacency_list(edges):
    # Initialize an empty dictionary to hold the adjacency list
    adjacency_list = {}

    # Loop through each edge in the input list
    for i in range(len(edges)):
        # If the origin node of the edge is not already in the adjacency list, 
        # add it with an empty list as its value
        if edges[i][0] not in adjacency_list:
            adjacency_list[edges[i][0]] = []

        # If the destination node of the edge is not already in the adjacency list, 
        # add it with an empty list as its value
        if edges[i][1] not in adjacency_list:
            adjacency_list[edges[i][1]] = []

        # Add the destination node to the list of adjacent nodes for the origin node
        adjacency_list[edges[i][0]].append(edges[i][1])
    
    # Return the completed adjacency list
    return adjacency_list

def dfs(root,road_network,visited):
    # If root has already been visited, return the visited set
    if root in visited:
        return visited

    # Add the root to the visited set
    visited.add(root)

    # Call DFS on each neighbor of the root
    for i in road_network[root]:
        dfs(i,road_network,visited)

    # Return the set of visited nodes
    return visited

def RoadNetworks(towns, roads):
    # Initialize the number of road networks to zero
    networks = 0

    # Initialize the set of visited nodes
    visited = set()

    # If there are no roads, return zero
    if len(roads) == 0:
        return networks

    # Build the adjacency list
    road_network = build_adjacency_list(roads)

    # For each node in the road network
    for i in road_network:
        # If the node has not been visited and has neighbors
        if i not in visited and len(road_network[i]) != 0:
            # Increment the number of road networks
            networks += 1

            # Add the set of nodes reachable from the current node to the visited set
            visited |= dfs(i,road_network,visited)

    # Return the number of road networks
    return networks

# Test cases
print(RoadNetworks(["Skagway", "Juneau", "Gustavus", "Homer", "Port Alsworth", 
                    "Glacier Bay", "Fairbanks", "McCarthy", "Copper Center", "Healy"], 
                   [("Anchorage", "Homer"), ("Glacier Bay", "Gustavus"), 
                    ("Copper Center", "McCarthy"), ("Anchorage", "Copper Center"), 
                    ("Copper Center", "Fairbanks"), ("Healy", "Fairbanks"), 
                    ("Healy", "Anchorage")]))  # Output: 2

print(RoadNetworks(["Kona", "Hilo", "Volcano", "Lahaina", "Hana", "Haiku", 
                    "Kahului", "Princeville", "Lihue", "Waimea"], 
                   [("Kona", "Volcano"), ("Volcano", "Hilo"), 
                    ("Lahaina", "Hana"), ("Kahului", "Haiku"), 
                    ("Hana", "Haiku"), ("Kahului", "Lahaina"), 
                    ("Princeville", "Lihue"), ("Lihue", "Waimea")]))  # Output: 2
# Test case with no towns and no roads
print(RoadNetworks([], []))  # Output: 0

# Test case with one town and no roads
print(RoadNetworks(["Town A"], []))  # Output: 0

# Test case with multiple towns but no roads
print(RoadNetworks(["Town A", "Town B", "Town C"], []))  # Output: 0

# Test case with one road network
print(RoadNetworks(["Town A", "Town B", "Town C"], [("Town A", "Town B"), ("Town B", "Town C")]))  # Output: 1

# Test case with disconnected road networks
print(RoadNetworks(["Town A", "Town B", "Town C", "Town D"], [("Town A", "Town B"), ("Town C", "Town D")]))  # Output: 2

# Test case with a circular road network
print(RoadNetworks(["Town A", "Town B", "Town C", "Town D"], [("Town A", "Town B"), ("Town B", "Town C"), ("Town C", "Town D"), ("Town D", "Town A")]))  # Output: 1
