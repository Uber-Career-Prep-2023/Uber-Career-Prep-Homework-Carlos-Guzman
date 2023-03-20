"""
Given two strings representing series of keystrokes, determine whether the resulting text is the same. Backspaces are represented by the '#' character so "x#" results in the empty string ("").

Examples:
eInput Strings: "abcde", "abcde"
Output: True

Input Strings: "Uber Career Prep", "u#Uber Careee#r Prep"
Output: True

Input Strings: "abcdef###xyz", "abcw#xyz"
Output: True

Input Strings: "abcdef###xyz", "abcdefxyz###"
Output: False


"""
#naive aproach O(n^2)
"""
string1 = "abcdef###xyz"
string2 = "abcw#xyz"

string1_lst = list(string1)
string2_lst = list(string2)

left_pointer = 0
rigth_pointer = 1


while rigth_pointer < len(string1_lst):
    if string1_lst[rigth_pointer] == "#":
        string1_lst.pop(rigth_pointer)
        string1_lst.pop(left_pointer)
        left_pointer -= 1
        rigth_pointer -= 1
    else:
        left_pointer += 1
        rigth_pointer += 1               
print(string1_lst)

left_pointer = 0
rigth_pointer = 1

while rigth_pointer < len(string2_lst):
    if string2_lst[rigth_pointer] == "#":
        string2_lst.pop(rigth_pointer)
        string2_lst.pop(left_pointer)
        left_pointer -= 1
        rigth_pointer -= 1
    else:
        left_pointer += 1
        rigth_pointer += 1               
print(string2_lst)

left_pointer = 0
rigth_pointer = 0

def comparar(string1_lst,string2_lst):
    if len(string1_lst) != len(string2_lst):
        print("no son iguales")
        return(None)
    for i,j in zip(range(len(string1_lst)),range(len(string2_lst))):
        if string1_lst[i] != string2_lst[j]:
            print("no son iguales")
            return(False)
    print("son iguales")
    return(True)

print(comparar(string1_lst,string2_lst))
"""




# solution complexity O(n), space complexity is O(n), time 28 min, uses a string processing technique

def process_keystrokes(s):
    result = ""
    for c in s:
        if c == "#":
            if len(result) > 0:
                result = result[:-1]
        else:
            result += c
    return result

string1 = "abcdef###xyz"
string2 = "abcdefxyz###"

result1 = process_keystrokes(string1)
result2 = process_keystrokes(string2)

if result1 == result2:
    print(True)
else:
    print(False)



