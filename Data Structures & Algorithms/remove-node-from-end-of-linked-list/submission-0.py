# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #2nd from the end is just len(list) - 2 + 1 from the start

        #lets go thru the whole list and keep track of the count of nodes first
        #then we will simply just remove that value from the front
        count = 0
        temp = head
        while temp:
            count += 1
            temp = temp.next
        
        front_val = count - n + 1

        if count == 1: return None
        #just keep track of a prev value until we hit the value that we want
        prev = None
        curr = head
        
        #starts from 0, our counting starts from 1
        for i in range(1, front_val):
            prev = curr
            curr = curr.next
        
        if prev:
            prev.next = curr.next
        else:
            #EDGE CASE - need to move head if head is no longer in the list
            prev = curr.next
            head = curr.next
        curr.next = None

        return head
        