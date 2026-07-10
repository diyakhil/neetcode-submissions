# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
         #use a var to record carry over and add it to next sum
        carryover = 0
        res = ListNode(0)
        head = res

        while l1 and l2:
            _sum = l1.val + l2.val + carryover
            digit = _sum % 10
            carryover = _sum // 10

            new_node = ListNode(digit)
            head.next = new_node
            head = head.next

            l1 = l1.next
            l2 = l2.next
        
        while l1:
            _sum = l1.val + carryover
            digit = _sum % 10
            carryover = _sum // 10

            new_node = ListNode(digit)
            head.next = new_node
            head = head.next

            l1 = l1.next

        while l2:
            _sum = l2.val + carryover
            digit = _sum % 10
            carryover = _sum // 10

            new_node = ListNode(digit)
            head.next = new_node
            head = head.next

            l2 = l2.next
        
        #need to make sure if there is a value there for carryover, then it is appended to the end
        #eg 5+5 = 10 (the one will be in the carryover)

        if carryover > 0:
            new_node = ListNode(carryover)
            head.next = new_node
        return res.next
        