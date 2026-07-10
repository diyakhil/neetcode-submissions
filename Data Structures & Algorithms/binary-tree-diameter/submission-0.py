# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def helper(root):
            #we have gone out of the boundaries of the tree
            if not root:
                return 0
            
            #need to check left and right because we don't want to add a 1 if left or right doesn't exist
            left_len = helper(root.left)
            right_len = helper(root.right)

            #this is the step where we "close off the tree", need to account for this max value
            self._max = max(self._max, left_len + right_len)

            return 1 + max(left_len, right_len)
            #one accounts for the edge connected from the current node to it's parent node
        
        self._max = 0 #this is our "global var" to keep track of the max value -> need to declare it "self."

        helper(root)
        return self._max
        