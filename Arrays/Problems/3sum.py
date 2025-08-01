def three_sum_brute_force(nums):
    """
    BRUTE FORCE - All possible combination and take one's which satisfies the constraints
    Time: O(n³), Space: O(k) where k is number of triplets
    """
    result = set()  # Use set to avoid duplicates
    n = len(nums)
    
    # Check every possible triplet
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    # Sort triplet to handle duplicates like [-1,0,1] and [0,1,-1]
                    triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                    result.add(triplet)
    
    return [list(triplet) for triplet in result]

def three_sum_optimized(nums):
    """
    OPTIMIZED APPROACH - Sort(for handling duplicates) + Fix One(consider target =-fixone) + Two Pointers(to find target in 1'le pass)
    Time: O(n²), Space: O(1) 
    
    STRATEGY:
    1. Sort array → enables two pointers
    2. Fix first element → reduces to 2Sum problem  
    3. Use two pointers on remaining subarray
    4. Skip duplicates carefully
    """
    nums.sort()  # O(n log n) - CRITICAL step
    result = []
    n = len(nums)
    
    for i in range(n - 2):  # Fix first element (need at least 3 elements)
        # Skip duplicate first elements
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        # Now solve 2Sum for target = -nums[i]
        left = i + 1
        right = n - 1
        target = -nums[i]
        
        while left < right:
            current_sum = nums[left] + nums[right]
            
            if current_sum == target:
                # Found a valid triplet!
                result.append([nums[i], nums[left], nums[right]])
                
                # Skip duplicates for left pointer
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                
                # Skip duplicates for right pointer - Not Required Why ?
                # if left fixed -> if some right value not working -It's duplicate also won't work - so fixing one side is enough for this job
                # while left < right and nums[right] == nums[right - 1]:
                #     right -= 1
                
                # Move both pointers
                left += 1
                right -= 1
                
            elif current_sum < target:
                left += 1   # Need larger sum -> 
                # to increase we need to remove max negative number -> hence automatically - sum will increase 
            else:
                right -= 1  # Need smaller sum -> remove max positive(right pointer) - sum decrease
    
    return result

print("Input Array -> ", [-1,0,1,2,-1,-4])
print("Brute-Force->", three_sum_brute_force([-1,0,1,2,-1,-4]))
print("Optimized->", three_sum_optimized([-1,0,1,2,-1,-4]))
# Brute-Force-> [[-1, 0, 1], [-1, -1, 2]]
# Optimized-> [[-1, -1, 2], [-1, 0, 1]]