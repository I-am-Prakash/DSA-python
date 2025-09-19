def merge(nums1, nums2):
        """Do not return anything, modify nums1 in-place instead."""
        for i in range(len(nums2)):
            for j in range(len(nums1)):
                if nums2[i] >nums1[j] or nums2[i] == nums1[j]:
                    continue
                elif nums2[i] < nums1[j]:
                    nums1.insert(j, nums2[i])
                if nums2[i] > nums1[j] and j == len(nums1):
                    nums1.append(nums2[i])
        return nums1
 
print(merge([1,2,3,0,0,0], [2,5,6], 3, 3))