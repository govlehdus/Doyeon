"""First there are three conditions, it is opening parenthesis, it is closing parenthesis that has opening parenthesis in front, and it is closing parenthesis that
doesn't have matching opening parenthesis. Using stack, since it is LIFO, I make a condition for the opening parenthesis and closing parenthesis."""
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opens = {')': '(', '}': '{', ']': '['}
        for i in s:
            if i not in opens:
                stack.append(i)
            else:
                if not stack or stack[-1] != opens[i]:
                    return False
                else:
                    stack.pop()
        return not stack

            
