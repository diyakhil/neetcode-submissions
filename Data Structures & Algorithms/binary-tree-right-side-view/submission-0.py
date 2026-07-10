# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        if not root:
            return res

        queue = [root]

        while queue:
            #pop right most node and add to result
            #CAN'T pop b/c we need to append the children in the loop below, just access it
            rightmost = queue[-1] #rightmost node will be at the end

            res.append(rightmost.val)

            #go through res of the queue and pop all the nodes in the level and add their children
            #pop from the front as we will be adding children to the back
            nodes_in_level = len(queue)

            for _ in range(nodes_in_level):
                curr_node = queue.pop(0)

                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
        return res
        