def valid_palindrome(input_str):
    left, right = 0, len(input_str)-1

    while(left < right):
        
        # Skip any non-alpha numeric characters
        while left < right and not input_str[left].isalnum():
            left+=1
        
        while left<right and not input_str[right].isalnum():
            right-=1
        
        if input_str[left].lower() != input_str[right].lower():
            return False
        left+=1
        right-=1
    return True

print(valid_palindrome("I AbC, c : bA, j  ,]"))
