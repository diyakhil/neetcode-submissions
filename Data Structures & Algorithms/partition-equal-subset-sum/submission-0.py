class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        else:
            half = total // 2

            dp = [{}] * len(nums)

            dp[0] = {0, nums[0]}

            for i in range(1, len(nums)):
                if nums[i] == half:
                    return True
                new_set = dp[i-1].copy()

                for val in dp[i-1]:
                    new_val = val + nums[i]
                    
                    if new_val == half:
                        return True
                    new_set.add(new_val)
                dp[i] = new_set
            
            return False
        