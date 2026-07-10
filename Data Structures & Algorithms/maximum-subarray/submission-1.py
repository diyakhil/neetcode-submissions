class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #relation is prev_sum = max(nums[i], nums[i] + prev_sum)

        #logic is that we want to compare the current value b/c when we hit a negative, we want to 'reset'
        #since we will just keep going negative if we keep adding negative number

        #at each step record the max
        _max = float('-inf')

        prev_sum = 0

        for i in range(len(nums)):
            #we are either starting the sequence from here or continuing the prev one
            #prev_sum = nums[i] will reset the sequence to the current value
            prev_sum = max(nums[i], prev_sum + nums[i])

            _max = max(_max, prev_sum)

        return _max
        