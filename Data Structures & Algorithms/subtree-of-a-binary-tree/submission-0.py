# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, root, subroot):
        if not root and not subroot:
            #KEY: cannot just set value to true here, because this branch may execute last and overrite the prev failures from another branch of recursion since isSame is a global var
            return True
        
        #checks if one tree has a node and the other one doesn't (mismatch so return false)
        if not root or not subroot:
            return False
        
        if root.val != subroot.val:
            return False
        
        return self.isSameTree(root.left, subroot.left) and self.isSameTree(root.right, subroot.right)
           
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #this is the function that will scan
        if not root:
            return False
        
        #need to reset this before the call since isSame is a global var and isSameTree's logic depends on isSame being initialized to true first
        isSame = self.isSameTree(root, subRoot)

        if isSame:
            return True
        
        #search for sub tree in right and left halves
        #if tree is found in either half, then we should return True (tree does not need to be in both halves)
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        