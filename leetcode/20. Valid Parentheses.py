class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        di = {']':'[', '}':'{',')':'('}
        for p in s:
            if p not in di:
                stack.append(p)
                continue
            if not stack or stack[-1] != di[p]:
                return False
            stack.pop()
        return True if len(stack) == 0 else False
