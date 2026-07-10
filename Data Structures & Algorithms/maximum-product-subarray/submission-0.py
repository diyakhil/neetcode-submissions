class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #keep track of a min and max for each square in the array. return the max value in the last square of the array
        #when we encounter a 0, reset min and max
        #have a global min and max, no need for a local one, reset it to 1 when we encounter a zero
        #we can either use or not use the last value

        _min = 1
        _max = 1
        result = float("-inf")

        dp = [0] * len(nums)

        for i in range(0, len(nums)):
            if nums[i] == 0:
                _min = 1
                _max = 1
                result = max(result, 0)
                continue
            
            #2 choices are using the prev value or not using it
            #NOTICE HOW WE ARE ALWAYS INCLUDING NUMS[I] - this is why the chain is never broken
            value_with_prev_min = _min * nums[i]
            value_with_prev_max = _max * nums[i]
            value_without = nums[i]

            #since we aren't using _min or _max within the comparison, we don't have to worry about chain breaking
            _max = max(value_with_prev_min, value_with_prev_max, value_without)
            _min = min(value_with_prev_min, value_with_prev_max, value_without)

            result = max(result, _max)
       
        return result
        