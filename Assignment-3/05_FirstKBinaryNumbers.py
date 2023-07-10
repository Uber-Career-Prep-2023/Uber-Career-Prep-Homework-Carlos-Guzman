"""Given a number, k, return an array of the first k binary numbers, represented as strings.
"""
"""
Time: O(N^2) (converting each of first N numbers to binary)
Space: O(N) (storing N binary strings)
Technique: Iteration and base conversion
Time: ~30 minutes.
"""
"""

# Function to convert decimal number to binary string
def decimal_to_binary(decimal):
    # List to store the remainder
    remainder = []
    
    # Check if the number is zero
    if decimal == 0:
        return	'0'
    
    # Loop until the decimal number becomes zero
    while decimal != 0:
        # Append the remainder when the decimal number is divided by 2
        remainder.append(str(decimal % 2))
        
        # Update the decimal number by dividing it by 2
        decimal = decimal // 2
    
    # Reverse the remainder list and join the elements to get the binary string
    binary = ''.join(reversed(remainder))
    
    return binary

# Function to generate first k binary numbers
def FirstKBinaryNumbers(number):
    # Initialize the counter
    aux = 0
    # List to store the binary numbers
    binary_numbers = []
    
    # Loop until counter is less than the number
    while aux < number:
        # Convert the counter to binary and append to the list
        binary_numbers.append(decimal_to_binary(aux))
        
        # Increment the counter
        aux += 1
    
    return binary_numbers

# Test cases
print(FirstKBinaryNumbers(5))  # Should print ['0', '1', '10', '11', '100']
print(FirstKBinaryNumbers(10))  # Should print ['0', '1', '10', '11', '100', '101', '110', '111', '1000', '1001']
"""
#solution with a queue

from queue import Queue

def FirstKBinaryNumbers(k):
    q = Queue()
    # Start with the binary representation of 1
    q.put("1")

    result = ["0"] # Start with the binary representation of 0
    while k > 1:
        # Remove the next binary number from the queue and add it to the result
        bin_num = q.get()
        result.append(bin_num)

        # Add '0' and '1' to the end of the binary number and put it back in the queue
        q.put(bin_num + "0")
        q.put(bin_num + "1")

        k -= 1

    return result

print(FirstKBinaryNumbers(5))  # Should print ['0', '1', '10', '11', '100']
print(FirstKBinaryNumbers(10))  # Should print ['0', '1', '10', '11', '100', '101', '110', '111', '1000', '1001']