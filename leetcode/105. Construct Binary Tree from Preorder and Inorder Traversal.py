#The root of the tree will be always preorder's first index. And index the preorder and inorder to give left and right child
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1: mid+1] , inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1 :])
        return root
