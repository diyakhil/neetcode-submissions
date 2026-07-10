class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #sort the array first
        #keep one element fixed and then perform 2sum II on the other elements
        #to see which one adds up to complement the fixed value
        #make sure to skip over repeating values

        #need to return nums rather than indices

        sorted_nums = sorted(nums)
        res = []
        
        for i in range(len(sorted_nums)):
            #need to skip over dup values
            if i > 0 and sorted_nums[i] == sorted_nums[i-1]:
                continue
            
            fixed_val = sorted_nums[i]
            target = -fixed_val

            #KEY: we only check for values that sum to the target after the fixed_val, this is because any values including the nums before target have alr been accounted for, see example [-4, -1, -1, 0, 1, 2, 3, 5] (-4, -1, 5), (-1, -4, 5) would have already been accounted for before
            left = i + 1
            right = len(sorted_nums) - 1
            
            while left < right:
                if sorted_nums[left] + sorted_nums[right] > target:
                    #need to check to make sure the next elem is not dup
                    val = sorted_nums[right]
                    
                    while right > left and sorted_nums[right] == val:
                        right -= 1
                
                if sorted_nums[left] + sorted_nums[right] < target:
                    val = sorted_nums[left]

                    while left < right and sorted_nums[left] == val:
                        left += 1
                
                if sorted_nums[left] + sorted_nums[right] == target and right != left:
                    res.append([sorted_nums[i], sorted_nums[left], sorted_nums[right]])

                    #we need to move left and right forward so that we can do other cals, need to do the same check as
                    #whene we normally move pointers
                    val = sorted_nums[left]
                    while left < right and sorted_nums[left] == val:
                        left += 1
                    
                    val = sorted_nums[right]
                    
                    while right > left and sorted_nums[right] == val:
                        right -= 1
                    
        return res
        