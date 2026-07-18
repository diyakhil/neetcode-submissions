class Solution:
    def jump(self, nums: List[int]) -> int:
        goalpost = len(nums) - 1
        jumps = 0

        #need to iterate until goalpost reaches the front
        while goalpost > 0:
            min_index = goalpost

            #start from goal post and go backward since we only care about the hops before
            for i in range(goalpost -1, -1, -1):
                if goalpost - i <= nums[i]:
                    min_index = min(min_index, i)
                
            goalpost = min_index
            jumps += 1
        
        return jumps
        