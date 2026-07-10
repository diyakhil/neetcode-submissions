class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0

        #just do an infinite loop
        while True:
            slow = nums[slow] #this is the next index we want to visit replacement for slow = slow.next
            fast = nums[nums[fast]]

            if slow == fast:
                break
        
        #put another slow pointer at the start of list and where the pointers intersect next
        #is the start of the cycle

        #forget the fast pointer
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]

            if slow == slow2:
                break
        
        return slow
        