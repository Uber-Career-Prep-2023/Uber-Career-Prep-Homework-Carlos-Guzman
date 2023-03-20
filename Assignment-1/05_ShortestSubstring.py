"""

Given a string and a second string representing required characters, return the length of the shortest substring containing all the required characters.

Examples:
Input Strings: "abracadabra", "abc"
Output: 4
(Shortest Substring: "brac")

Input Strings: "zxycbaabcdwxyzzxwdcbxyzabccbazyx", "zzyzx" (Fun fact: "Zzyzx" is a town in the Mojave Desert in California!)
Output: 10
(Shortest Substring: "zzxwdcbxyz")

Input Strings: "dog", "god"
Output: 3
(Shortest Substring: "dog")


"""



string = "zxycbaabcdwxyzzxwdcbxyzabccbazyx"
target = "zzyzx"


# solution the optimal solution is using the dynamic sliding window
# time 47 min, time complexity O(n), space complexity is O(k) where k is the number of distinct characters in the target string 


def shortest_substring(s: str, target: str) -> int:
    target_dict = {}
    for c in target:
        target_dict[c] = target_dict.get(c, 0) + 1
        
    window_start = 0
    window_end = 0
    min_window_len = float('inf')
    target_len = len(target_dict)
    target_seen = 0
    
    while window_end < len(s):
        if s[window_end] in target_dict:
            target_dict[s[window_end]] -= 1
            if target_dict[s[window_end]] == 0:
                target_seen += 1
                
        while target_seen == target_len:
            if min_window_len > window_end - window_start + 1:
                min_window_len = window_end - window_start + 1
                
            if s[window_start] in target_dict:
                target_dict[s[window_start]] += 1
                if target_dict[s[window_start]] > 0:
                    target_seen -= 1
                    
            window_start += 1
            
        window_end += 1
        
    return min_window_len if min_window_len != float('inf') else 0

print(shortest_substring(string, target))


