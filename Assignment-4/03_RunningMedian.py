"""You will be given a stream of numbers, one by one. After each new number, return the median of the numbers so far.

Examples (newest number at each step in bold):
Input: 1
Output: 1

Input: 1, 11
Output: 6

Input: 1, 11, 4
Output: 4

Input: 1, 11, 4, 15
Output: 7.5

Input: 1, 11, 4, 15, 12
Output: 11

"""


"""The first possible solution is:
 1) Insert all the values into an array as they come in
 2) while we recibe the values, sort the array
 3) Check if the array's size is even or odd
 4) If it is even, we return the average of the middle value and the following one array[n//2] + array[n//2 +1]/ 2
 5) If it's odd, we simply return the middle value of the array

 This solution is not the most optimal, it works but it is not the most efficient
"""

"""THE BEST SOLUTION IS USING THE TECHNIQUE OF MAINTAINING TWO HEAPS, A MAX HEAP AND A MIN HEAP
1) CREATE A MIN HEAP -> HERE THE UPPER HALF OF THE VALUES GREATER THAN THE MEDIAN WILL BE STORED 
2) CREATE A MAX HEAP -> HERE THE LOWER HALF OF THE VALUES LESS THAN OR EQUAL TO THE MEDIAN WILL BE STORED
3) ADD THE FIRST VALUE TO THE MAX HEAP
4) AS I RECEIVE VALUES, I DECIDE IN WHICH HEAP TO INSERT THE GIVEN VALUE
5) FOR THE FIRST VALUE, I SIMPLY INSERT IT INTO THE MAX HEAP AT THIS POINT, THIS IS THE MEDIAN, THE FIRST VALUE
6) FOR THE OTHER VALUES, I SIMPLY CALCULATE THE MEDIAN TO KNOW IN WHICH HEAP TO INSERT THE CURRENT VALUE
7) IF THE SIZE OF ONE HEAP IS LARGER THAN THE OTHER, THE MEDIAN IS THE VALUE OF THE LARGER HEAP
8) IF THE 2 HEAPS ARE OF THE SAME SIZE, THE MEDIAN IS THE AVERAGE OF THE TOP VALUES IN THE HEAP MEDIAN = (MAX_HEAP + MIN_HEAP)//2
9) NOW I COMPARE THE MEDIAN WITH THE CURRENT VALUE
10) IF THE CURRENT VALUE IS GREATER THAN THE MEDIAN, I INSERT IT INTO THE MIN HEAP, OTHERWISE I INSERT IT INTO THE MAX HEAP
11) I CHECK THAT THE HEAPS ARE BALANCED, THAT IS, THAT NEITHER HEAP EXCEEDS THE OTHER HEAP'S SIZE BY MORE THAN 1
12) IF ANY OF THE HEAPS IS LARGER THAN 1 OF WHAT THE OTHER IS, I REMOVE THE TOP VALUE OF THE LARGER HEAP AND INSERT IT INTO THE OTHER HEAP
13) AT THE END OF INSERTING ALL THE VALUES, I CALCULATE THE FINAL MEDIAN
14) IF THE SIZE OF ONE HEAP IS LARGER THAN THE OTHER, THE MEDIAN IS THE VALUE OF THE LARGER HEAP
15) IF THE 2 HEAPS ARE OF THE SAME SIZE, THE MEDIAN IS THE AVERAGE OF THE TOP VALUES IN THE HEAP MEDIAN = (MAX_HEAP + MIN_HEAP)//2

"""
import heapq

def RunningMedian(num, max_heap, min_heap):
    # If both heaps are empty
    if len(min_heap) == 0 and len(max_heap) == 0:
        # Push first number into max heap
        heapq.heappush(max_heap, -num)
        return(num,max_heap,min_heap)
    
    # If heaps are of different sizes
    if len(min_heap) != len(max_heap):
        # Median is top of the larger heap
        if len(min_heap) < len(max_heap):
            median = -max_heap[0]
        else:
            median = min_heap[0]
    else:
        # If heaps are same size, median is average of the tops of both heaps
        median = ((-max_heap[0])+min_heap[0])/2

    # If number is larger than median
    if num > median:
        # Push to min heap
        heapq.heappush(min_heap, num)
    else:
        # Else, push to max heap
        heapq.heappush(max_heap, -num)

    # If max heap is larger than min heap by more than 1
    if len(max_heap) - len(min_heap) > 1:
        # Move top of max heap to min heap
        heapq.heappush(min_heap, -heapq.heappop(max_heap)) 
    # If min heap is larger than max heap by more than 1
    elif len(min_heap) - len(max_heap) > 1:
        # Move top of min heap to max heap
        heapq.heappush(max_heap, -heapq.heappop(min_heap))

    # Recalculate median after possible rebalancing
    if len(min_heap) != len(max_heap):
        if len(min_heap) < len(max_heap):
            median = -max_heap[0]
        else:
            median = min_heap[0]
    else:
        median = ((-max_heap[0])+min_heap[0])/2

    # Return updated median and the two heaps
    return(median, max_heap, min_heap)


#Test cases
print("Test 1")   
# Test case 1:
numbers = [1, 11, 4, 15, 12]
min_heap = []
max_heap = []
for number in numbers:
    median, max_heap, min_heap = RunningMedian(number, max_heap, min_heap)
    print(median)
print("Test 2")
# Test case 2: alternating small and large numbers
numbers = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96]
min_heap = []
max_heap = []
for number in numbers:
    median, max_heap, min_heap = RunningMedian(number, max_heap, min_heap)
    print(median)
print("Test 3")
# Test case 3: numbers with duplicates
numbers = [5, 5, 5, 10, 10, 10, 15, 15, 15]
min_heap = []
max_heap = []
for number in numbers:
    median, max_heap, min_heap = RunningMedian(number, max_heap, min_heap)
    print(median)

    


