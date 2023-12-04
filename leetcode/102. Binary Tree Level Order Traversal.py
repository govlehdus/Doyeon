#Using a deque, to pop the left which is the node of the one level, and add the value of the node.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        stack = collections.deque()
        if root:
            stack.append(root)
        while stack:
            val = []

            for i in range(len(stack)):
                node = stack.popleft()
                val.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            res.append(val)

        return res
