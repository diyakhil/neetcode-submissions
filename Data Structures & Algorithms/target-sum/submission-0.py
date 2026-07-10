class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        #cache solution
        cache = {}

        #drawing out the decision tree, we can see index and total at index can be repeated many time, cache this (index, total) pair

        #i is the index we are on in the nums array
        #we need to decide whether to add the num at i or subtract it
        def helper(i, total):
            
            if total == target and i == len(nums):
                return 1
            #this base needs to go at the end b/c it will block results that we might get before that
            if i >= len(nums):
                return 0
            if (i, total) in cache:
                return cache[(i, total)]

            #we cannot do a base case where we return if sum has exceeded target b/c we can ALWAYS subtract
            
            #2 choices: add or subtract

            res = helper(i+1, total + nums[i]) + helper(i+1, total - nums[i])

            cache[(i, total)] = res

            return res
        
        return helper(0, 0)