"""
Given an origin city, a maximum travel time k, and pairs of destinations that can be reached directly from each other with corresponding travel times in hours, return the number of destinations within k hours of the origin. Assume that having a stopover in a city adds an hour of travel time.

this problem could be resolved using Dijkstra algorithm but i think i can resolve in a diferent ways using a variant
"""

"""
Complexity Analysis:
- Time: O(V + E log E) (building and sorting the adjacency list, followed by DFS)
- Space: O(V + E) (storage for adjacency list and visited cities set)

Technique Used:
The algorithm implements a combination of Depth-First Search (DFS) and Dijkstra, prioritizing shorter routes but not updating distances as Dijkstra would.

Time: ~48 minutes.
"""

def get_second_element(arr):
    return arr[1]

# Build the adjacency list based on the given edges
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
        # Add the destination node to the list of adjacent nodes for the origin node The destination node contains the city and the arrival time
        adjacency_list[edges[i][0]].append((edges[i][1],edges[i][2]))
        adjacency_list[edges[i][1]].append((edges[i][0],edges[i][2]))
    # Sort the adjacency list based on the second element of each tuple We sort to ensure that we are always visiting the closest city or the one with the shortest arrival time, this maximizing the number of cities visited based on travel time.
    for city in adjacency_list:
        adjacency_list[city] = sorted(adjacency_list[city], key=get_second_element)
    
    # Return the completed adjacency list
    return adjacency_list

# Depth-first search to count the number of destinations within the given travel time
def dfs(destinations, origin, k, visited=None):
    visited.add(origin)
    number_of_destinations = 1

    # Explore the adjacent cities from the current origin
    for city in destinations[origin]:
        # Check if travel time allows visiting the city and it hasn't been visited before
        if k >= city[1] and city[0] not in visited:
            number_of_destinations += dfs(destinations, city[0], k - city[1] - 1, visited)
        elif k <= 0:
            break


    # Return total number of visited destinations
    return number_of_destinations


# Main function to calculate the number of destinations within the given travel time
def VacationDestinations(pair_destination, origin, k):
    # Build the adjacency list from the given pairs of destinations
    destinations = build_adjacency_list(pair_destination)
    visited = set()
    #print(destinations)
    # If there are no destinations, return 0
    if len(destinations) == 0:
        return 0
    
    # Perform depth-first search to count the number of destinations
    return dfs(destinations, origin, k, visited) - 1  # We subtract one because the dfs method includes the origin city in the count

print(VacationDestinations([("Boston", "New York", 4), ("New York", "Philadelphia", 2), ("Boston", "Newport", 1.5), ("Washington, D.C.", "Harper's Ferry", 1), ("Boston", "Portland", 2.5), ("Philadelphia", "Washington, D.C.", 2.5)],"New York",5))  #should return 2 

print(VacationDestinations([("Boston", "New York", 4), ("New York", "Philadelphia", 2), ("Boston", "Newport", 1.5), ("Washington, D.C.", "Harper's Ferry", 1), ("Boston", "Portland", 2.5), ("Philadelphia", "Washington, D.C.", 2.5)],"New York",7))  #should return 4 

print(VacationDestinations([("Boston", "New York", 4), ("New York", "Philadelphia", 2), ("Boston", "Newport", 1.5), ("Washington, D.C.", "Harper's Ferry", 1), ("Boston", "Portland", 2.5), ("Philadelphia", "Washington, D.C.", 2.5)],"New York",8))  #should return 6 


# Origin = "New York", k=5
# Output: 2 (["Boston", "Philadelphia"])

# Origin = "New York", k=7
# Output: 4 (["Boston", "Philadelphia", "Washington, D.C", "Newport"])

# Origin = "New York", k=8
# Output: 6 (["Boston", "Philadelphia", "Washington, D.C", "Newport", "Harper's Ferry", "Portland"])

# Here the cities are connected in a straight line.
print(VacationDestinations([("CityA", "CityB", 2), ("CityB", "CityC", 3), ("CityC", "CityD", 4)], "CityA", 6))  # should return 2 (["CityB", "CityC"])

# Here we have multiple cities accessible directly from the origin.
print(VacationDestinations([("CityA", "CityB", 1), ("CityA", "CityC", 2), ("CityA", "CityD", 3), ("CityA", "CityE", 4)], "CityA", 3))  # should return 3 (["CityB", "CityC", "CityD"])

# Here we have a complex graph with multiple branches.
print(VacationDestinations([("CityA", "CityB", 1), ("CityB", "CityC", 2), ("CityC", "CityD", 1), ("CityA", "CityE", 3), ("CityE", "CityF", 1), ("CityF", "CityG", 2)], "CityA", 5))  # should return 4 (["CityB", "CityC", "CityE", "CityF"])
