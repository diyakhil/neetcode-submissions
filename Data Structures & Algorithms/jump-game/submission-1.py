class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal_index = len(nums) - 1
        for i in range(len(nums) -2, -1, -1):
            if goal_index - i <= nums[i]:
                goal_index = i
        
        return goal_index == 0
        