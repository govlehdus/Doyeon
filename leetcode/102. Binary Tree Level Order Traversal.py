# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return root

        queue = []
        res = []
        queue.append(root)
        while len(queue) > 0:
            ans = []
            for i in range(len(queue)):
                nod = queue.pop(0)
                if nod.left:
                    queue.append(nod.left)
                if nod.right:
                    queue.append(nod.right)
                ans.append(nod.val)
            res.append(ans)
        return res
