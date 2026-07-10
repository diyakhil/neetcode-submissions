class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #if sum is greater than target then move right pointer down,
        #otherwise move left pointer up

        left = 0
        right = len(numbers) - 1

        while left <= right:
            if numbers[left] + numbers[right] > target:
                right -= 1
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                return [left + 1, right + 1]
        