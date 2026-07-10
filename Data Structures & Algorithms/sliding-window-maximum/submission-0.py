class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        #need to store the index of the curr_max along with the value to make sure its still in window
        res = []
        curr_window = deque() #store indices here

        right = 0
        left = 0

        while right < len(nums):
            #need to make sure no smaller values are in queue, and if they are then we need to remove
            #curr_window[-1] is the easiest way to access the last value in the queue
            while curr_window and nums[curr_window[-1]] < nums[right]:
                #popping from right of queue
                curr_window.pop()
            
            curr_window.append(right)

            #remove from queue if out of bounds
            if left > curr_window[0]:
                #popping from left of queue b/c that is where the smallest indices will be
                curr_window.popleft()

            if right - left + 1 == k:
                #only update result when we have reached our window size
                res.append(nums[curr_window[0]])

                #only decrement window when we have reached the full size
                left += 1
            #incrementing right regardless
            right += 1
        return res
        