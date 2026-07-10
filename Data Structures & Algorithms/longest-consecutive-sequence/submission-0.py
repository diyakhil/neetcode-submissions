class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums_set = set(nums)

        longest = 0

        #if there is a left neighbor, we will not add it to list, we will move on b/c that will be 
        for num in nums_set:
            count = 0
            if num - 1 not in nums_set:
                #num needs to be counted in the seq as well
                count += 1
                
                copy_num = num + 1
                
                while copy_num in nums_set:
                    count+=1
                    copy_num += 1
            longest = max(longest, count)
            
        return longest
        
        