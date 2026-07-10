# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root, float("-inf"), float("inf"))
        
    def helper(self, root, minimum, maximum):
        if not root:
            return True
        
        if root.val <= minimum or root.val >= maximum:
            return False
        
        #left side update max with root value as ceil and inherit min from prev call
        left = self.helper(root.left, minimum, root.val)

        #right side update min with root value as floor and inherit max from prev call
        right = self.helper(root.right, root.val, maximum)

        #if even one of them returns false, then everything should be false
        return left and right
        