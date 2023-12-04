#Having a val that is the list of all the nodes' value in the same level, and add its' last element, so it will be the same as the right side view.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        if root:
            stack.append(root)

        while stack:
            val = []

            for i in range(len(stack)):
                node = stack.pop(0)
                val.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            res.append(val[-1])
        return res
        
