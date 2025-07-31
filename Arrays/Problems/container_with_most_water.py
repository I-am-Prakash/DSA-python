def max_area_bf(array):
    #write edge cases - but not required here , the code will take care
    #empty array or one element array -> can't form container and 
		#return '0'
    if(len(array) < 1): return 0
    area_max = 0
    for i in range(len(array)-1):
        for j in range(i+1, len(array)):
            area = min(array[i], array[j]) * (j - i)
            if area_max<area:
                area_max = area
    return area_max

print("BF - area -->", max_area_bf([1,8,6,2,5,4,8,3,7])) # return 49

def max_area_optimal(height):
    max_area = float("-inf")
    left, right = 0, len(height)-1
    while left < right:
        area = min(height[left], height[right]) * (right - left)
        if max_area < area : max_area = area
        if height[left] < height[right]:
            left +=1
        else:
            right-=1
    return max_area

print("Optimal - area -->", max_area_optimal([1,8,6,2,5,4,8,3,7])) # return 49
