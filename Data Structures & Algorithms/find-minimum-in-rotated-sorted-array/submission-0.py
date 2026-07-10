class Solution:
    def findMin(self, nums: List[int]) -> int:
        #start out the min value to be the leftmost value in the array to account for case where all values are sorted
        min_value = nums[0]
        left = 0
        right = len(nums) - 1

        #we are always comparing w the right value b/c this whole thing rides on the fact that the right value is
        #max value in the min side of the array

        while left <= right:
            mid = (left + right) // 2
            min_value = min(min_value, nums[mid])

            #we are still in greater half of the array (left), we need to move left pointer towards right
            if nums[mid] > nums[right]:
                left = mid + 1
            #we are already in the smaller half of array (right) and need to zero in on the smallest value
            elif nums[mid] <= nums[right]:
                right = mid - 1
        return min_value
        