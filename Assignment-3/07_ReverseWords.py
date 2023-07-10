"""
Given a string, return the string with the order of the space-separated words reversed
"""
"""
Time: O(N) (Iterating over all characters in the string)
Space: O(N) (Storing split words and reversed string)
Technique: String manipulation.
Time: ~25 minutes.
"""
# def ReverseWords(string):
#     reversed_string = ''  # Variable to store the reversed string
#     splitted_string = []  # List to store individual words
#     crr_word = ''  # Variable to hold the current word being constructed

#     # Iterate through each character in the input string
#     for i in string:
#         if i == ' ':
#             splitted_string.append(crr_word)  # Add the current word to the list
#             crr_word = ''  # Reset the current word
#         crr_word += i  # Add the current character to the current word
#     splitted_string.append(crr_word)  # Add the last word to the list

#     # Iterate through the reversed list of words
#     for j in reversed(splitted_string):
#         reversed_string += j  # Concatenate the reversed words
#         reversed_string += ' '  # Add a space after each word

# #     return reversed_string
# # Test cases
# # Case 1: Basic example
# input_str = "Uber Career Prep"
# # Output: "Prep Career Uber"
# print(ReverseWords(input_str))

# # Case 2: Example with punctuation and multiple spaces
# input_str = "Emma lives in Brooklyn, New York."
# # Output: "York. New Brooklyn, in lives Emma"
# print(ReverseWords(input_str))

# # Case 3: Empty string
# input_str = ""
# # Output: ""
# print(ReverseWords(input_str))

# # Case 4: Single word
# input_str = "Hello"
# # Output: "Hello"
# print(ReverseWords(input_str))

# # Case 5: String with leading and trailing spaces
# input_str = "   Uber is amazing!   "
# # Output: "   amazing! is    "
# print(ReverseWords(input_str))



def ReverseWordsStack(string):
    reversed_string = ''  # Initialize an empty string to hold the reversed string
    stack = []  # Initialize an empty list to act as a stack to hold individual words
    word = ''  # Initialize an empty string to hold the current word being constructed

    # Iterate through each character in the input string
    for char in string:
        if char == ' ':  # If the current character is a space
            stack.append(word)  # Add the current word to the stack
            word = ''  # Reset the current word to an empty string
        else:
            word += char  # If the current character is not a space, add it to the current word

    # Add the last word to the stack
    stack.append(word)

    # While the stack is not empty
    while stack:
        # Pop the top word off the stack and add it to the reversed string
        reversed_string += stack.pop()
        if stack:  # If there are still words in the stack
            reversed_string += ' '  # Add a space after each word (except for the last word)

    return reversed_string  # Return the reversed string
# Test case 1: Basic example
input_str = "Hello, my name is Carlos Guzman"
# Expected output: "Guzman Carlos is name my Hello,"
print(ReverseWordsStack(input_str))

# Test case 2: Single word
input_str = "Hello"
# Expected output: "Hello"
print(ReverseWordsStack(input_str))

# Test case 3: Empty string
input_str = ""
# Expected output: ""
print(ReverseWordsStack(input_str))

# Test case 4: String with leading and trailing spaces
input_str = "   Hello, world!   "
# Expected output: "   world! Hello,"
print(ReverseWordsStack(input_str))

# Test case 5: String with multiple spaces between words
input_str = "Hello,   world!"
# Expected output: "world!   Hello,"
print(ReverseWordsStack(input_str))
