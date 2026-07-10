class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0] * len(nums)

        dp[0] = 1

        for i in range(1, len(nums)):
            highest_seq = 0
            #start from end and see whichever one has the largest entry in dp
            for j in range(i-1, -1, -1):
                #only works if prev value is less than current value
                if nums[j] < nums[i]:
                    highest_seq = max(highest_seq, dp[j])
            
            dp[i] = highest_seq + 1
        
        return max(dp)
        