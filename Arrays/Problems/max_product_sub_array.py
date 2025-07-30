# Given an integer array nums, find the contiguous subarray within an array (containing at least one number) 
# which has the largest product, and return the product.


"""
Observations
- A negative number can become positive if multiplied with another negative
- A zero can reset the product

Input: nums = [2, 3, -2, 4]
Output: 6
# Explanation: [2, 3] has max product 6

Input: nums = [-2, 0, -1]
Output: 0
# Explanation: Only 0 is safe

Input: nums = [-2, 3, -4]
Output: 24
# Explanation: [-2, 3, -4] = 24
"""

# B.F
def max_prod_sub_array(nums):
    max_prod = float('-inf')
    for i in range(len(nums)):
        curr_max =1
        for j in range(i, len(nums)):
            curr_max = curr_max*nums[j]
            max_prod = max(max_prod, curr_max)
    return max_prod

# Optimal 
def max_prod_sub_array_o(nums):
    max_so_far = nums[0]
    min_so_far = nums[0]
    global_max = nums[0]
    for i in range(1, len(nums)):
        num = nums[i]
        if num < 0:
            max_so_far, min_so_far = min_so_far, max_so_far
        # max_so_far= max_so_far*num
        max_so_far = max(num, max_so_far*num)
        # min_so_far = min_so_far*num
        max_so_far = min(num, min_so_far*num)
        
        global_max = max(global_max, max_so_far)
    return global_max

print(max_prod_sub_array_o([2, 3, -2, 4]))
print(max_prod_sub_array_o([-2, 0, -1]))
print(max_prod_sub_array_o([-2, 3, -4]))
