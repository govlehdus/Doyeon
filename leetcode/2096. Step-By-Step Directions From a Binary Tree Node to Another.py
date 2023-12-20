class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def find(n: TreeNode, val: int, path: List[str]) -> bool:
            if n.val == val:
                return True
            if n.left and find(n.left, val, path):
                path +="L"
            elif n.right and find(n.right, val,path):
                path += "R"
            return path
        c, d = [], []
        find(root, startValue, c)
        find(root, destValue, d)

        while c and d and c[-1] == d[-1]:
            c.pop()
            d.pop()
        return "".join("U" * len(c)) + "".join(reversed(d))
