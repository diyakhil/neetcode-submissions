# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        return self.helper(lists) #make sure to return the final algo
    
    def helper(self, l):
        if len(l) == 0:
            return
        if len(l) == 1:
            return l[0] #make sure here we are actually returning the list and not just the array containing the list
        
        mid = len(l) // 2
        
        list1 = self.helper(l[:mid])
        list2 = self.helper(l[mid:])
        return self.merge2Lists(list1, list2)
        

    def merge2Lists(self, list1, list2):
        merged_list = ListNode(0)
        head = merged_list

        while list1 and list2:
            if list1.val <= list2.val:
                head.next = list1
                list1 = list1.next
                head = head.next
            else:
                head.next = list2
                list2 = list2.next
                head = head.next
        
        #now check if any values remain in either list
        if list1:
            head.next = list1
        if list2:
            head.next = list2
        
        return merged_list.next
        