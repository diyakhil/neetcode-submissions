class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #height will be the min of the 2 heights we are examining currently
        #width will be the distance between the 2 indices 

        left = 0
        right = len(heights) - 1

        res = 0

        while left <= right:
            h = min(heights[left], heights[right])
            width = right - left

            res = max(res, h * width)

            #now move up whichever side is causing the bottleneck (limiting behavior)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return res
        