"""
Two strings are considered to be “k-anagrams” if they can be made into anagrams by changing at most k characters in one of the strings. Given two strings and an integer k, determine if they are k-anagrams.

Examples:
Input Strings: "apple", "peach"
Input k: 1
Output: False

Input Strings: "apple", "peach"
Input k: 2
Output: True

Input Strings: "cat", "dog"
Input k: 3
Output: True

Input Strings: "debit curd", "bad credit"
Input k: 1
Output: True

Input Strings: "baseball", "basketball"
Input k: 2
Output: False


"""


""" naive aproach 
def k_anagrams(string1,string2,k):

    if len(string1) != len(string2):
        return False

    dict_str1 = {}
    dict_str2 = {}

    for char1,char2 in zip(string1, string2):
        dict_str1[char1] = dict_str1.get(char1, 0) + 1
        dict_str2[char2] = dict_str2.get(char2, 0) + 1
    #print(dict_str2,dict_str1)

    for key, value in dict_str1.copy().items():
        if key in dict_str2:
            dict_str1[key] -= 1
        if dict_str1[key] == 0:
            del dict_str1[key]
    #print(dict_str2,dict_str1)
    if len(dict_str1) > k:
        return False
    else:
        return True

print(k_anagrams(string1,string2,k))

wrong 
"""



# def k_anagrams(string1,string2,k):
#     count = 0
#     if len(string1) != len(string2):
#         return False

#     dict_str1 = {}
#     dict_str2 = {}
#     for char1,char2 in zip(string1, string2):
#         dict_str1[char1] = dict_str1.get(char1, 0) + 1
#         dict_str2[char2] = dict_str2.get(char2, 0) + 1
#     for key, value in dict_str1.copy().items():
#         if key not in dict_str2:
#             count += 1
#         if key in dict_str2:
#             value -= 1
#             dict_str2[key] -= 1
#             if dict_str2[key] == 0:
#                 del dict_str2[key]
#             if value == 0:
#                 del dict_str1[key]
#     if count > k:
#         return False
#     else:
#         return True

# print(k_anagrams(string1,string2,k))


#solution complexity O(n),The space complexity is O(n), time 35 min

string1 = "baseball"
string2 = "basketball"
k = 2


def k_anagrams(string1, string2, k):
    count = 0
    if len(string1) != len(string2):
        return False

    dict_str = {}
    for char in string1:
        dict_str[char] = dict_str.get(char, 0) + 1
    for char in string2:
        if char in dict_str:
            dict_str[char] -= 1
            if dict_str[char] == 0:
                del dict_str[char]
        else:
            count += 1
        if count > k:
            return False

    return True

print(k_anagrams(string1,string2,k))
