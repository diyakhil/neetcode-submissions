class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []

        sorted_nums = sorted(nums) #need to sort input

        def helper(curr_set, index):
            if index > len(sorted_nums) - 1:
                if curr_set not in res:
                    res.append(curr_set.copy())
                
                return
            
            curr_set.append(sorted_nums[index])
            helper(curr_set, index+1) #repeat with next value in the list

            curr_set.pop()
            helper(curr_set, index+1) #proceed without adding this value
        
        helper([], 0)

        return res
        