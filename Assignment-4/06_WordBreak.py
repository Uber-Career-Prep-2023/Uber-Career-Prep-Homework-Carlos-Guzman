"""Given a string of characters without spaces and a dictionary of valid words, determine if it can be broken into a list of valid words by adding spaces. 
Dictionary:
Elf   Go   Golf   Man    Manatee    Not    Note   Pig
Quip   Tee   Teen

Input: mangolf
Output: True (“man”, “golf”)

Input: manateenotelf
Output: True (“manatee”, “not”, “elf”)

Input: quipig
Output: False
"""

"""
This problem is solved using dynamic programming:
1) We convert all the words in the dictionary into a set for more efficient access. We also initialize a list called dp of length n+1, where n is the length of the string.

2) We set dp[0] to True, as the empty string can always be divided.

3) We iterate over the string from index 1 to the end. For each index i, we check whether the string up to i can be split into words from the dictionary.

4) To verify this, we iterate from 0 to i, looking for a position j such that dp[j] is True and the string from j+1 to i is in the dictionary. If we find such a position j, we set dp[i] to True.

5) If we do not find such a position j, we leave dp[i] as False.

6) We continue iterating through the string until we have reviewed the entire string.

7) Finally, we return dp[-1], which represents whether the complete string can be divided into words from the dictionary.
"""


def word_break(dictionary, string):
    # Convert the dictionary into a set for faster access and make all words lowercase
    dictionary = set(word.lower() for word in dictionary)
    # Convert the input string to lowercase
    string = string.lower()
    # Initialize a list to store the results of subproblems
    dp = [False] * (len(string) + 1)
    # Set the first element of the list to True, since the empty string can always be broken into words
    dp[0] = True

    # Iterate over the string from index 1 to the end
    for i in range(1, len(string) + 1):
        # Iterate over the string from index 0 to i
        for j in range(i):
            # If the string from index 0 to j can be broken into words and the string from index j+1 to i is in the dictionary
            if dp[j] and string[j:i] in dictionary:
                # Set dp[i] to True
                dp[i] = True
                # Break out of the loop
                break

    # Return the last element of the list, which represents whether the entire string can be broken into words
    return dp[-1]


dictionary = ["Elf", "Go", "Golf", "Man", "Manatee", "Not", "Note", "Pig", "Quip", "Tee", "Teen"]

print(word_break(dictionary, "mangolf"))  # Should return: True
print(word_break(dictionary, "manateenotelf"))  # Should return: True
print(word_break(dictionary, "quipig"))  # Should return: False

