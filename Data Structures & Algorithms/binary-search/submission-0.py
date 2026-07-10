class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #input: array of nums in sorted order
        #output: index of num which matches up with the target, otherwise -1

        left = 0
        right = len(nums) - 1

        #we want it to cross over
        while left <= right:
            med = (left + right) // 2

            if nums[med] > target:
                #need to move right down and make search on the smaller side of array
                right = med - 1
            elif nums[med] < target:
                left = med + 1
            else:
                return med
        return -1
        