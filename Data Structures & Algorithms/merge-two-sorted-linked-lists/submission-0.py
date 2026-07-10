# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #create an auxiliary node to start the result
        aux_node = ListNode(0)

        res = aux_node

        #loop until one of the lists is empty
        while list1 != None and list2 != None:
            if list1.val <= list2.val:
                res.next = list1
                list1 = list1.next
                res = res.next
            else:
                res.next = list2
                list2 = list2.next
                res = res.next
        #need to append the remainder of the list that is not none to the resulting list

        while list1 != None:
            res.next = list1
            list1 = list1.next
            res = res.next
        
        while list2 != None:
            res.next = list2
            list2 = list2.next
            res = res.next
        return aux_node.next
        