def two_sum_2(nums, target):
    left, right = 0, len(nums)-1

    while(left < right):
        value = nums[left]+nums[right]
        if value == target:
            return [left+1, right+1]
        elif value < target:
            left+=1
        else:
            right-=1
print("input array ->", [1,3,4,6])
print("Target ->", 9)
print("Pair of indices that holds values add up to target is", two_sum_2([1,3,4,6], 9))
# prints [2,4]