class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = [pushed.pop(0)]
        while pushed or popped:
            if not stack:
                stack.append(pushed[0])
                pushed.pop(0)
           
            if pushed:
                if stack[-1] == popped[0]:
                    stack.pop()
                    popped.pop(0)
                else:
                    stack.append(pushed[0])
                    pushed.pop(0)
            else:
                if stack[-1] == popped[0]:
                    stack.pop()
                    popped.pop(0)
                else:
                    return False
        return True
