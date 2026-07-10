"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        :type head: Node
        :rtype: Node
        """
        old_new = {} #new node created to old node that it is duplicating

        aux_node = Node(0)
        new_head = aux_node

        old_head = head

        while old_head:
            new_node = Node(old_head.val)
            old_new[old_head] = new_node #update mapping in list old:new
            
            new_head.next = new_node

            #increment both old and new to next node
            new_head = new_head.next
            old_head = old_head.next
        
        old = head
        new = aux_node.next
        #iter 2 to fill in random pointers
        while old:
            new_random = None
            
            if old.random:
                new_random = old_new[old.random]
            new.random = new_random

            old = old.next
            new = new.next

        return aux_node.next
        