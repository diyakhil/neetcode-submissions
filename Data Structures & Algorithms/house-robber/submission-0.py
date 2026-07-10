class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)

        if len(nums) < 2:
            return nums[0]

        dp[0] = nums[0]

        #KEY: this is not just dp[1] = nums[1] b/c 2nd value max can be the first value and we can skip the second one entirely
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])
        
        return dp[len(nums) -1]
        