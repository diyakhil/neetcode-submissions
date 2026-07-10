# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        :type root: TreeNode
        :rtype: int
        """

        #NEED a GLOBAL VAR for count, every node at each step will have a diff version of count
        #don't need to do this for curr_max b/c we want diff versions of it as we go down the tree
        self.count = 0

        def helper(root, curr_max):
            if not root:
                return

            if root.val >= curr_max:
                self.count += 1
            
            new_max = max(curr_max, root.val)

            helper(root.left, new_max)
            helper(root.right, new_max)
        
        helper(root, root.val)

        return self.count
        