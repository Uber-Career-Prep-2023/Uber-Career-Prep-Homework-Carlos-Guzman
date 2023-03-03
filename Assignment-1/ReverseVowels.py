"""
Given a string, reverse the order of the vowels in the string.
Examples:
Input String: "Uber Career Prep"
Modified String: "eber Ceraer PrUp"

Input String: "xyz"
Modified String: "xyz"

Input String: "flamingo"
Modified String: "flominga"

time: 42 min
method: two pointers
complexity: O(n)  

"""
# use 2 pointers

# naive aproach
"""
string = "Uber Career Prep"
x = string.lower()
y = {}
vowels = ['a','e','i','o','u']

for i in range(len(x)):
    if x[i] in vowels:
        y[i]= x[i]

print(y)
wrong

"""


    
'''
string = "Uber Career Prep"
x = string.lower()
print(x)
y = []
vowels = ['a','e','i','o','u']
#print(len(x))
for i in range(len(x)):
    if x[i] in vowels:
        y.append(x[i])
aux = len(y)-1

for j in range(len(x)):
    if x[j] in y:
        x = x.replace(x[j],y[aux],1)
        aux = aux-1
print(x,y)





 2 pointers:

string = "Uber Career Prep"
vowels = ['a','e','i','o','u','A','E','I','O','U']
string_list = list(string)

print(string_list)


left_pointer = 0
rigth_pointer = len(string_list)

        
while left_pointer < rigth_pointer:
    if string_list[left_pointer] in vowels or string_list[rigth_pointer] in vowels:
        if string_list[left_pointer] in vowels and string_list[rigth_pointer] in vowels:
            vowel_left = string_list[left_pointer]
            vowel_rigth = string_list[rigth_pointer]
            string_list[rigth_pointer] = vowel_left
            string_list[left_pointer] = vowel_rigth
        elif string_list[left_pointer] in vowels
            rigth_pointer -= 1
        else 
            left_pointer += 1

            


'''


# solution O(n) time 38 min

string = "Uber Career Prep"
vowels = set('aeiouAEIOU')
string_list = list(string)

#print(string_list)


left_pointer = 0
rigth_pointer = len(string_list) -1

        
while left_pointer < rigth_pointer:
    if string_list[left_pointer] in vowels or string_list[rigth_pointer] in vowels:
        if string_list[left_pointer] in vowels and string_list[rigth_pointer] in vowels:
            vowel_left = string_list[left_pointer]
            vowel_rigth = string_list[rigth_pointer]
            string_list[rigth_pointer] = vowel_left
            string_list[left_pointer] = vowel_rigth
            rigth_pointer -= 1
            left_pointer += 1
        elif string_list[left_pointer] in vowels:
            rigth_pointer -= 1
        elif string_list[rigth_pointer] in vowels:
            left_pointer += 1
    else: 
        rigth_pointer -= 1
        left_pointer += 1
result = "".join(string_list)
print(result)
