"""
🔍 Problem Statement:

Given an array of integers `nums` and an integer `target`, return *indices* of the two numbers such that they add up to `target`.

You may assume that each input has exactly one solution, and you may not use the same element twice.

Return the answer in any order.

"""

def twoSum(nums, target):
    num_map = {}  # value: index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
