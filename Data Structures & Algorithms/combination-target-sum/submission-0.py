class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        
        #KEY: need to keep track of index b/c in the subsequent recursive calls, we only want the options to be the current value or values after to prevent duplicates
        def helper(curr_sum, curr_list, index):
            if curr_sum == target:
                res.append(curr_list.copy()) #append copy
                return
            
            if curr_sum > target:
                return
            
            for i in range(index, len(nums)):
                curr_list.append(nums[i])
                curr_sum += nums[i]
                
                helper(curr_sum, curr_list, i) 
                #KEY: pass in i here (you can pick this candidate or any candidate after in the next recursive step)

                #now remove the value from curr_list and decrement it from curr_sum so we can process next possible val
                curr_list.pop()
                curr_sum -= nums[i]
        
        helper(0, [], 0)

        return res
        