# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        def add( root, val, depth, curr):
            if not root:
                return None

            if curr == depth - 1:
                lTemp = root.left
                rTemp = root.right

                root.left = TreeNode(val)
                root.right = TreeNode(val)
                root.left.left = lTemp
                root.right.right = rTemp

                return root

            root.left = add(root.left, val, depth, curr + 1)
            root.right = add(root.right, val, depth, curr + 1)

            return root


        if depth == 1:
            newRoot = TreeNode(val)
            newRoot.left = root
            return newRoot

        return add(root, val, depth, 1)
