# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return root
        queue = []
        res = []
        queue.append(root)
        count = 0
        while len(queue) > 0:
            ans = []
            for i in range(len(queue)):
                node = queue.pop(0)
                ans.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if count % 2 == 0:
                res.append(ans)
                count +=1
            else:
                res.append(reversed(ans))
                count +=1
        return res
