"""
Given a list of integer pairs representing the low and high end of an interval, inclusive, return a list in which overlapping intervals are merged.
Examples:

Input: [(2, 3), (4, 8), (1, 2), (5, 7), (9, 12)]
Output: [(4, 8), (1, 3), (9, 12)]

Input: [(5, 8), (6, 10), (2, 4), (3, 6)]
Output: [(2, 10)]

Input: [(10, 12), (5, 6), (7, 9), (1, 3)]
Output: [(10, 12), (5, 6), (7, 9), (1, 3)]


"""

# first aproach 
"""
array = [(2, 3), (4, 8), (1, 2), (5, 7), (9, 12)]
intervals_list = {}
new_array = []

for i in array.copy():
    for j in range(i[0],i[1]+1):
        if j in intervals_list:
            print(f"el intervalo {i} se sobre pone con el {intervals_list[j]}")
            if i[0] < intervals_list[j][0]:
                a = i[0]
                print(f"{i[0]}")
            else:
                print(f"{intervals_list[j][0]}")
                a = intervals_list[j][0]
            if i[1] > intervals_list[j][1]:
                print(f"{i[1]}")
                b = i[1]
            else:
                print(f"{intervals_list[j][1]}")
                b = intervals_list[j][1]
            
            
            new_array.append((a,b))
        intervals_list[j] = i
    if i not in new_array:
            new_array.append(i)        
print(intervals_list)
print(array)
print(new_array)

wrong
"""


# solution time complexity of the algorithm is O(n log n) + O(n) = O(n log n) time 42 min


intervals = [(5, 8), (6, 10), (2, 4), (3, 6)]

# Python uses the Timsort sorting algorithm in the sort O(nlogn) function.
def MergeIntervals(intervals):
# Sort intervals by start value
    intervals.sort(key=lambda x: x[0])
    current_interval = intervals[0]

    result = []
    for interval in intervals[1:]:
        if current_interval[1] >= interval[0]: 
            current_interval = (current_interval[0],max(current_interval[1], interval[1]))
        else:
            result.append(current_interval)
            current_interval = interval
    result.append(current_interval)  # Add the last updated interval to the results list

    return(result)
print(MergeIntervals(intervals))