# Given an integer array nums, find the contiguous subarray 
# (containing at least one number) which has the largest sum, and return its sum.
'''
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6

Input: nums = [1]
Output: 1

Input: nums = [5,4,-1,7,8]
Output: 23
'''

# B.F

def max_sub_array(nums):
    max_value = float('-inf')
    for i in range(len(nums)):
        curr_sum = 0
        for j in range(i, len(nums)):
            curr_sum += nums[j]
            max_value = max(max_value, curr_sum)
    return max_value


# Optimal - Kadane's Algorithm

def max_sub_array_o(nums):
    curr_sum = nums[0]
    max_sum = nums[0]

    for i in range(1, len(nums)):
        curr_sum = max(nums[i], curr_sum+nums[i])
        max_sum = max(max_sum, curr_sum)
    return max_sum



print(max_sub_array_o([-2, -5]))
print(max_sub_array_o([4,-1,2,1]))
print(max_sub_array_o([1]))
print(max_sub_array_o([-2,1,-3,4,-1]))
