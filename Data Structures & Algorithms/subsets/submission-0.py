class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sets = []

        #need curr_subset to track what we currently have in the subset combo
        #need index to see which item we are exploring currently
        def dfs(curr_subset, index):
            if index > len(nums) - 1:
                return

            #decision to include nums[index]
            curr_subset.append(nums[index])
            sets.append(list(curr_subset)) #have to make copy of list here b/c later when we pop it will change the reference to this list
            dfs(curr_subset, index + 1) #now recursive call w/ the current subset and incremented index

            #decision to exclude nums[index]
            curr_subset.pop() #remove value from subset
            dfs(curr_subset, index + 1) #process without item
        
        dfs([], 0)

        sets.append([])

        return sets
        