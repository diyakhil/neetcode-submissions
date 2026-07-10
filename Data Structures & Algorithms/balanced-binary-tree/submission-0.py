# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #this will return depth values not bool b/c that is what we will need for the following calls to determine height
        def helper(root):
            if not root:
                return 0
            
            left_len = helper(root.left)
            right_len = helper(root.right)

            if abs(left_len - right_len) > 1: #have to take absolute value of diff to not end up w negatives
                self.is_balanced = False
            
            return 1 + max(left_len, right_len)
        
        self.is_balanced = True

        helper(root)

        return self.is_balanced
        