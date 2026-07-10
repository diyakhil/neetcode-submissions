# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.isSame = True

        def helper(p, q):
            #return if one of the values is None
            if not p and not q:
                return

            #KEY: 
            if not p or not q:
                self.isSame = False
                return
            
            #this is in order traversal b/c we are checking values first and then recursing
            if p.val != q.val:
                self.isSame = False
            
            helper(p.left, q.left)
            helper(p.right, q.right)
        
        helper(p, q)
        return self.isSame
        