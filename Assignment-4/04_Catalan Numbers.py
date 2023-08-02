"""The Catalan numbers are a mathematical sequence of numbers. The nth Catalan number is defined as (2n)! / (n+1)!n!. Given a 
non-negative integer n, return the Catalan numbers 0-n.
Examples:
Input: 1
Output: 1, 1

Input: 5
Output: 1, 1, 2, 5, 14, 42

"""
"""
    This problem is solved using dynamic programming.
    
    1) Declare two arrays: one for storing factorials from 0 to 2n, initializing it with the first two factorial numbers which are [1,1] (factorial array), 
    and another one to store the Catalan numbers up to n (catalan array).
    
    2) Calculate the factorials from 1 to 2n and store each factorial in the factorial array.
    
    3) Once the factorials up to 2n have been calculated, calculate all the Catalan numbers and append them to the second array using the formula: 
    catalan_number_n = factorial[2n] // (factorial[n+1] * factorial[n]).
    
    4) Return the second array as the answer.
"""


def catalan_numbers(n):
    # Initialize lists to store factorial and catalan numbers, 
    # starting with the first two factorials and Catalan numbers
    factorial = [1,1]
    catalan = [1,1]
    
    # Calculate the factorials from 2 to 2n
    for i in range(2, 2*n+1):
        factorial.append(factorial[i-1]*i)
    
    # Calculate the Catalan numbers from 2 to n
    for i in range(2, n+1):
        catalan.append(factorial[2*i]//(factorial[i+1]*factorial[i]))
    
    # Return the n-th Catalan number
    return catalan[n]

# Test cases
print(catalan_numbers(5))  # Output: 42
print(catalan_numbers(1))  # Output: 1
print(catalan_numbers(0))  # Output: 1
print(catalan_numbers(2))  # Output: 2
print(catalan_numbers(3))  # Output: 5
print(catalan_numbers(4))  # Output: 14
print(catalan_numbers(6))  # Output: 132
print(catalan_numbers(100))  # Output: a large number