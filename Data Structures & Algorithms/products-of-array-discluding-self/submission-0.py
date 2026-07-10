class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        #keep a list of all of the products of values from the start -> end and end -> start
        #eg. [1, 2, 4, 6] -> [1, 2, 8, 48] and [48, 48, 24, 6]

        #to calculate the product at i, take the value after in the desc list
        #and multiply it by the value before in the asc list

        asc = [0] * len(nums)
        desc = [0] * len(nums)

        #remember to multiply by the prev asc or desc number b/c that's keeping track of cumulative
        for i in range(len(asc)):
            if i > 0:
                asc[i] = asc[i-1] * nums[i]
            else:
                asc[i] = 1 * nums[i]
        
        for i in range(len(asc) -1, -1, -1):
            if i < len(asc) - 1:
                desc[i] = desc[i+1] * nums[i]
            else:
                desc[i] = 1 * nums[i]
        
        res = [0] * len(nums)

        for i in range(len(nums)):
            if i == len(nums) -1:
                res[i] = asc[i-1] * 1
            elif i == 0:
                res[i] = 1 * desc[i+1]
            else:
                res[i] = asc[i-1] * desc[i+1]
        return res
