# Problem Statement
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An anagram is formed by rearranging the letters of another, using all the original letters exactly once.

# is it case sensitive ? No
# String will have valid 26 characters ? Yes
# what if s is empty string ? return - False

# Test Cases
# 1. s="cat" t = "car" -> False
# 2. s="rat" t = "art" -> True
# 3. s="" t="aim" -> False

def valid_anagram(s, t):
    # Edge Case
    if (len(s) != len(t)):
        return False
    # Hashmap -> to store characters and their Frequencies
    hash_map_s ={}
    hash_map_t ={}
    for char in s:
        hash_map_s[char] = hash_map_s.get(char, 0)+ 1
    
    for char in t:
        hash_map_t[char] = hash_map_t.get(char, 0)+ 1
    
    for char in t:
        if hash_map_s[char] != hash_map_t[char]:
            return False
    return True

print(valid_anagram("rata1", "1aart"))
