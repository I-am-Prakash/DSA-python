
def search_in_rotated_sorted_array(nums, target):
    left, right = 0, len(nums)-1

    while left < right:
        mid = (left + right)//2
        if nums[mid] == target:
            return mid
        if nums[left] <= nums[mid]:
            if nums[left]<=target< nums[mid]:
                right = mid-1
            else:
                right = mid+1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid+1
            else:
                right = mid-1
                
    return -1





print(search_in_rotated_sorted_array([3,4,5,-1,2], 2))
