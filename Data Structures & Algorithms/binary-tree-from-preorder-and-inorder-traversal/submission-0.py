# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #have to check the empty list case
        if not preorder and not inorder:
            return
        
        if len(preorder) == 1 and len(inorder) == 1:
            return TreeNode(preorder[0])
        
        root_val = preorder[0]

        root_index = inorder.index(root_val)

        #have to skip over current ndoe we made root so starting indexing at 1
        pre_left = preorder[1:root_index + 1]
        pre_right = preorder[root_index+1:]

        in_left = inorder[:root_index]
        in_right = inorder[root_index+1:]

        new_node = TreeNode(root_val)

        new_node.left = self.buildTree(pre_left, in_left)
        new_node.right = self.buildTree(pre_right, in_right)

        return new_node
        