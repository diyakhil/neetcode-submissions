class Solution:
    def isPalindrome(self, s: str) -> bool:
        #go through string, removing any non alphaumeric chars and save to list
        cleaned = []

        for c in s:
            if c.isalnum():
                cleaned.append(c.lower())
        #have one pointer at the start and one at the end
        left = 0
        right = len(cleaned) - 1

        while left <= right:
            if cleaned[left] != cleaned[right]:
                return False
            left += 1
            right -= 1

        return True
        