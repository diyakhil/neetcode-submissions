class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(goal, -1, -1):
            #KEY: have to add i here b/c i is starting point of jump
            if i + nums[i] >= goal:
                goal = i
        if goal > 0:
            return False
        return True
        