class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def house_robber_helper(_list):
            dp = [0] * len(_list)

            dp[0] = _list[0]
            dp[1] = max(_list[0], _list[1])

            for i in range(2, len(_list)):
                dp[i] = max(dp[i-1], _list[i] + dp[i-2])
            
            return dp[len(_list) - 1]
        
        #need to check edge cases of if there is only 2 values in the array
        x = nums[:-1]

        first_house_included = x[0]
        if len(x) >= 2:
            first_house_included = house_robber_helper(x)

        y = nums[1:]

        last_house_included = y[0]
        if len(y) >= 2:
            last_house_included = house_robber_helper(nums[1:])

        return max(first_house_included, last_house_included)
        