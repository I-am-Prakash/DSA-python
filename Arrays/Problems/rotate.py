# bf -> brute force Approach -> extra space
def rotate_bf(k, nums):
    k = k % len(nums)
    nums[:] = nums[-k:] + nums[:-k]
    return nums

print(rotate_bf(3, [1,2,3,4,5,6,7]))

'''
Time Complexity: O(n) Space Complexity: O(n)

Behind the scenes:

nums[-k:] creates a new list containing the last k elements of nums. This operation takes O(k) time.
nums[:-k] creates a new list containing all elements of nums except the last k elements. This operation takes O(n-k) time.
The + operator concatenates the two lists, creating a new list containing all elements of nums in the rotated order. This operation takes O(n) time.
In total, the time complexity is O(k) + O(n-k) + O(n) = O(2n) = O(n).
The space complexity is O(n) because we're creating new lists to store the sliced and concatenated elements.
'''

# bf -> better approach

def rotate_better(k, nums):
    n=len(nums)
    if n == 0: return []
    k = k % n
    if k==0 or k==n:
        return nums
    else:
        temp = nums[-k:] # O(k) time and O(k) space
        for i in reversed(range(0, n-k)): # O(n-k)
            nums[i+k] = nums[i]
        for j in range(0, k): # O(k)
            nums[j] = temp[j]
        return nums
    
# T.C = O(k) + O(n-k) + O(k) = O(n+k)= O(n)  since n>k
# S.C = O(k)
print(rotate_better(3, [1,2,3,4,5,6,7]))



# better -> optimal

def rotate_optimal(k, nums):
    def reverse(nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
        return nums
    n = len(nums)
    if n==0: return []
    k = k % n
    if k==0 or k==n:
        return nums
    else:
        reverse(nums, 0, n-1)
        reverse(nums, 0, k-1)
        reverse(nums, k, n-1)
    return nums
# T.C = O(n) + O(k) + O(n-k) = O(2n) = O(n)
# S.C = O(1)

print(rotate_optimal(3, [1,2,3,4,5,6,7]))
