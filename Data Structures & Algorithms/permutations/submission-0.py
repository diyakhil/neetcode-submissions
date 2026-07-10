class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def helper(curr_set):
            
            if len(curr_set) == len(nums):
                res.append(curr_set.copy()) #APPEND COPY
                return
            
            for i in range(len(nums)):
                if nums[i] in curr_set:
                    continue
                
                curr_set.append(nums[i])
                helper(curr_set)
                curr_set.pop()
        
        helper([])
        return res
        