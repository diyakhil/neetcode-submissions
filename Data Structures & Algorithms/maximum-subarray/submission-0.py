class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_curr = nums[0]
        max_global = nums[0]

        #start range from 1 b/c we are already accounting for the first number in the current and global vals
        for i in range(1, len(nums)):
            max_curr = max(max_curr + nums[i], nums[i])

            max_global = max(max_curr, max_global)
        
        return max_global
        