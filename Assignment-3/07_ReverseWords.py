"""
Given a string, return the string with the order of the space-separated words reversed
"""
"""
Time: O(N) (Iterating over all characters in the string)
Space: O(N) (Storing split words and reversed string)
Technique: String manipulation.
Time: ~25 minutes.
"""
def ReverseWords(string):
    reversed_string = ''  # Variable to store the reversed string
    splitted_string = []  # List to store individual words
    crr_word = ''  # Variable to hold the current word being constructed

    # Iterate through each character in the input string
    for i in string:
        if i == ' ':
            splitted_string.append(crr_word)  # Add the current word to the list
            crr_word = ''  # Reset the current word
        crr_word += i  # Add the current character to the current word
    splitted_string.append(crr_word)  # Add the last word to the list

    # Iterate through the reversed list of words
    for j in reversed(splitted_string):
        reversed_string += j  # Concatenate the reversed words
        reversed_string += ' '  # Add a space after each word

    return reversed_string

# Test cases
# Case 1: Basic example
input_str = "Uber Career Prep"
# Output: "Prep Career Uber"
print(ReverseWords(input_str))

# Case 2: Example with punctuation and multiple spaces
input_str = "Emma lives in Brooklyn, New York."
# Output: "York. New Brooklyn, in lives Emma"
print(ReverseWords(input_str))

# Case 3: Empty string
input_str = ""
# Output: ""
print(ReverseWords(input_str))

# Case 4: Single word
input_str = "Hello"
# Output: "Hello"
print(ReverseWords(input_str))

# Case 5: String with leading and trailing spaces
input_str = "   Uber is amazing!   "
# Output: "   amazing! is    "
print(ReverseWords(input_str))
