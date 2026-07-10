class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        sorted_candidates = sorted(candidates)

        def helper(curr_list, curr_count, index):
            #recurse until we reach the target or go over the target
            if curr_count == target:
                res.append(curr_list.copy()) #we have to append a copy of the list
                return
            if curr_count > target:
                return
            
            prev = -1
            #go through the list from the current index value to end of candidates
            for i in range(index, len(sorted_candidates)):
                if sorted_candidates[i] == prev:
                    continue
                prev = sorted_candidates[i]
                #first we do the case where we add the current number
                curr_list.append(sorted_candidates[i])
                curr_count += sorted_candidates[i]

                helper(curr_list, curr_count, i+1) #don't include current value in next calculation

                #decision to not include current number
                curr_list.pop()
                curr_count -= sorted_candidates[i]
        
        helper([], 0, 0)

        return res
        