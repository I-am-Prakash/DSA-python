
def min_in_rotated_sorted_array(nums):
    left, right = 0, len(nums)-1

    while (left < right):
        mid = (left + right)//2
        if nums[mid] > nums[right]:
            left = mid+1
        else:
            right = mid
    return nums[mid]

print(min_in_rotated_sorted_array([3,4,5,-1,2]))
