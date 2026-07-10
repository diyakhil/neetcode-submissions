class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_i = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            #this means target - nums[i] is in hashmap which is other val
            if complement in num_to_i.keys():
                return sorted([i, num_to_i[complement]])
            
            num_to_i[nums[i]] = i
        