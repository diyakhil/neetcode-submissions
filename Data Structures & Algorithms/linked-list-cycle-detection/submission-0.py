# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        
        slow = head
        fast = head.next

        while slow != None and fast != None:
            if slow == fast:
                return True

            slow = slow.next
            
            if fast.next:
                fast = fast.next.next
            else:
                return False
        
        return False