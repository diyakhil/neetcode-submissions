# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        
        start = head
        count = 1
        
        while count < k and start.next:
            count += 1
            start = start.next
        
        #this is our base case
        if count != k:
            return head
        
        #otherwise slice out the list
        _next = start.next
        start.next = None
        new_head = _next
        
        reversed_part = self.reverseList(head)
        head.next = self.reverseKGroup(new_head, k)
        
        return reversed_part
    
    def reverseList(self, head):
        prev = None
        curr = head

        while curr:
            _next = curr.next
            curr.next = prev
            
            prev = curr
            curr = _next
        return prev #curr will already be null, prev is what will point to the last node
        