# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        if not root:
            return res

        queue = [root]

        while queue:
            curr_res = []

            #use a for loop and take the length of the queue before we start appending stuff to it
            #if we use a while loop here (while queue) and keep appending things, we will never reach end of queue

            nodes_on_lev = len(queue)

            for i in range(nodes_on_lev):
                curr_node = queue.pop(0)
                curr_res.append(curr_node.val)
                
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
            
            res.append(curr_res)
        return res
        