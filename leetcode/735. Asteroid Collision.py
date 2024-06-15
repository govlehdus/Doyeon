class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ast in asteroids:
            stack.append(ast)

            while len(stack) >=2:
                if  (stack[-1] < 0 and stack[-2] >0):
                    if abs(stack[-1]) > abs(stack[-2]):
                        stack.pop(-2)
                    elif abs(stack[-1]) < abs(stack[-2]):
                        stack.pop()
                    else:
                        stack.pop()
                        stack.pop()
                else:
                    break
        return stack
