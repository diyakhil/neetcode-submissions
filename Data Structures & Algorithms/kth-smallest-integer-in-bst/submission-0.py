# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0 
        self.val = 0 
        def helper(root): 
            if not root: 
                return 
            
            helper(root.left) 
            
            self.count += 1 

            if self.count == k: 
                self.val = root.val 
                return
            
            helper(root.right) 
        
        helper(root)
        return self.val
        