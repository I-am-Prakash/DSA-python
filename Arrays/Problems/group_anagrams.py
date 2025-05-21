'''Problem Statement'''
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

'''Clarifying Questions'''
# we always have something grouped together ?
# -> what if we are not able to group ? -> you'll return each string as an individual array

# if input array -> empty [] -> return empty nested array[[]]

'''Test Cases'''
# Input: strs = ["eat", "rat", "tea", "art", "cat"]
# Output: [["eat","tea"],["rat","art"],["cat"]]

# Input: strs = ["a"]
# Output: [["a"]]


def group_anagram(strings_array):
    # HashMap -> to store sorted word -> as key 
    # values -> whichever word sorting version equates key -> appended to a list -> added as value -> HashMap
    # { "aet": ["eat","tea"], "art" : ["rat","art"], "act" : ["cat"]}
    anagrams = {}

    for word in strings_array:
        sorted_word = ''.join(sorted(word))
        # print(word + " -> "+ sorted_word)
        if sorted_word not in anagrams:
            anagrams[sorted_word] =[]
        anagrams.get(sorted_word, []).append(word)
        # print(f":->{anagrams.values()}")
    return list(anagrams.values())
    
print(f"Output :-> {group_anagram(["eat", "rat", "tea", "art", "cat"])}")



