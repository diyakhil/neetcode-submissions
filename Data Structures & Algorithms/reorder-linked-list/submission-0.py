# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        stack = []

        start = head

        while start:
            stack.append(start)
            start = start.next
        
        aux_node = ListNode(0)
        new_head = aux_node

        while stack:
            popped = stack.pop(0)
            popped.next = None
            
            new_head.next = popped
            new_head = new_head.next

            if stack:
                popped = stack.pop()
                popped.next = None
                new_head.next = popped
                new_head = new_head.next
        
        aux_node.next