### Problem Statement

# Given a string s containing just the characters '(', ')', '{', '}', '[', and ']', 
# determine if the input string is valid.

# A string is valid if:
#  1. Open brackets are closed by the same type of brackets.
#  2. Open brackets are closed in the correct order.

# Test Cases
# ({([])}) -> True
# ({([})}) -> False

# Approach
# 1. Hashmap -> stores "}" : "{"
# 2. Stack -> 1. while found open -> push to stack
#          -> 2. found close -> pop from stack 

def valid_parentheses(brackets_string):
    # HashMap to store close and open brackets as key and pair of different kinds
    hash_map = { "}" : "{", 
                ")" : "(", 
                "]" : "["
                }
    stack =[]
    for parentheses in brackets_string:
        if parentheses in hash_map:
            if stack and stack.pop() != hash_map[parentheses]:
                return False
        else:
            stack.append(parentheses)
    return not stack



print(valid_parentheses("({([})})")) #False
print(valid_parentheses("({([])})")) #True
