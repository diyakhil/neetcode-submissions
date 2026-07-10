class Solution:
    def trap(self, height: List[int]) -> int:
        #max_left - maximum values starting from the start of the array, we will keep track of all time max
        #max_right - maximum values starting from the end of the array, similar approach as above

        #to find the amount of water that can be trapped at index i
        #find the minimum (bottleneck) of max_left and max_right and then subtract the height at i itself
        #negative and 0 values means no water can be trapped

        max_left = [0] * len(height)
        max_right = [0] * len(height)

        #populate both arrays
        max_curr_l = 0
        for i in range(len(max_left)):
            max_curr_l = max(max_curr_l, height[i])
            max_left[i] = max_curr_l
        
        max_curr_r = 0
        for i in range(len(max_right) - 1, -1, -1):
            max_curr_r = max(max_curr_r, height[i])
            max_right[i] = max_curr_r

        max_water = 0
        for i in range(len(height)):
            area = min(max_left[i], max_right[i]) - height[i]
            if area > 0:
                max_water += area
        
        return max_water
        